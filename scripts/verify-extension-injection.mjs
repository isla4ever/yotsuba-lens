import { mkdtemp, rm } from "node:fs/promises";
import { createServer } from "node:http";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { chromium } from "playwright";

const extensionPath = resolve(".output/chrome-mv3");
const profilePath = await mkdtemp(join(tmpdir(), "design-lens-injection-"));
const server = createServer((_request, response) => {
  response.writeHead(200, { "content-type": "text/html; charset=utf-8" });
  const controls = Array.from({ length: 48 }, (_, index) => `<button id="control-${index}" class="fixture-control">Control ${index + 1}</button>`).join("");
  response.end(`<!doctype html><html><head><title>Injection fixture</title><style>
    body { margin: 0; font: 16px sans-serif; }
    main { padding: 24px; }
    .fixture-grid { display: grid; grid-template-columns: repeat(8, minmax(100px, 1fr)); gap: 8px; }
    .fixture-control { min-height: 36px; border-radius: 6px; transition: transform 160ms ease; }
  </style></head><body><main><h1>Design Lens injection fixture</h1><section class="fixture-grid">${controls}</section></main></body></html>`);
});
await new Promise((resolvePromise, reject) => {
  server.once("error", reject);
  server.listen(0, "127.0.0.1", resolvePromise);
});

const address = server.address();
if (!address || typeof address === "string") throw new Error("Injection fixture server did not expose a TCP port");
const fixtureUrl = `http://127.0.0.1:${address.port}/`;
let context;

try {
  context = await chromium.launchPersistentContext(profilePath, {
    channel: "chromium",
    headless: true,
    args: [`--disable-extensions-except=${extensionPath}`, `--load-extension=${extensionPath}`]
  });
  let worker = context.serviceWorkers()[0];
  if (!worker) worker = await context.waitForEvent("serviceworker");
  const page = await context.newPage();
  await page.goto(fixtureUrl, { waitUntil: "domcontentloaded" });

  const tab = await worker.evaluate(async (url) => {
    const tabs = await chrome.tabs.query({});
    return tabs.find((item) => item.url?.startsWith(url)) ?? null;
  }, fixtureUrl);
  if (!tab?.id) throw new Error("Injection fixture tab was not found");

  await worker.evaluate(async (tabId) => {
    await chrome.scripting.executeScript({ target: { tabId }, files: ["/content-scripts/content.js"] });
  }, tab.id);
  const status = await worker.evaluate(async (tabId) => chrome.tabs.sendMessage(tabId, {
    type: "DESIGN_LENS_RECORD_STATUS",
    locale: "en"
  }), tab.id);
  if (!status?.ok || status.isRecording) throw new Error("Injected page bridge did not return an idle status");

  const captureResponse = await worker.evaluate(async (tabId) => chrome.tabs.sendMessage(tabId, {
    type: "DESIGN_LENS_CAPTURE_PAGE"
  }), tab.id);
  if (!captureResponse?.ok) throw new Error(`Dense fixture capture failed: ${captureResponse?.error ?? "unknown error"}`);
  const evidenceCounts = {
    components: captureResponse.capture.components.length,
    motion: captureResponse.capture.motion.length,
    interactions: captureResponse.capture.interactions.length
  };
  if (evidenceCounts.components <= 32 || evidenceCounts.motion <= 32 || evidenceCounts.interactions <= 32) {
    throw new Error(`Dense fixture evidence was unexpectedly capped: ${JSON.stringify(evidenceCounts)}`);
  }

  console.log(JSON.stringify({ injected: true, messageBridge: true, uncappedEvidence: true, evidenceCounts, fixtureUrl }, null, 2));
} finally {
  await context?.close().catch(() => undefined);
  await new Promise((resolvePromise) => server.close(resolvePromise));
  await rm(profilePath, { recursive: true, force: true });
}

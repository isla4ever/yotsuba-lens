import { chromium } from "playwright";
import { fileURLToPath } from "node:url";
import path from "node:path";

const sourceDir = path.dirname(fileURLToPath(import.meta.url));
const outputDir = path.resolve(sourceDir, "..");
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1800, height: 1200 }, deviceScaleFactor: 1 });

await page.goto(new URL("./readme-assets.html", import.meta.url).href);
await page.evaluate(() => document.fonts.ready);

for (const name of ["readme-hero", "workspace-showcase", "evidence-flow"]) {
  const target = page.locator(`[data-export="${name}"]`);
  await target.screenshot({
    path: path.join(outputDir, `${name}.jpg`),
    type: "jpeg",
    quality: 94,
  });
}

await browser.close();

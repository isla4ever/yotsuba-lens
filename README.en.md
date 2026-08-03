<p align="center">
  <img src="docs/store-assets/icon-128.png" alt="Yotsuba Style Extractor icon" width="128" height="128" />
</p>

<h1 align="center">Yotsuba Style Extractor</h1>
<p align="center"><strong>Extract colors, layouts, components, interactions, and motion into a prompt you can use.</strong></p>

<p align="center">
  <a href="https://github.com/isla4ever/yotsuba-lens/actions/workflows/ci.yml"><img src="https://github.com/isla4ever/yotsuba-lens/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <img src="https://img.shields.io/badge/version-0.3.1-2563eb" alt="Version 0.3.1" />
  <img src="https://img.shields.io/badge/Chrome-MV3-4285f4" alt="Chrome MV3" />
  <img src="https://img.shields.io/badge/status-published-16a34a" alt="Published" />
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-16a34a" alt="MIT License" /></a>
</p>

<p align="center"><a href="README.md">中文</a> · <strong>English</strong></p>

<p align="center">
  <img src="docs/readme-assets/readme-hero.jpg" alt="Yotsuba extracts webpage styles and generates a reusable prompt" width="100%" />
</p>

Found a webpage you like but do not know how to describe its colors, layout, or interactions to a coding tool? Run Smart Capture once. Yotsuba organizes the page style, component structure, interaction states, and motion into a practical prompt and reference pack.

```text
Open page → Smart Capture → Review styles and gaps → Generate prompt / reference pack → Start building
```

> [!IMPORTANT]
> Version `0.3.0` is live in the Chrome Web Store. This repository is preparing the clearer `0.3.1` naming and description update. Use it only on pages you are authorized to analyze, reference, or reproduce.

## What It Helps You Do

| Your goal | What Yotsuba does | What you get |
| --- | --- | --- |
| **Reference a webpage style** | Extract colors, type, spacing, layout, components, and visual effects | A style reference you can adapt to a new project |
| **Generate a better prompt** | Turn captured page features into structured implementation requirements | A prompt ready for common coding tools |
| **Reproduce an authorized page** | Preserve key screenshots, dimensions, states, and checks | A bounded rebuild pack instead of a vague “make it similar” request |
| **Capture hover and open states** | Point out missing states and ask only for the necessary follow-up | No need to record the entire browsing session |

## Real Workspace

<p align="center">
  <img src="docs/readme-assets/workspace-showcase.jpg" alt="Yotsuba Lens coverage and capture settings beside a real webpage" width="100%" />
</p>

Clicking the extension action opens the Side Panel by default. Overview, coverage, history, and settings share one workspace, while the popup keeps only frequent actions. Capture results show extracted content, missing states, and the next useful task.

<details>
  <summary><strong>View history and delete confirmation</strong></summary>
  <br />
  <p align="center">
    <img src="docs/store-assets/screenshot-history-dark-1280x800.png" alt="Yotsuba Lens history and delete confirmation" width="960" />
  </p>
</details>

## From Webpage To Prompt And Reference Pack

<p align="center">
  <img src="docs/readme-assets/evidence-flow.jpg" alt="Yotsuba Lens turns live webpage evidence into Prompt, Evidence, and Acceptance outputs" width="100%" />
</p>

Generated prompts are grounded in the page features that were actually captured. Missing states remain visible instead of being presented as a complete reproduction.

| Mode | Best for | Output boundary |
| --- | --- | --- |
| **Reference** | Borrowing visual, layout, motion, or interaction ideas for an original interface | Extract transferable design grammar without copying the reference brand, content, or assets |
| **Authorized Rebuild** | Building a verifiable draft for an explicit page, viewport set, and state set | Be accountable only for captured evidence; uncaptured states remain gaps |

## Core Capabilities

| Capability | Implementation boundary |
| --- | --- |
| **Smart Capture safety budget** | Baseline work shares a 15-second budget; Rebuild screenshots and CDP finalization use independent timeouts and circuit breakers, with cancellation and degradation for mutation storms or very large DOMs |
| **Guided supplemental capture** | Merge gaps into at most three scroll, hover, focus, open, or responsive tasks; users perform real actions while the extension only observes and saves the target state |
| **Side Panel by default** | Mode, capture, coverage, history, configuration, and export stay together; first-use guidance appears before generating AI output |
| **On-demand injection and split permissions** | The page bridge is injected only after a user action; Standard excludes `debugger`, while deeper CDP collection is isolated in Collector |
| **Scene-based acceptance** | Rebuild Packs can drive screenshot, pixel, geometry, motion-checkpoint, and browser-error checks without inventing uncaptured behavior |

## More Than Screenshot-To-Prompt

| Dimension | Typical screenshot workflow | Yotsuba Lens |
| --- | --- | --- |
| Input | One or several static screenshots | DOM, tokens, geometry, screenshots, events, motion, and runtime clues |
| Interaction states | Described manually or guessed by a model | Real hover, focus, scroll, open, and responsive scene evidence |
| Missing information | Often filled in as an imagined result | Recorded explicitly as `missing`, `partial`, or `not-applicable` |
| Output | One generic prompt | Evidence Pack, AI Prompt Pack, or Rebuild Draft Pack |
| Acceptance | Visual judgment alone | Explainable candidate reports based on captured scenes |

## Workflow

1. **Open a page**: visit a normal `http` or `https` page and click Yotsuba Lens; the Side Panel opens by default.
2. **Choose the outcome**: use Reference for original design direction or Rebuild for an authorized implementation draft.
3. **Run Smart Capture**: collect baseline evidence; the page bridge is injected on demand only after this kind of user action.
4. **Review gaps**: use the Side Panel and complete guided capture only for important missing states.
5. **Organize the project**: import a Recorder plan or add up to eight same-origin routes to a Rebuild project.
6. **Export and build**: hand the evidence or prompt pack to an AI coding agent.
7. **Verify the candidate**: replay only evidenced Rebuild scenes without inventing uncaptured behavior.

## Output Packs

| Pack | Main files | Use it for |
| --- | --- | --- |
| **Evidence-only Pack** | `README.md`, `skill.md`, `evidence.json` | Saving, sharing, or handing structured design evidence to any AI tool |
| **AI Prompt Pack** | Evidence files, `ai-coding-prompt.md`, `ai-implementation-brief.md` | Generating a target-specific coding prompt with an OpenAI-compatible model |
| **Rebuild Draft Pack** | `capture-project-v2.json`, `scene-manifest.json`, `acceptance.json`, screenshots, and bounded artifacts | Preserving authorized baselines, explicit gaps, and candidate acceptance rules |

## Install

Requirements: Node.js `>=22.13.0`, npm `>=10`, and Chrome or another Chromium browser.

### Standard Build

```bash
npm ci
npm run build
```

Open `chrome://extensions`, enable **Developer mode**, choose **Load unpacked**, and select:

```text
<project-root>/.output/chrome-mv3
```

The standard build does not request Chrome's `debugger` permission. Use it for everyday Reference and baseline Rebuild capture.

### Collector Build

```bash
npm run build:collector
```

Load `<project-root>/.output/collector/chrome-mv3`. Collector adds `debugger` for authorized DOMSnapshot, matched CSS, geometry, viewport, and animation evidence. Canvas bitmap capture is off by default and bounded by count, pixel-area, and file-size budgets.

## Rebuild Candidate Acceptance

```bash
npm run verify:rebuild -- \
  --pack <rebuild-pack.zip> \
  --url http://localhost:3000
```

The verifier replays only initial, scroll, hover, focus, and open states supported by `scene-manifest.json`. It produces JSON/HTML reports, candidate screenshots, diffs, and focused repair context for an agent.

See the [AstroWind reconstruction benchmark](docs/astrowind-rebuild-benchmark.md) and the [Bilibili homepage capture and reconstruction benchmark](docs/bilibili-rebuild-benchmark.md) for real capture, candidate, and error measurements. Both reports keep failed cases visible; the Bilibili case also exercises recovery on a high-mutation page and stable-node acceptance.

## Privacy And Permissions

Yotsuba Lens processes and exports evidence locally by default. It sends a reduced evidence payload only when a user configures a model key and explicitly requests AI output. That payload is designed to exclude raw DOM, cookies, local storage, credentials, screenshots, and unmasked input values.

| Permission | Purpose |
| --- | --- |
| `activeTab`, `scripting` | Inject the page bridge and capture the active page after a user action |
| `storage` | Store locale, theme, workspace metadata, and optional AI settings locally |
| `tabs`, `sidePanel` | Identify the active tab and connect it to the persistent workspace |
| `<all_urls>` | Let users initiate capture across sites; it does not mean the extension runs automatically on every page |
| `debugger` | Included only in Collector for explicitly authorized, bounded deep collection |

Local Rebuild packs may contain visible page text, screenshots, and sanitized DOMSnapshot data. Treat them as potentially sensitive files. See [Privacy And Permissions](docs/privacy.md) for the complete boundary.

## Development And Quality Gates

```bash
npm run dev                 # Standard development server
npm run dev:collector       # Collector development server
npm run check:all           # TypeScript, 101 tests, and both production builds
npm run check:browser       # Real MV3 injection, UI alignment/overflow, and 20k/100k DOM recovery probes
npm run package:store       # Validate and create store candidate ZIPs and SHA256SUMS
```

Install Chromium before the first browser gate:

```bash
npx playwright install chromium
```

## Project Structure

```text
entrypoints/        WXT background, content, popup, and side panel entrypoints
src/analyzer/       Page structure, token, interaction, and motion analysis
src/capture-v2/     Rebuild projects, CDP Collector, scenes, and acceptance contracts
src/evidence/       Evidence packs and summaries
src/generators/     Evidence, prompt, and Skill generators
src/overlay/        In-page picker and guided supplemental capture controls
src/smart-capture/  Smart Capture budgets, orchestration, and gap tasks
src/storage/        IndexedDB workspace and artifact storage
scripts/            Release, stress-probe, and Rebuild verification tools
tests/              Behavior tests
docs/               Architecture, privacy, product decisions, and validation records
```

## Documentation And Contributing

- [Architecture](docs/architecture.md)
- [Privacy And Permissions](docs/privacy.md)
- [Validation](docs/validation.md)
- [AstroWind reconstruction benchmark](docs/astrowind-rebuild-benchmark.md)
- [Bilibili homepage capture and reconstruction benchmark](docs/bilibili-rebuild-benchmark.md)
- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Security Policy](SECURITY.md)
- [Release Checklist](docs/release-checklist.md)
- [Chrome Web Store Submission](docs/chrome-web-store-listing.md)

Open an issue before starting a large feature. Report security issues privately through [GitHub Private Vulnerability Reporting](https://github.com/isla4ever/yotsuba-lens/security/advisories/new).

## License

[MIT](LICENSE) © Isla

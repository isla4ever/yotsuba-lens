<p align="center">
  <img src="docs/store-assets/icon-128.png" alt="Yotsuba Style Extractor icon" width="128" height="128" />
</p>

<h1 align="center">Yotsuba Style Extractor</h1>
<p align="center"><strong>Turn a webpage's colors, layout, components, interactions, and motion into a practical prompt and design reference.</strong></p>

<p align="center">
  <a href="https://chromewebstore.google.com/detail/yotsuba-lens-%E7%BD%91%E9%A1%B5%E8%AE%BE%E8%AE%A1%E8%AF%81%E6%8D%AE%E9%87%87%E9%9B%86/imbmglmdajepbagbflgalkfokofcilag"><img src="https://img.shields.io/badge/Chrome-Install_Now-4285F4?logo=googlechrome&logoColor=white" alt="Install from the Chrome Web Store" /></a>
  <a href="https://github.com/isla4ever/yotsuba-lens/actions/workflows/ci.yml"><img src="https://github.com/isla4ever/yotsuba-lens/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <img src="https://img.shields.io/badge/version-0.3.1-2563eb" alt="Version 0.3.1" />
  <img src="https://img.shields.io/badge/Chrome-MV3-4285f4" alt="Chrome MV3" />
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-16a34a" alt="MIT License" /></a>
</p>

<p align="center"><a href="README.md">中文</a> · <strong>English</strong></p>

<p align="center">
  <a href="https://chromewebstore.google.com/detail/yotsuba-lens-%E7%BD%91%E9%A1%B5%E8%AE%BE%E8%AE%A1%E8%AF%81%E6%8D%AE%E9%87%87%E9%9B%86/imbmglmdajepbagbflgalkfokofcilag">
    <img src="docs/readme-assets/readme-hero.jpg" alt="Yotsuba extracts webpage styles and generates a practical prompt" width="100%" />
  </a>
</p>

Found a webpage you like but struggle to describe its design language to an AI coding tool? Yotsuba reads the visual and interaction details that actually exist on the current page, then organizes them into a structured prompt, a design reference, and verification criteria. It replaces vague “make it look similar” requests with usable implementation context.

> [!IMPORTANT]
> Version `0.3.0` is live in the Chrome Web Store. The clearer `0.3.1` naming and description update has been submitted for review and is expected to arrive soon. Existing installations will update automatically after approval. Use Yotsuba only on pages you are authorized to analyze, reference, or reproduce.

## Get Started

### 1. Install the extension

[**Install Yotsuba from the Chrome Web Store**](https://chromewebstore.google.com/detail/yotsuba-lens-%E7%BD%91%E9%A1%B5%E8%AE%BE%E8%AE%A1%E8%AF%81%E6%8D%AE%E9%87%87%E9%9B%86/imbmglmdajepbagbflgalkfokofcilag)

No source checkout or Node.js installation is required. Pin the extension to the Chrome toolbar for quick access.

### 2. Open a webpage

Visit a regular `http` or `https` page and click the extension icon. Yotsuba opens in Chrome's Side Panel by default, keeping the source page visible beside your workspace.

### 3. Capture and generate

Choose **Smart Capture**, review the extracted styles and missing states, then generate a prompt or export the reference pack. Basic page extraction requires no model setup. When you request AI-generated output, the first-use guide helps you add your own compatible model configuration.

```text
Open page → Smart Capture → Review result → Generate prompt / Export reference
```

## What You Get

| Use case | What Yotsuba extracts | Result |
| --- | --- | --- |
| **Describe a style to an AI tool** | Colors, type, spacing, radii, shadows, layout, and component patterns | A structured prompt ready for an AI coding tool |
| **Use a strong website as inspiration** | Transferable visual language, component styles, interaction, and motion clues | A design reference without the source brand or content |
| **Reproduce an authorized page** | Key screenshots, dimensions, page states, and verification requirements | A bounded rebuild reference that can be extended and checked |
| **Fill in hidden states** | Hover, focus, open, scroll, and responsive gaps | Up to three necessary follow-up tasks instead of a full recording session |

## Side Panel Workspace

<p align="center">
  <img src="docs/readme-assets/workspace-showcase.jpg" alt="Yotsuba capture results and settings beside a live webpage" width="100%" />
</p>

Overview, coverage, history, and settings share one Side Panel. The popup keeps only frequent actions. After capture, you can immediately see what was found, which states are missing, and what to do next.

<details>
  <summary><strong>View history and delete confirmation</strong></summary>
  <br />
  <p align="center">
    <img src="docs/store-assets/screenshot-history-dark-1280x800.png" alt="Yotsuba history and delete confirmation" width="960" />
  </p>
</details>

## Two Ways To Use It

| Mode | Best for | Boundary |
| --- | --- | --- |
| **Reference** | Borrowing colors, layout, components, motion, or interaction ideas for an original interface | Extract transferable design rules without copying the source brand, copy, or assets |
| **Authorized Rebuild** | Reproducing an explicit page, viewport, and state set within an authorized scope | Be accountable only for captured evidence; uncaptured states remain visible gaps |

<p align="center">
  <img src="docs/readme-assets/evidence-flow.jpg" alt="Yotsuba turns webpage details into a prompt and reference pack" width="100%" />
</p>

Generated output is grounded in captured page details. Missing interaction or responsive states remain marked as gaps rather than being presented as a complete reproduction.

## Privacy And Safety

- Page analysis and exports are processed locally by default.
- The extension reads the active page only after you start a capture. It does not scan every website in the background.
- Data is sent to a selected model provider only when you configure a model and explicitly request AI output.
- AI requests exclude cookies, local storage, credentials, raw DOM, screenshots, and unmasked input values.
- The standard Chrome Web Store build does not request the `debugger` permission.

See [Privacy And Permissions](docs/privacy.md) for the complete permission and data boundary.

## Open Source And Advanced Usage

<details>
  <summary><strong>Install the standard build from source</strong></summary>
  <br />

Requirements: Node.js `>=22.13.0`, npm `>=10`, and Chrome or another Chromium browser.

```bash
npm ci
npm run build
```

Open `chrome://extensions`, enable **Developer mode**, choose **Load unpacked**, and select `<project-root>/.output/chrome-mv3`.
</details>

<details>
  <summary><strong>Collector deep-capture build</strong></summary>
  <br />

```bash
npm run build:collector
```

Load `<project-root>/.output/collector/chrome-mv3`. Collector is for authorized deep capture only. It adds the `debugger` permission to collect budgeted DOMSnapshot, matched-style, geometry, viewport, and animation evidence. It is not distributed through the Chrome Web Store.
</details>

<details>
  <summary><strong>Exports and candidate verification</strong></summary>
  <br />

Yotsuba can export three types of material:

| Export | Best for |
| --- | --- |
| **Design Evidence Pack** | Saving, sharing, or handing structured evidence to any AI tool |
| **AI Prompt Pack** | Generating project-specific implementation requirements and a coding brief |
| **Rebuild Draft Pack** | Preserving authorized baselines, page states, explicit gaps, and verification rules |

Verify an authorized candidate page with:

```bash
npm run verify:rebuild -- \
  --pack <rebuild-pack.zip> \
  --url http://localhost:3000
```

The verifier checks only pages and states supported by captured evidence. See the [AstroWind reconstruction benchmark](docs/astrowind-rebuild-benchmark.md) and [Bilibili homepage capture and reconstruction benchmark](docs/bilibili-rebuild-benchmark.md) for real examples.
</details>

## Development

```bash
npm run dev                 # Standard development server
npm run dev:collector       # Collector development server
npm run check:all           # Type checks, tests, and both production builds
npm run check:browser       # MV3 injection, UI overflow, and large-DOM recovery checks
npm run package:store       # Build and validate Chrome Web Store candidates
```

Key documentation:

- [Architecture](docs/architecture.md)
- [Privacy And Permissions](docs/privacy.md)
- [Validation](docs/validation.md)
- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Security Policy](SECURITY.md)
- [Release Checklist](docs/release-checklist.md)

Open an issue before starting a large feature. Report security issues privately through [GitHub Private Vulnerability Reporting](https://github.com/isla4ever/yotsuba-lens/security/advisories/new).

## License

[MIT](LICENSE) © Isla

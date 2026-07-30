# Changelog

All notable changes to Design Lens are documented here. The project follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and uses semantic
versioning.

## Unreleased

### Changed

- Replace tag-triggered GitHub Releases with a manual Chrome Web Store v2
  submission workflow that uploads only the standard build and defaults to
  staged publishing after review.

## 0.3.0 - 2026-07-30

### Added

- Safety levels (`normal`, `reduced`, `snapshot-only`, and `stopped`), hard
  capture deadlines, cancellation propagation, and bounded finalization for
  responsive Smart Capture on large or continuously mutating pages.
- Per-file and per-project artifact budgets, orphan reclamation, shared-artifact
  protection, and explicit readiness labels for Reference and Rebuild results.
- Side Panel coverage, history, AI onboarding, Recorder import diagnosis,
  same-origin route projects, and guided capture for evidence gaps.
- Reproducible Bilibili and AstroWind capture/reconstruction benchmarks with
  explicit scene, geometry, screenshot, and failure evidence.
- Chrome Web Store icon, listing copy, privacy declarations, screenshots, and
  promotional artwork for the standard build.

### Changed

- Open the compact workflow as a native toolbar-anchored extension popup while
  keeping the Side Panel as the default action surface.
- Rename supplemental recording actions to Manual Capture and show a concise
  AI setup guide before first-time Prompt generation.
- Keep the Side Panel as the default workspace while the toolbar popup provides
  the same core mode and capture semantics in a compact form.

### Fixed

- Left-align history content, center delete icons, and require an inline
  confirmation before removing a capture.
- Dismiss transient Smart Capture progress notices automatically after capture
  completion without hiding persistent success or error messages.
- Skip the second full-page recording sample after Smart Capture has degraded
  to `snapshot-only` or `stopped`, preventing slow finalization on large pages.
- Calibrate browser-driver interaction latency against the same active fixture
  while retaining heartbeat, long-task, and frame-sample hard limits.

### Security

- Upgrade WXT to `0.21.2` so its unused vulnerable `web-ext-run` chain is
  removed, pin patched PostCSS, and retain the existing patched build-tool
  overrides.

## 0.2.0 - 2026-07-16

### Added

- Reference and authorized Rebuild workflows with evidence-specific exports.
- Budgeted Smart Capture with safe large-page degradation and recovery probes.
- Side Panel workspace for coverage, history, Recorder plans, and route projects.
- Task-aware guided capture for real hover, focus, scroll, open, wait, and
  responsive evidence without synthetic page actions.
- Standard and Collector packages with manifest permission validation.
- Pull request CI, browser stress gates, and reproducible store candidates.

### Changed

- Manual interaction recording is now supplemental rather than the default
  capture path.
- Deep Chrome DevTools Protocol inspection remains isolated to the separately
  authorized Collector build.

### Fixed

- Use 95th-percentile interaction latency for browser CI gates while retaining
  the maximum driver round-trip for diagnostics, avoiding single-runner
  scheduling outliers without weakening page long-task or heartbeat checks.
- Measure the continuously mutating stress fixture before capture so its own
  long tasks are not misattributed to the extension on slower CI runners.
- Upgrade official GitHub Actions to v7 so CI and packaging workflows use the
  supported Node runtime without deprecation warnings.
- Inject the page bridge only after an explicit user action instead of loading
  it on every website.
- Restore overlay, privacy-mask, and recording runtime state after preparation,
  storage, deep-capture, stop, and guided-capture failures.
- Require explicit open-state evidence for guided open tasks instead of treating
  unrelated DOM mutations as successful capture.
- Pinned patched transitive build-tool versions for esbuild, shell-quote, tmp,
  and uuid while upstream WXT dependencies catch up.
- Generate WXT types during dependency installation so TypeScript checks also
  pass in clean CI runners.

## 0.1.0 - 2026-06-29

### Added

- Initial Chrome MV3 extension for design tokens, component structure,
  interaction timelines, implementation traces, and AI-ready evidence packs.

[Unreleased]: https://github.com/isla4ever/design-lens/commits/main
[0.3.0]: https://github.com/isla4ever/design-lens/commit/dcb70d3c86ac4cb2133d16aa17c2f0b47fa5f4b1
[0.1.0]: https://github.com/isla4ever/design-lens/releases/tag/v0.1.0

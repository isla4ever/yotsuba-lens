# Privacy And Permissions

Yotsuba Lens is a local-first browser extension. This document describes the
behavior of the source build in this repository; a modified distribution may
behave differently.

## 中文摘要

Yotsuba Lens 仅在用户主动操作时采集当前网页的布局、样式、截图和交互状态证据，
并将其整理为设计参照或经授权重建所需的本地证据包。Chrome 应用商店披露的用户
数据类型包括：身份验证信息、网络记录、用户活动和网站内容。其中，身份验证信息
仅指用户自愿保存的可选 AI 服务 API Key；该密钥保存在 Chrome 本地存储中，且只会
作为授权凭据发送给用户选择的 AI 服务商。其他捕获数据默认保存在本机，只有用户
主动请求 AI 生成时，精简后的设计证据才会发送给其选择的服务商。Yotsuba Lens
不会出售这些数据，也不会将其用于广告、信用评估或与单一用途无关的目的。

## Activation And Default Behavior

- The extension does not register a content script that runs automatically on
  every matching website.
- The page bridge is injected on demand after a user starts capture, opens a
  page tool, or uses the capture shortcut. Once injected, it remains idle
  between explicit commands and is removed by the browser when the page unloads.
- Captures are processed in the page and extension contexts. Generated exports
  are downloaded locally.
- The extension does not automatically click, type, submit forms, or navigate
  to unknown pages.

Workspace metadata and bounded artifacts are stored in the extension's local
IndexedDB or `browser.storage.local`. Users can delete workspace records from
the Side Panel or clear all extension data through the browser.

## Data In Captures

A reference capture can include design tokens, layout metrics, component
summaries, visible text excerpts, resource clues, interaction samples, motion
timing, and evidence metadata.

For a page the user explicitly captures, workspace history can store the page
URL, page title, and capture time so the user can identify routes, reopen local
evidence, and name exported files. Yotsuba Lens does not build a background
record of unrelated browsing activity.

An authorized Rebuild capture can additionally include screenshots, masked
rrweb events, and, in the Collector build, sanitized DOMSnapshot, matched CSS,
geometry, viewport, animation, and optionally bounded Canvas evidence. Input
values are masked and DOMSnapshot form-value fields are sanitized, but captures
can still contain visible page content. Treat exported packs as potentially
sensitive files.

Yotsuba Lens is not designed to read cookies, local-storage values, credentials,
request headers, or request bodies. Cross-origin iframe internals and unreadable
or oversized visual surfaces remain explicit gaps.

## Optional AI Generation

AI generation is opt-in. It is not called unless the user configures an
OpenAI-compatible provider and requests AI output.

Before a request, Yotsuba Lens builds a reduced evidence payload. It is designed
to exclude raw DOM, full DOM trees, cookies, browser storage, credentials,
tracking identifiers, screenshots, and unmasked input values. The selected
provider still receives the reduced design evidence and the user's build brief;
its own privacy policy applies.

Provider base URL, model, endpoint mode, and API key are saved only when the
user chooses to save them. Profiles are stored in `browser.storage.local` on
the user's machine and are not encrypted by Yotsuba Lens. Profiles can be
cleared from the AI settings UI. Without a configured key, users can export an
evidence-only pack. For Chrome Web Store disclosure, the optional provider API
key is classified as authentication information. It is sent only to the
provider selected by the user as an authorization credential for an explicit AI
request.

## Chrome Web Store Limited Use

Yotsuba Lens uses captured website content and observed interaction evidence
only to perform the capture, analysis, storage, export, or optional AI request
that the user explicitly starts. The developer does not receive, sell, share,
or use captured data for advertising, credit decisions, or unrelated product
analytics. The developer does not allow humans to read captured data unless a
user intentionally includes it in a support or security report.

Without optional AI generation, captured content stays in the browser profile
or in files the user exports. When the user configures a compatible AI provider
and explicitly requests generation, only the reduced payload described above
is sent to that provider. Yotsuba Lens does not transfer captured data to any
other third party and does not use it for purposes unrelated to the extension's
single purpose.

## Permissions

| Permission | Why it is requested |
| --- | --- |
| `activeTab` | Temporarily access the page after the user clicks the extension action, starts Smart Capture, or selects a component. |
| `scripting` | Inject only the local, packaged page bridge after a user action; no remote code is injected or executed. |
| `storage` | Store locale, theme, workspace metadata, bounded capture history, and optional AI provider settings locally. |
| `tabs` | Identify the active tab, read its URL and title, refresh the Side Panel after tab changes, exchange capture messages, and capture the current visible area. |
| `sidePanel` | Keep capture controls, progress, evidence coverage, history, and settings visible without navigating away from the inspected page. |
| `<all_urls>` | Let users initiate capture on an HTTP or HTTPS website they are authorized to inspect. This host permission does not cause automatic capture or automatic page injection. |

The separately built Collector adds Chrome's `debugger` permission. It is used
only after explicit Rebuild authorization for bounded DOMSnapshot, CSS,
geometry, viewport, and animation evidence. The standard release is validated
to exclude this permission. Collector sessions detach and restore viewport,
scroll, animation, forced pseudo-state, capture UI, and privacy-mask state on
success, stop, timeout, and handled failure paths.

## User Responsibility

Use Yotsuba Lens only where you have permission to inspect and reuse the
resulting evidence. Do not use it to republish proprietary source code, private
content, credentials, trademarks, brand assets, fonts, images, or video without
the required rights.

Report a privacy or security vulnerability through
[GitHub Private Vulnerability Reporting](https://github.com/isla4ever/yotsuba-lens/security/advisories/new).

# Chrome Web Store Submission - Design Lens 0.3.0

This document is the source of truth for the public standard build. Do not
upload the Collector package to Chrome Web Store because it intentionally adds
the `debugger` permission for separately authorized development use.

## Listing

| Field | English | Chinese |
| --- | --- | --- |
| Name | Design Lens | Design Lens 网页设计采集器 |
| Summary | Capture structured design evidence, interaction states, and explicit gaps for reference or authorized rebuild workflows. | 采集网页设计证据、交互状态与缺口，用于设计参照或经授权的重建流程。 |
| Category | Developer Tools | 开发者工具 |
| Language | English | 中文（简体） |

### Detailed Description - English

Design Lens turns a user-initiated inspection of the current page into
structured design evidence. Choose Reference to extract transferable layout,
style, component, interaction, and motion patterns for an original design, or
choose Rebuild for a bounded implementation draft when you are authorized to
reconstruct the page.

Smart Capture collects a baseline in one action and degrades safely on large or
continuously changing pages. The Side Panel reports what was observed, what is
missing, and at most three useful follow-up tasks. It can export an evidence
pack without an account or AI configuration. Optional AI generation runs only
after you configure a compatible provider and request it.

Design Lens does not download website source code, run automatically on every
page, click or submit forms for you, or claim fidelity for uncaptured states.
All standard capture and export work is local by default.

### Detailed Description - Chinese

Design Lens 将用户主动发起的当前页面检查整理为结构化设计证据。选择“设计参照”，可提取可迁移的布局、样式、组件、交互和动效规律，用于原创设计；在已获得授权时，可选择“重建”生成边界明确、可验证的实现草案。

智能捕获只需一次操作，并会在超大或持续变化的页面上自动降级，避免影响页面使用。侧边栏会明确显示已观察证据、缺失状态以及最多三个必要的补充任务。无需账号或 AI 配置即可导出证据包；只有用户配置兼容的 AI 服务并主动请求时，才会发送精简后的证据。

Design Lens 不下载网站源代码，不会在所有页面自动运行，不会代替用户点击或提交表单，也不会把未捕获状态描述为高还原结果。标准版默认在本地完成采集、存储与导出。

## Single Purpose

Capture and organize user-requested design evidence from the active web page so
the user can create an original reference-based design or an explicitly
authorized, evidence-bounded rebuild draft.

## Permission Justifications

| Permission | Reviewer justification |
| --- | --- |
| `activeTab` | Accesses only the tab the user is actively inspecting after the user starts Smart Capture, component selection, manual capture, or the shortcut. |
| `scripting` | Injects the bundled page bridge on demand to inspect the active page. The standard build has no persistent content script. |
| `storage` | Stores locale, theme, workspace history, capture metadata, optional AI provider settings, and bounded local artifacts in the browser profile. |
| `tabs` | Finds the active tab and associates user-requested capture results with the correct Side Panel workspace. |
| `sidePanel` | Provides the extension's default persistent workspace for capture status, history, evidence gaps, exports, and settings. |
| `<all_urls>` | Lets the user initiate capture on websites they choose. It does not inject code or collect data until the user invokes a capture action. |

## Remote Code

**No.** All executable JavaScript and WebAssembly used by the extension is
packaged in the submitted ZIP. Optional AI requests exchange data with the
provider configured by the user; responses are treated as content and are not
executed as remote code.

## Data Use And Limited Use

Declare these data types:

- **Website content**: visible text excerpts, design tokens, layout metrics,
  screenshots, and sanitized evidence from pages the user explicitly captures.
- **User activity**: bounded hover, focus, scroll, open, and timing evidence
  observed only during a user-started capture session.

The data is used only for the extension's single purpose. It is not sold, used
for advertising or credit decisions, or transferred for unrelated purposes.
The developer does not receive captured data. Optional AI transfer occurs only
when the user configures a provider and explicitly requests generation.

Check all Chrome Web Store Limited Use attestations that match the statements
above. Privacy policy:

https://github.com/isla4ever/design-lens/blob/main/docs/privacy.md

## Reviewer Test Instructions

1. Install the submitted standard ZIP. No account is required.
2. Open a normal public `https` page and click the Design Lens toolbar icon.
   The Side Panel should open by default.
3. Keep **Reference** selected and choose **Smart Capture**. The page bridge is
   injected only now; the result appears in the Side Panel.
4. Open **Coverage** and **History** to inspect the evidence and readiness state.
5. Export the evidence pack. This path does not require an AI key.
6. Optional: choose **Rebuild**, confirm authorization, and run Smart Capture to
   see the stricter screenshot/state coverage and explicit missing evidence.

Expected behavior: the extension does not navigate, submit forms, or perform
synthetic clicks. Unsupported browser pages such as `chrome://` are rejected.

## URLs And Distribution

- Homepage: https://github.com/isla4ever/design-lens
- Support: https://github.com/isla4ever/design-lens/issues
- Privacy policy: https://github.com/isla4ever/design-lens/blob/main/docs/privacy.md
- Distribution: Public, all supported Chrome Web Store regions
- Publishing: Deferred publishing after review approval

## Assets

- Store icon: `docs/store-assets/icon-128.png`
- Screenshot 1: `docs/store-assets/screenshot-evidence-workspace-1280x800.png`
- Screenshot 2: `docs/store-assets/screenshot-smart-capture-1280x800.png`
- Small promo tile: `docs/store-assets/promo-small-440x280.png`

Only upload `dist/design-lens-0.3.0-standard-chrome.zip`. Keep the Collector ZIP
as a local, explicitly authorized development build; do not submit it to Chrome
Web Store or publish it as the public extension package.

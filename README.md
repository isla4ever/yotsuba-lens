<p align="center">
  <img src="docs/store-assets/icon-128.png" alt="Yotsuba 网页风格提取器图标" width="128" height="128" />
</p>

<h1 align="center">Yotsuba 网页风格提取器</h1>
<p align="center"><strong>把网页的配色、布局、组件、交互和动效，整理成可直接使用的 Prompt 与设计参考。</strong></p>

<p align="center">
  <a href="https://chromewebstore.google.com/detail/yotsuba-lens-%E7%BD%91%E9%A1%B5%E8%AE%BE%E8%AE%A1%E8%AF%81%E6%8D%AE%E9%87%87%E9%9B%86/imbmglmdajepbagbflgalkfokofcilag"><img src="https://img.shields.io/badge/Chrome-%E7%AB%8B%E5%8D%B3%E5%AE%89%E8%A3%85-4285F4?logo=googlechrome&logoColor=white" alt="从 Chrome 应用商店安装" /></a>
  <a href="https://github.com/isla4ever/yotsuba-lens/actions/workflows/ci.yml"><img src="https://github.com/isla4ever/yotsuba-lens/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <img src="https://img.shields.io/badge/version-0.3.1-2563eb" alt="Version 0.3.1" />
  <img src="https://img.shields.io/badge/Chrome-MV3-4285f4" alt="Chrome MV3" />
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-16a34a" alt="MIT License" /></a>
</p>

<p align="center"><strong>中文</strong> · <a href="README.en.md">English</a></p>

<p align="center">
  <a href="https://chromewebstore.google.com/detail/yotsuba-lens-%E7%BD%91%E9%A1%B5%E8%AE%BE%E8%AE%A1%E8%AF%81%E6%8D%AE%E9%87%87%E9%9B%86/imbmglmdajepbagbflgalkfokofcilag">
    <img src="docs/readme-assets/readme-hero.jpg" alt="Yotsuba 提取网页风格并生成可用 Prompt" width="100%" />
  </a>
</p>

看到喜欢的网页，却很难把它的设计语言准确描述给 AI 编码工具？Yotsuba 会读取当前页面中真实存在的视觉与交互特征，整理出结构清晰的 Prompt、设计参考和检查依据，减少“做得像一点”带来的反复沟通。

> [!IMPORTANT]
> Chrome 应用商店已发布 `0.3.0`；名称和说明更清晰的 `0.3.1` 已提交审核，预计近日上线。商店审核通过后，已安装用户会自动收到更新。请只分析、参考或还原你有权使用的页面。

## 立即开始

### 1. 安装扩展

[**从 Chrome 应用商店安装 Yotsuba**](https://chromewebstore.google.com/detail/yotsuba-lens-%E7%BD%91%E9%A1%B5%E8%AE%BE%E8%AE%A1%E8%AF%81%E6%8D%AE%E9%87%87%E9%9B%86/imbmglmdajepbagbflgalkfokofcilag)

无需下载源码，也无需安装 Node.js。安装后建议将扩展固定在 Chrome 工具栏。

### 2. 打开目标网页

进入一个普通的 `http` 或 `https` 页面，点击扩展图标。Yotsuba 默认在浏览器侧边栏打开，不会遮住正在参考的网页。

### 3. 智能捕获并生成结果

点击 **智能捕获**，查看提取到的风格和待补充状态，再生成 Prompt 或导出参考资料。仅提取页面信息无需配置模型；需要 AI 整理时，按照首次使用指引填写自己的兼容模型配置即可。

```text
打开网页 → 智能捕获 → 检查结果 → 生成 Prompt / 导出参考资料
```

## 你能得到什么

| 使用场景 | Yotsuba 提取什么 | 最终结果 |
| --- | --- | --- |
| **给 AI 描述网页风格** | 配色、字体、间距、圆角、阴影、布局和组件规律 | 可直接交给 AI 编码工具的结构化 Prompt |
| **参考优秀网页做新设计** | 可复用的视觉语言、组件样式、交互和动效线索 | 不包含原站品牌和内容的设计参考 |
| **还原已获授权的页面** | 关键截图、尺寸、页面状态和验证要求 | 范围明确、可以继续补充和检查的重建资料 |
| **补齐隐藏状态** | 悬停、聚焦、展开、滚动和响应式缺口 | 最多 3 个必要补采任务，无需录制整段操作 |

## 侧边栏工作区

<p align="center">
  <img src="docs/readme-assets/workspace-showcase.jpg" alt="Yotsuba 在真实网页旁显示捕获结果与设置" width="100%" />
</p>

概览、覆盖、历史和设置集中在同一侧边栏中。快速弹窗只保留高频操作；捕获结束后可以立即查看已识别内容、缺失状态和下一步建议。

<details>
  <summary><strong>查看历史记录与删除确认</strong></summary>
  <br />
  <p align="center">
    <img src="docs/store-assets/screenshot-history-dark-1280x800.png" alt="Yotsuba 历史记录与删除二次确认" width="960" />
  </p>
</details>

## 两种使用方式

| 模式 | 适合什么情况 | 输出边界 |
| --- | --- | --- |
| **设计参照（Reference）** | 借鉴网页的配色、布局、组件、动效或交互，完成自己的原创页面 | 提炼可迁移的设计规律，不复制原站品牌、文案和素材 |
| **授权还原（Rebuild）** | 在明确授权范围内，还原指定页面、尺寸和交互状态 | 只对已经捕获的内容负责，未捕获状态会标记为待补充 |

<p align="center">
  <img src="docs/readme-assets/evidence-flow.jpg" alt="Yotsuba 将网页特征整理成 Prompt 与参考资料" width="100%" />
</p>

生成内容以实际捕获结果为依据。没有采集到的交互或响应式状态会明确标记，不会被包装成“完整复刻”。

## 隐私与安全

- 页面分析与资料导出默认在本地完成。
- 扩展只在用户主动点击捕获后读取当前页面，不会在后台自动扫描所有网站。
- 只有配置模型并主动生成 AI 内容时，才会向所选模型服务发送压缩后的必要信息。
- AI 请求不会包含 Cookie、本地存储、账号凭证、原始 DOM、截图或未脱敏的输入内容。
- Chrome 商店标准版不申请 `debugger` 权限。

权限用途和数据边界详见 [隐私与权限说明](docs/privacy.md)。

## 开源与高级用法

<details>
  <summary><strong>从源码安装标准版</strong></summary>
  <br />

环境要求：Node.js `>=22.13.0`、npm `>=10`、Chrome 或其他 Chromium 浏览器。

```bash
npm ci
npm run build
```

打开 `chrome://extensions`，开启 **开发者模式**，点击 **加载已解压的扩展程序**，选择 `<project-root>/.output/chrome-mv3`。
</details>

<details>
  <summary><strong>Collector 深度采集版</strong></summary>
  <br />

```bash
npm run build:collector
```

加载 `<project-root>/.output/collector/chrome-mv3`。Collector 仅用于经授权的深度采集，会额外申请 `debugger` 权限，以获取受预算限制的 DOMSnapshot、匹配样式、几何、视口与动画证据。它不会随 Chrome 商店标准版发布。
</details>

<details>
  <summary><strong>导出资料与候选页面验证</strong></summary>
  <br />

Yotsuba 可导出三类资料：

| 资料 | 适合用途 |
| --- | --- |
| **设计证据包** | 保存、分享或交给任意 AI 工具继续分析 |
| **AI Prompt 包** | 为目标项目生成可直接执行的编码要求和实现说明 |
| **Rebuild 草稿包** | 保存授权还原基线、页面状态、明确缺口和验证规则 |

验证授权还原的候选页面：

```bash
npm run verify:rebuild -- \
  --pack <rebuild-pack.zip> \
  --url http://localhost:3000
```

验证器只检查资料包中已有证据的页面与状态，不推测未捕获行为。真实案例见 [AstroWind 自动重建实战](docs/astrowind-rebuild-benchmark.md) 和 [Bilibili 首页智能捕获与重建实战](docs/bilibili-rebuild-benchmark.md)。
</details>

## 开发

```bash
npm run dev                 # 标准版开发服务器
npm run dev:collector       # Collector 开发服务器
npm run check:all           # 类型检查、测试与两种生产构建
npm run check:browser       # MV3 注入、UI 溢出、大型 DOM 性能与恢复检查
npm run package:store       # 生成并校验 Chrome 商店候选包
```

主要文档：

- [架构说明](docs/architecture.md)
- [隐私与权限](docs/privacy.md)
- [验证记录](docs/validation.md)
- [变更记录](CHANGELOG.md)
- [参与贡献](CONTRIBUTING.md)
- [安全策略](SECURITY.md)
- [发布检查清单](docs/release-checklist.md)

提交较大功能前请先创建 Issue。安全问题请通过 [GitHub Private Vulnerability Reporting](https://github.com/isla4ever/yotsuba-lens/security/advisories/new) 私下报告。

## License

[MIT](LICENSE) © Isla

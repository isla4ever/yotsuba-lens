export function buildExtensionManifest(mode: string) {
  const isCollector = mode === "collector";
  return {
    name: isCollector ? "Yotsuba Lens Collector" : "Yotsuba 网页风格提取器",
    description: isCollector
      ? "Capture authorized rebuild evidence with optional Chrome DevTools Protocol inspection."
      : "提取当前网页的配色、布局、组件、交互和动效，生成可直接使用的 Prompt，帮助你参考或还原网页风格。",
    version: "0.3.1",
    icons: {
      16: "icon/16.png",
      32: "icon/32.png",
      48: "icon/48.png",
      128: "icon/128.png"
    },
    permissions: ["activeTab", "scripting", "storage", "tabs", "sidePanel", ...(isCollector ? ["debugger"] : [])],
    host_permissions: ["<all_urls>"],
    action: {
      default_title: isCollector ? "Open Yotsuba Lens Collector" : "打开 Yotsuba 网页风格提取器",
      default_icon: {
        16: "icon/16.png",
        32: "icon/32.png"
      }
    },
    side_panel: {
      default_path: "sidepanel.html"
    },
    commands: {
      "capture-selection": {
        suggested_key: {
          default: "Alt+Shift+D",
          mac: "Alt+Shift+D"
        },
        description: "提取所选区域的网页风格"
      }
    }
  };
}

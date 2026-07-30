export function buildExtensionManifest(mode: string) {
  const isCollector = mode === "collector";
  return {
    name: isCollector ? "Design Lens Collector" : "Design Lens 设计证据采集",
    description: isCollector
      ? "Capture authorized rebuild evidence with optional Chrome DevTools Protocol inspection."
      : "采集网页设计证据、交互状态与缺口，支持设计参照与经授权重建。",
    version: "0.3.0",
    icons: {
      16: "icon/16.png",
      32: "icon/32.png",
      48: "icon/48.png",
      128: "icon/128.png"
    },
    permissions: ["activeTab", "scripting", "storage", "tabs", "sidePanel", ...(isCollector ? ["debugger"] : [])],
    host_permissions: ["<all_urls>"],
    action: {
      default_title: isCollector ? "Open Design Lens Collector" : "打开 Design Lens 设计证据采集",
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
        description: "Capture the selected element with Design Lens"
      }
    }
  };
}

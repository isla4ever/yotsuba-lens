from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "store-assets"
SOURCE = ROOT / "docs" / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

BG = "#f5f6f0"
INK = "#111812"
MUTED = "#4f5a51"
LIME = "#84ad13"
LIME_DARK = "#5f7f08"
DARK = "#101712"
LIGHT = "#f5f3e9"


def font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc" if bold else "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default()


def fit_text(draw, text, max_width, size, bold=False):
    f = font(size, bold)
    lines, current = [], ""
    for char in text:
        candidate = current + char
        if draw.textbbox((0, 0), candidate, font=f)[2] <= max_width or not current:
            current = candidate
        else:
            lines.append(current)
            current = char
    if current:
        lines.append(current)
    return lines, f


def draw_mark(draw, xy, size, background=LIME):
    x, y = xy
    draw.rounded_rectangle((x, y, x + size, y + size), radius=size // 5, fill=background)
    f = font(round(size * 0.48), True)
    bbox = draw.textbbox((0, 0), "D", font=f)
    draw.text((x + (size - bbox[2]) / 2, y + (size - (bbox[3] - bbox[1])) / 2 - bbox[1]), "D", fill=INK, font=f)


def draw_brand(draw, x, y, size=48, dark=False):
    draw_mark(draw, (x, y), size, "#c8ff56" if dark else LIME)
    f = font(round(size * 0.46), True)
    draw.text((x + size + 14, y + size * 0.18), "Design Lens", fill=LIGHT if dark else INK, font=f)


def paste_panel(canvas, path, box):
    panel = Image.open(path).convert("RGB")
    panel.thumbnail((box[2] - box[0], box[3] - box[1]), Image.Resampling.LANCZOS)
    x = box[0] + ((box[2] - box[0]) - panel.width) // 2
    y = box[1] + ((box[3] - box[1]) - panel.height) // 2
    canvas.paste(panel, (x, y))
    return (x, y, panel.width, panel.height)


def make_icon():
    source = Image.open(ASSETS / "icon-128.png").convert("RGBA")
    base = Image.new("RGB", source.size, BG)
    base.paste(source, mask=source.getchannel("A"))
    base.save(ASSETS / "icon-128.png", format="PNG", optimize=True)


def make_small_promo():
    image = Image.new("RGB", (440, 280), BG)
    draw = ImageDraw.Draw(image)
    draw.rectangle((420, 0, 440, 280), fill=LIME)
    draw_brand(draw, 30, 30, 58)
    lines, f = fit_text(draw, "让 AI 先看懂设计", 330, 34, True)
    y = 135
    for line in lines:
        draw.text((30, y), line, fill=INK, font=f)
        y += 38
    draw.ellipse((318, 158, 388, 228), outline=INK, width=12)
    draw.line((375, 215, 408, 248), fill=INK, width=12)
    image.save(ASSETS / "promo-small-440x280.png", format="PNG", optimize=True)


def make_top_promo():
    image = Image.new("RGB", (1400, 560), DARK)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 18, 560), fill="#c8ff56")
    draw_brand(draw, 64, 48, 54, dark=True)
    draw.text((64, 180), "网页设计证据采集器", fill="#c8ff56", font=font(25, True))
    lines, f = fit_text(draw, "捕获结构、状态与动效\n让 AI 编码更有依据", 560, 52, True)
    y = 230
    for line in lines:
        draw.text((64, y), line, fill=LIGHT, font=f)
        y += 64
    draw.text((64, 390), "设计参照 · 经授权重建 · 智能捕获 · 缺口提示", fill="#b8c1b9", font=font(22))
    panel = Image.open(SOURCE / "design-lens-sidepanel-coverage.png").convert("RGB")
    panel.thumbnail((700, 410), Image.Resampling.LANCZOS)
    frame = (650, 92, 1340, 468)
    draw.rounded_rectangle(frame, radius=12, fill="#e9ece4", outline="#cdd2c9", width=2)
    x = frame[0] + (frame[2] - frame[0] - panel.width) // 2
    y = frame[1] + (frame[3] - frame[1] - panel.height) // 2
    draw.rounded_rectangle((x - 2, y - 2, x + panel.width + 2, y + panel.height + 2), radius=8, fill="#ffffff")
    image.paste(panel, (x, y))
    image.save(ASSETS / "promo-top-1400x560.png", format="PNG", optimize=True)


def normalize_screenshots():
    for name in ["screenshot-evidence-workspace-1280x800.png", "screenshot-smart-capture-1280x800.png"]:
        path = ASSETS / name
        Image.open(path).convert("RGB").save(path, format="PNG", optimize=True)


def add_paragraph(doc, text="", bold=False, color=None, size=11, after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(after)
    r = p.add_run(text)
    r.bold = bold
    set_docx_font(r)
    r.font.size = Pt(size)
    if color:
        r.font.color.rgb = RGBColor.from_string(color)
    return p


def set_docx_font(run):
    # Keep the East Asian family explicit so Word and macOS Preview select a
    # Chinese-capable face instead of inheriting the Latin body font.
    family = "Heiti SC"
    run.font.name = family
    run._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:ascii"), family)
    run._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:hAnsi"), family)
    run._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), family)
    run._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:cs"), family)


def add_field(doc, label, value, note=""):
    add_paragraph(doc, label, bold=True, color="5F7F08", size=11, after=2)
    add_paragraph(doc, value, size=11, after=2)
    if note:
        add_paragraph(doc, "后台提示：" + note, color="555555", size=9, after=8)


def make_docx():
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.85)
    section.right_margin = Inches(0.85)
    title = doc.add_paragraph()
    title.paragraph_format.space_after = Pt(4)
    run = title.add_run("Design Lens Chrome Web Store 中文上架填写包")
    set_docx_font(run)
    run.font.size = Pt(24)
    run.bold = True
    run.font.color.rgb = RGBColor(17, 24, 18)
    add_paragraph(doc, "版本：0.3.0　｜　仅上传标准版　｜　发布范围：公开　｜　审核通过后暂存", color="5F7F08", size=10, after=14)
    add_paragraph(doc, "使用说明", bold=True, color="111812", size=15, after=6)
    add_paragraph(doc, "按 Chrome Web Store 开发者后台从上到下填写。文字字段可直接复制；图片文件位于项目 docs/store-assets/ 目录。首次提交建议关闭自动发布，审核通过后再手动公开。", size=10, after=12)

    add_paragraph(doc, "一、商品详情", bold=True, color="111812", size=15, after=8)
    add_field(doc, "软件包中的标题", "Design Lens 设计证据采集", "保持与新标准版扩展包 manifest 中的名称一致。")
    add_field(doc, "软件包中的摘要", "采集网页设计证据、交互状态与缺口，支持设计参照与经授权重建。", "上传新的标准版 ZIP 后由软件包自动带入。")
    add_field(doc, "说明", "Design Lens 是一款面向设计师、产品经理和开发者的网页设计证据采集工具。用户主动发起智能捕获后，它会整理当前页面的布局结构、设计令牌、组件模式、交互状态、截图、动效线索和证据缺口。\n\n你可以选择“设计参照”，提取可迁移的视觉和交互规律，用于原创设计；也可以在已获得授权时选择“经授权重建”，生成有边界、可验证的实现草案。侧边栏会清楚展示已捕获证据、缺失状态和下一步补充任务。\n\n智能捕获只需一次操作，并会在超大或持续变化的页面上自动降级，避免页面卡顿。采集、存储和导出默认在本地完成，无需账号或 AI 配置即可导出证据包。只有用户主动配置兼容的 AI 服务并请求生成时，才会发送精简后的结构化证据。\n\nDesign Lens 不会自动运行在所有网页上，不会自动点击、输入、提交表单或跳转页面，也不会把未采集的状态描述为完整复刻结果。请仅在你有权查看和使用相关页面证据时进行采集。", "完整粘贴到说明文本框。")
    add_field(doc, "类别", "开发者工具", "选择 Developer Tools / 开发者工具。")
    add_field(doc, "语言", "中文（简体）", "选择 Chinese (Simplified) / 中文（简体）。")

    add_paragraph(doc, "二、图片资源", bold=True, color="111812", size=15, after=8)
    add_field(doc, "商店图标", "docs/store-assets/icon-128.png", "128×128，24 位 PNG，无透明层。")
    add_field(doc, "屏幕截图 1", "docs/store-assets/screenshot-evidence-workspace-1280x800.png", "1280×800，24 位 PNG，无透明层。")
    add_field(doc, "屏幕截图 2", "docs/store-assets/screenshot-smart-capture-1280x800.png", "1280×800，24 位 PNG，无透明层。")
    add_field(doc, "小型宣传图块", "docs/store-assets/promo-small-440x280.png", "440×280，24 位 PNG，无透明层。")
    add_field(doc, "顶部宣传图块", "docs/store-assets/promo-top-1400x560.png", "1400×560，24 位 PNG，无透明层。")
    add_field(doc, "宣传视频", "留空", "项目当前没有公开视频，不要填写无关链接。")

    add_paragraph(doc, "三、其他字段", bold=True, color="111812", size=15, after=8)
    add_field(doc, "官方网站", "https://github.com/isla4ever/design-lens", "选择 GitHub 项目主页。")
    add_field(doc, "主页网址", "https://github.com/isla4ever/design-lens", "如果后台把官方网站与主页分开，两个字段都填项目主页。")
    add_field(doc, "支持信息页面网址", "https://github.com/isla4ever/design-lens/issues", "用于接收问题反馈和使用支持。")
    add_field(doc, "成人内容", "否 / 关闭", "Design Lens 不包含成人内容。")
    add_field(doc, "商品支持", "公开范围 / 开启", "允许用户从商店详情页进入支持入口；支持地址使用 GitHub Issues。")

    add_paragraph(doc, "截图对应的填写顺序", bold=True, color="111812", size=15, after=8)
    for item in [
        "软件包中的标题：保留 Design Lens。",
        "软件包中的摘要：保留上传 ZIP 带入的摘要，或粘贴上方中文摘要。",
        "说明：粘贴上方完整中文说明。",
        "类别：选择开发者工具。语言：选择中文（简体）。",
        "商店图标：上传 icon-128.png。宣传视频：留空。",
        "屏幕截图：建议上传两张 1280×800 截图，最多不要超过 5 张。",
        "小型宣传图块：上传 promo-small-440x280.png；顶部宣传图块：上传 promo-top-1400x560.png。",
        "官方网站、主页网址、支持信息页面网址：按上方地址填写；成人内容关闭；商品支持选择公开范围并开启。",
    ]:
        p = doc.add_paragraph(style="List Number")
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(item)
        set_docx_font(r)
        r.font.size = Pt(10)

    add_paragraph(doc, "四、隐私权与审核", bold=True, color="111812", size=15, after=8)
    add_field(doc, "隐私权政策网址", "https://github.com/isla4ever/design-lens/blob/main/docs/privacy.md", "必须使用可公开访问的 HTTPS 地址。")
    add_field(doc, "单一用途", "采集并整理用户主动发起的网页设计证据，用于设计参照或经授权的重建草案。", "按后台提示填写单一用途。")
    add_field(doc, "远程代码", "否", "所有 JavaScript 和 WebAssembly 都随扩展包发布，不执行远程返回的代码。")
    add_field(doc, "数据使用", "网站内容：可见文本片段、设计令牌、布局指标、截图和脱敏后的证据。用户活动：仅在用户主动发起的采集会话中观察到的悬停、聚焦、滚动、打开和时间证据。数据仅用于采集、分析、存储、导出和用户主动请求的 AI 生成，不出售、不用于广告、不用于信用评估，也不用于无关用途。", "与 docs/privacy.md 保持一致，并勾选 Limited Use 声明。")
    add_field(doc, "审核测试说明", "1. 安装标准版扩展，不需要账号。\n2. 打开普通公开 HTTPS 网页，点击工具栏中的 Design Lens，侧边栏应默认打开。\n3. 保持“设计参照”模式，点击“智能捕获”，等待结果出现在侧边栏。\n4. 打开“覆盖”和“历史”查看证据状态。\n5. 导出证据包；此流程不需要 AI 密钥。\n6. 仅在获得授权时选择“经授权重建”，确认授权后再测试重建证据。\n扩展不会自动导航、提交表单或执行合成点击；chrome:// 等受限页面会被拒绝。", "完整粘贴到审核测试说明。")

    add_paragraph(doc, "五、提交前检查", bold=True, color="111812", size=15, after=8)
    for item in [
        "只上传 dist/design-lens-0.3.0-standard-chrome.zip，不上传 Collector 版本。",
        "分发范围选择公开，地区选择所有地区。",
        "审核通过后关闭自动发布或选择暂存发布。",
        "确认图标、截图、小型宣传图块和顶部宣传图块均已上传。",
        "确认隐私权政策、支持网址和说明文字均可公开访问。",
        "确认交易者身份按实际情况填写；当前个人免费开源项目通常为非交易者。",
    ]:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(item)
        set_docx_font(r)
        r.font.size = Pt(10)
    out = ROOT / "docs" / "chrome-web-store-cn-fill-pack.docx"
    doc.save(out)
    return out


make_icon()
make_small_promo()
make_top_promo()
normalize_screenshots()
make_docx()
print("Generated Chrome Web Store assets and Chinese fill pack")

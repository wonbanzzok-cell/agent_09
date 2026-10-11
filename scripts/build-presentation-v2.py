"""Build AI_발전_발표자료_v2.pptx. Usage: python build-presentation-v2.py <output.pptx>

Content comes from research/ai-development-research-v2.md.
Design follows references/ppt/slide-design-system.md.
"""

import sys
import unicodedata

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.oxml.xmlchemy import OxmlElement
from pptx.util import Inches, Pt

# Fonts: each Pretendard weight is its own family name in PowerPoint.
FONT = "Pretendard"
FONT_LIGHT = "Pretendard Light"
FONT_SEMIBOLD = "Pretendard SemiBold"

# Palette from the design system. No other colors are used.
BG = RGBColor(0xEE, 0xEE, 0xEE)
PRIMARY = RGBColor(0x11, 0x11, 0x11)
SECONDARY = RGBColor(0x33, 0x33, 0x33)
MUTED = RGBColor(0x77, 0x77, 0x77)
LINE = RGBColor(0xBD, 0xBD, 0xBD)
ACCENT = RGBColor(0x6F, 0x8F, 0xB5)

# Canvas, in inches.
SLIDE_W, SLIDE_H = 13.333, 7.5
LEFT, RIGHT = 1.0, SLIDE_W - 1.0
TOP, BOTTOM = 0.9, SLIDE_H - 0.9
TEXT_W = 5.4                      # text column: x 1.0-6.4
IMG_X = 7.3                       # image column starts after a 0.9 in gutter
IMG_W = RIGHT - IMG_X
FULL_W = RIGHT - LEFT
BLANK = 6  # index of the blank layout in the default template

SOURCE_NOTE = "출처: research/ai-development-research-v2.md"


class Canvas:
    """One slide plus a record of what was placed on it, for the layout check."""

    def __init__(self, prs, name):
        self.name = name
        self.slide = prs.slides.add_slide(prs.slide_layouts[BLANK])
        fill = self.slide.background.fill
        fill.solid()
        fill.fore_color.rgb = BG
        self.boxes = []  # (label, x, y, w, h)

    def record(self, label, x, y, w, h):
        self.boxes.append((label, x, y, w, h))

    def notes(self, text):
        self.slide.notes_slide.notes_text_frame.text = text


def set_font_name(run, name):
    """Set the Latin, East Asian, and complex-script typefaces of a run.

    font.name writes only <a:latin>, so Korean text would fall back to the
    theme font without the <a:ea> element.
    """
    run.font.name = name
    rPr = run._r.get_or_add_rPr()
    anchor = rPr.find(qn("a:latin"))
    for tag in ("a:ea", "a:cs"):
        el = rPr.find(qn(tag))
        if el is None:
            el = OxmlElement(tag)
            anchor.addnext(el)  # schema order is latin, ea, cs
        el.set("typeface", name)
        anchor = el


def text_width(text, size):
    """Estimate the rendered width of one line in inches. Errs on the wide side."""
    ems = 0.0
    for ch in text:
        if ch == " ":
            ems += 0.3
        elif unicodedata.east_asian_width(ch) in ("W", "F"):
            ems += 1.0
        else:
            ems += 0.62
    return ems * size / 72


def line_count(text, size, width):
    """Estimate how many lines the text wraps to in a box of the given width."""
    lines, current = 1, 0.0
    for word in text.split(" "):
        w = text_width(word, size)
        gap = text_width(" ", size) if current else 0.0
        if current and current + gap + w > width:
            lines += 1
            current = w
        else:
            current += gap + w
    return lines


def add_text(cv, x, y, w, h, text, size, font=FONT, bold=False, color=MUTED,
             spacing=1.0, anchor=MSO_ANCHOR.TOP):
    """Add a left-aligned text box. Pass a list of strings for one paragraph per item.

    PowerPoint breaks Korean lines in the middle of a word, so text longer than
    one line is passed as a list that already holds one line per item.

    Fails the build when the text is estimated not to fit the box, because
    python-pptx does not measure text and PowerPoint would let it spill out.
    """
    paragraphs = text if isinstance(text, list) else [text]
    lines = sum(line_count(p, size, w) for p in paragraphs)
    needed = lines * size * spacing * 1.2 / 72
    if needed > h + 0.01:
        raise ValueError(f"{cv.name}: text needs {needed:.2f} in but the box is {h:.2f} in: {paragraphs[0]!r}")

    box = cv.slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    frame = box.text_frame
    frame.word_wrap = True
    frame.vertical_anchor = anchor
    frame.margin_left = frame.margin_right = frame.margin_top = frame.margin_bottom = 0
    for i, line in enumerate(paragraphs):
        para = frame.paragraphs[0] if i == 0 else frame.add_paragraph()
        para.alignment = PP_ALIGN.LEFT
        para.line_spacing = spacing
        run = para.add_run()
        run.text = line
        set_font_name(run, font)
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.color.rgb = color
    cv.record(paragraphs[0][:20], x, y, w, h)
    return box


def add_rect(cv, x, y, w, h, color, label="rect"):
    """Add a sharp-cornered rectangle with no border or shadow."""
    rect = cv.slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    rect.fill.solid()
    rect.fill.fore_color.rgb = color
    rect.line.fill.background()
    rect.shadow.inherit = False
    cv.record(label, x, y, w, h)
    return rect


def add_divider(cv, x, y, length):
    """Add a 0.75 pt horizontal divider line."""
    line = cv.slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x), Inches(y),
                                         Inches(x + length), Inches(y))
    line.line.color.rgb = LINE
    line.line.width = Pt(0.75)
    line._element.spPr.append(OxmlElement("a:effectLst"))  # drop the theme shadow
    cv.record("divider", x, y, length, 0)
    return line


def add_quote_line(cv, y, label):
    """Quote mark, thin line, then a short label."""
    add_text(cv, LEFT, y, 0.3, 0.42, "“", 24, bold=True, color=PRIMARY)
    add_divider(cv, LEFT + 0.4, y + 0.17, 2.4)
    add_text(cv, LEFT + 2.95, y + 0.05, 2.4, 0.22, label, 12, font=FONT_SEMIBOLD, color=PRIMARY)


def add_image(cv, y, h, label, text, x=IMG_X, w=IMG_W):
    """Image placeholder with a caption block below it.

    No photo is supplied for this deck, so the image area is a flat accent
    block. It is the single accent element of the slide.
    """
    add_rect(cv, x, y, w, h, ACCENT, label="image")
    add_text(cv, x, y + h + 0.15, w, 0.22, label, 12, font=FONT_SEMIBOLD, color=PRIMARY)
    add_text(cv, x, y + h + 0.42, w, 0.22, text, 11)


def add_block(cv, x, y, w, label, text, lines=2):
    """Caption label with a body paragraph under it."""
    add_text(cv, x, y, w, 0.22, label, 12, font=FONT_SEMIBOLD, color=PRIMARY)
    add_text(cv, x, y + 0.3, w, lines * 0.375, text, 15, spacing=1.5)


def add_source(cv, text=SOURCE_NOTE, w=TEXT_W):
    add_text(cv, LEFT, BOTTOM - 0.2, w, 0.2, text, 10)


def check_layout(cv):
    """Fail the build when a shape leaves the margins or two shapes overlap."""
    eps = 0.005
    for label, x, y, w, h in cv.boxes:
        if x < LEFT - eps or y < TOP - eps or x + w > RIGHT + eps or y + h > BOTTOM + eps:
            raise ValueError(f"{cv.name}: {label!r} is outside the margins")
    for i, (la, ax, ay, aw, ah) in enumerate(cv.boxes):
        for lb, bx, by, bw, bh in cv.boxes[i + 1:]:
            if ax < bx + bw - eps and bx < ax + aw - eps and ay < by + bh - eps and by < ay + ah - eps:
                raise ValueError(f"{cv.name}: {la!r} overlaps {lb!r}")


def build_content(prs, name, section, title, blocks, caption, notes):
    """Content slide: section label, title, and up to three blocks on the left, image on the right."""
    cv = Canvas(prs, name)
    add_text(cv, LEFT, TOP, TEXT_W, 0.22, section, 12, font=FONT_SEMIBOLD, color=PRIMARY)
    add_text(cv, LEFT, 1.3, TEXT_W, 1.1, title, 32, bold=True, color=PRIMARY)
    for i, (label, text) in enumerate(blocks):
        y = 2.7 + i * 1.3
        if i:
            add_divider(cv, LEFT, y - 0.125, TEXT_W)
        add_block(cv, LEFT, y, TEXT_W, label, text)
    add_source(cv)
    add_image(cv, TOP, 4.7, *caption)
    cv.notes(notes)
    check_layout(cv)


def build_cover(prs):
    cv = Canvas(prs, "cover")
    add_text(cv, LEFT, 1.5, TEXT_W, 0.95, "AI 발전 2026", 54, bold=True, color=PRIMARY)
    add_text(cv, LEFT, 2.65, TEXT_W, 0.5, "빠르게, 그러나 고르지 않게", 28, font=FONT_LIGHT, color=SECONDARY)
    add_quote_line(cv, 3.7, "2026년 10월 현황")
    add_text(cv, LEFT, 4.5, TEXT_W, 1.5,
             ["성능, 에이전트, 투자, 일자리, 규제의 다섯 가지 흐름을",
              "2026년 10월까지 공개된 자료로 정리했습니다."], 15, spacing=1.5)
    add_image(cv, TOP, 4.7, "AI 발전 현황", "2026년 10월 기준 공개 자료 정리")
    cv.notes(
        "2026년 10월 기준 AI 발전 현황을 정리한 자료입니다. 성능, 에이전트, 투자와 전력, 일자리, "
        "규제와 안전 순서로 말씀드립니다. 일부 수치는 1차 보고서가 아닌 2차 요약에서 가져왔으므로 "
        "개별 수치는 참고용으로 봐 주시기 바랍니다."
    )
    check_layout(cv)


def build_section(prs):
    cv = Canvas(prs, "section")
    add_text(cv, LEFT, 1.3, TEXT_W, 0.95, "01", 54, bold=True, color=PRIMARY)
    add_text(cv, LEFT, 2.45, 7.0, 1.1, ["지금 AI는", "어디에 있는가"], 32, bold=True, color=PRIMARY)
    add_quote_line(cv, 4.0, "다섯 가지 흐름")
    add_text(cv, LEFT, 4.75, 7.0, 0.8,
             ["성능 · 에이전트 · 투자와 전력", "일자리 · 규제와 안전"], 15, spacing=1.5)
    add_rect(cv, 10.8, TOP, RIGHT - 10.8, BOTTOM - TOP, ACCENT, label="image")
    cv.notes(
        "오늘 다룰 흐름은 다섯 가지입니다. 모델 성능, AI 에이전트의 확산, 투자와 전력 수요, "
        "일자리와 임금, 그리고 각국의 규제와 안전 문제입니다."
    )
    check_layout(cv)


def build_data(prs):
    cv = Canvas(prs, "data")
    add_text(cv, LEFT, TOP, FULL_W, 0.22, "03 투자와 전력", 12, font=FONT_SEMIBOLD, color=PRIMARY)
    add_text(cv, LEFT, 1.3, FULL_W, 0.6, "투자는 사상 최대, 병목은 전력", 32, bold=True, color=PRIMARY)
    add_text(cv, LEFT, 2.05, FULL_W, 0.3, "전 세계 데이터센터 전력 소비량 (TWh)", 14)

    # Bar chart drawn with shapes: bar length is proportional to the value.
    bar_x, bar_max, bar_h = 2.9, 5.6, 0.6
    rows = [
        ("2025년", 485, LINE, "485 TWh", 24, PRIMARY),
        ("2030년 전망", 950, MUTED, "약 950 TWh", 36, ACCENT),  # the key number
    ]
    for i, (label, value, bar_color, value_text, size, color) in enumerate(rows):
        y = 2.7 + i * 0.95
        add_text(cv, LEFT, y, 1.7, bar_h, label, 15, color=PRIMARY, anchor=MSO_ANCHOR.MIDDLE)
        bar_w = bar_max * value / 950
        add_rect(cv, bar_x, y, bar_w, bar_h, bar_color, label="bar")
        add_text(cv, bar_x + bar_w + 0.25, y, RIGHT - bar_x - bar_w - 0.25, bar_h, value_text,
                 size, bold=True, color=color, anchor=MSO_ANCHOR.MIDDLE)

    add_divider(cv, LEFT, 4.7, FULL_W)
    facts = [
        ("2026년 하이퍼스케일러 설비투자", "6,300억~6,970억 달러로 추정됩니다."),
        ("AI 인프라 비중", ["설비투자의 약 75%가", "AI 인프라에 들어갑니다."]),
        ("AI 데이터센터", ["AI 데이터센터의 전력 수요는", "2025년에 50% 늘었습니다."]),
    ]
    col_w, gap = 3.4, (FULL_W - 3 * 3.4) / 2
    for i, (label, text) in enumerate(facts):
        add_block(cv, LEFT + i * (col_w + gap), 4.95, col_w, label, text)
    add_source(cv, "출처: IEA, J.P. Morgan (research/ai-development-research-v2.md)", w=FULL_W)
    cv.notes(
        "IEA에 따르면 데이터센터는 2025년에 약 485 TWh의 전력을 썼고, 2030년에는 약 950 TWh로 "
        "두 배 가까이 늘 전망입니다. 이는 전 세계 전력 수요의 약 3%입니다. 2025년 데이터센터 전력 "
        "수요는 17% 늘었고 AI 데이터센터는 50% 늘었습니다. 설비투자는 J.P. Morgan 추정 6,970억 달러, "
        "다른 추정으로는 최대 6,300억 달러이며 2025년 기록인 3,880억 달러보다 약 62% 많습니다. "
        "AI 인프라 투자의 60% 이상은 연산 장비가 아니라 전력, 냉각, 건설에 쓰입니다."
    )
    check_layout(cv)


def build_closing(prs):
    cv = Canvas(prs, "closing")
    add_text(cv, LEFT, TOP, TEXT_W, 0.22, "핵심 정리", 12, font=FONT_SEMIBOLD, color=PRIMARY)
    add_text(cv, LEFT, 1.3, TEXT_W, 1.1, ["역량은 앞서가고", "나머지가 따라간다"], 32, bold=True,
             color=PRIMARY)
    add_quote_line(cv, 2.8, "감사합니다")
    add_text(cv, LEFT, 3.55, TEXT_W, 1.9,
             ["성능은 빠르게 오르지만 고르지 않습니다.",
              "에이전트 운영과 전력이 실제 제약입니다.",
              "일자리와 규제는 아직 방향을 찾고 있습니다."], 15, spacing=1.5)
    add_divider(cv, LEFT, 5.55, TEXT_W)
    add_text(cv, LEFT, 5.7, TEXT_W, 0.8,
             ["주요 출처: Stanford AI Index 2026, IEA",
              "International AI Safety Report 2026",
              "PwC 2026 Global AI Jobs Barometer"], 10, spacing=1.5)
    add_image(cv, TOP, 4.7, "AI 발전 2026", "2026년 10월 기준 공개 자료 정리")
    cv.notes(
        "정리하겠습니다. 첫째, 역량은 빠르게 오르지만 고르지 않고 벤치마크는 실제 신뢰도를 과대평가합니다. "
        "둘째, 에이전트는 빠르게 퍼지지만 대부분의 파일럿이 운영 단계에 이르지 못합니다. "
        "셋째, 투자는 사상 최대이고 전력이 제약입니다. 넷째, AI는 숙련 인력의 임금을 올리지만 "
        "신입의 진입 경로를 좁힙니다. 다섯째, 규제는 나라마다 갈라지고 안전 실무는 역량을 따라가지 못하고 있습니다. "
        "감사합니다."
    )
    check_layout(cv)


def build(output_path):
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(SLIDE_W), Inches(SLIDE_H)
    prs.core_properties.title = "AI 발전 2026"
    prs.core_properties.subject = "빠르게, 그러나 고르지 않게"

    build_cover(prs)
    build_section(prs)
    build_content(
        prs, "capability", "01 성능",
        ["성능은 빠르게,", "고르지 않게 오른다"],
        [
            ("가속", ["SWE-bench 최고 점수가 1년 만에", "약 60%에서 100% 가까이로 올랐습니다."]),
            ("들쭉날쭉한 경계", "올림피아드 금메달 모델도 아날로그 시계는 50.1%만 읽습니다."),
            ("좁혀진 격차", "미국과 중국의 성능 격차는 사실상 사라졌습니다."),
        ],
        ("들쭉날쭉한 경계", "벤치마크 점수와 실제 성능은 다릅니다"),
        "Stanford AI Index 2026에 따르면 AI 역량은 정체가 아니라 가속하고 있습니다. SWE-bench 코딩 "
        "벤치마크 최고 점수는 1년 사이 약 60%에서 100% 가까이로 올랐습니다. 다만 경계는 들쭉날쭉합니다. "
        "국제수학올림피아드에서 금메달을 딴 모델이 아날로그 시계는 50.1%만 맞게 읽습니다. 대표 벤치마크만으로 "
        "실제 성능을 판단하기 어렵다는 뜻입니다. 오픈 웨이트 모델도 최전선에 가까워졌고, 상위 5개 중 4개가 "
        "중국 연구소 모델입니다. 모델 가격은 계속 내려가고 있습니다.",
    )
    build_content(
        prs, "agents", "02 에이전트",
        ["에이전트는 퍼졌지만", "운영은 어렵다"],
        [
            ("확산", ["1분기에 출시되거나 갱신된 기업 앱의 80%가", "에이전트를 내장했습니다."]),
            ("운영 격차", "에이전트 파일럿의 약 88%는 운영 단계에 이르지 못합니다."),
            ("걸림돌", "평가 공백 64%, 거버넌스 마찰 57%, 모델 신뢰성 51% 순입니다."),
        ],
        ("챗봇에서 에이전트로", "도구를 쓰고 컴퓨터를 조작하는 AI"),
        "AI는 챗봇에서 도구를 쓰고, 웹을 탐색하고, 컴퓨터를 조작하는 에이전트로 넘어가고 있습니다. "
        "Gartner는 2026년 1분기에 출시되거나 갱신된 기업 애플리케이션의 80%가 AI 에이전트를 하나 이상 "
        "내장했다고 보고합니다. 2024년에는 33%였습니다. 도입률은 조사마다 달라서 기업의 65%가 이미 "
        "에이전트를 쓴다는 조사도 있고, 57.3%가 운영 중이라는 조사도 있습니다. 반면 파일럿의 약 88%는 "
        "운영 단계에 이르지 못합니다.",
    )
    build_data(prs)
    build_content(
        prs, "jobs", "04 일자리",
        ["보상은 늘고", "입구는 좁아진다"],
        [
            ("임금 프리미엄", "AI 기술의 평균 임금 프리미엄은 57%에서 62%로 올랐습니다."),
            ("일자리 증가", ["AI 기술을 요구하는 일자리는 69% 늘었고,", "전체 시장은 9% 늘었습니다."]),
            ("신입의 문턱", "고용주의 31%가 신입 직무의 경력 요건을 높였습니다."),
        ],
        ("좁아지는 입구", "신입에게 요구되는 역량이 높아집니다"),
        "PwC 2026 Global AI Jobs Barometer는 27개 국가와 지역의 채용 공고 10억 건 이상을 분석했습니다. "
        "AI 기술의 평균 임금 프리미엄은 62%이고, 정부 부문 16%에서 소비재 부문 118%까지 차이가 큽니다. "
        "AI 기술을 요구하는 일자리는 69% 늘어 전체 시장(9%)보다 약 8배 빨랐습니다. ZipRecruiter에 따르면 "
        "고용주의 38%가 기초 데이터 처리 업무를 신입에서 AI로 옮겼고 31%가 신입 경력 요건을 높였습니다. "
        "AI가 신입 일자리를 없애기보다는 요구 수준을 높이고 진입 경로를 좁히고 있습니다.",
    )
    build_content(
        prs, "regulation", "05 규제와 안전",
        ["규제는 갈라지고", "안전은 뒤처진다"],
        [
            ("EU와 미국", ["EU는 고위험 AI 의무를 2027년 12월로 미뤘습니다.", "미국은 연방 선점을 추진합니다."]),
            ("한국", "AI 기본법이 2026년 1월 22일 시행되었습니다."),
            ("안전", "기록된 AI 사고는 1년 사이 233건에서 362건으로 늘었습니다."),
        ],
        ("서로 다른 길", "EU는 연기, 미국은 선점, 한국은 시행"),
        "EU는 디지털 옴니버스 패키지로 독립형 고위험 AI 시스템의 의무를 2026년 8월에서 2027년 12월로 "
        "미뤘습니다. 투명성 의무는 2026년 8월 2일부터 그대로 적용됩니다. 미국은 2025년 12월 행정명령으로 "
        "주 AI 법에 대한 연방 선점을 추진하지만, 행정명령만으로 주법을 무효로 할 수는 없습니다. "
        "한국의 AI 기본법은 2026년 1월 22일 시행되었고, 고영향 AI에 더 엄격한 의무를 두며 생성형 AI에는 "
        "사전 고지와 표시를 요구합니다. Stanford AI Index 2026에 따르면 기록된 AI 사고는 233건에서 "
        "362건으로 늘었습니다.",
    )
    build_closing(prs)

    prs.save(output_path)


if __name__ == "__main__":
    build(sys.argv[1])

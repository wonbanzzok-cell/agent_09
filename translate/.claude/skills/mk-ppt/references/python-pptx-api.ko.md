# python-pptx API 참고 문서

라이브러리가 지원하는 작업별 코드를 `python-pptx` 1.0.2 기준으로 정리했다. 필요한 절만 읽는다.

## 목차

1. [스크립트 기본 틀과 헬퍼](#1-스크립트-기본-틀과-헬퍼)
2. [프레젠테이션과 슬라이드](#2-프레젠테이션과-슬라이드)
3. [플레이스홀더](#3-플레이스홀더)
4. [도형](#4-도형)
5. [텍스트](#5-텍스트)
6. [그림](#6-그림)
7. [표](#7-표)
8. [차트](#8-차트)
9. [채우기, 선, 색](#9-채우기-선-색)
10. [동작과 미디어](#10-동작과-미디어)
11. [읽기와 추출](#11-읽기와-추출)
12. [XML 우회 방법](#12-xml-우회-방법)

## 1. 스크립트 기본 틀과 헬퍼

모든 빌드 스크립트는 여기에서 시작한다. 헬퍼는 거의 모든 슬라이드에서 하는 두 가지 일을 맡는다. 한글에도 적용되는 글꼴 지정과 텍스트 상자 추가다.

```python
"""Build <주제>_발표자료_v<N>.pptx. Usage: python build-presentation-v<N>.py <output.pptx>"""

import sys

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.oxml.xmlchemy import OxmlElement
from pptx.util import Inches, Pt

FONT = "맑은 고딕"
ACCENT = RGBColor(0x1F, 0x4E, 0x79)
DARK = RGBColor(0x26, 0x26, 0x26)
GRAY = RGBColor(0x59, 0x59, 0x59)

SLIDE_W, SLIDE_H = Inches(13.333), Inches(7.5)
MARGIN = Inches(0.6)
BLANK = 6  # index of the blank layout in the default template


def set_font_name(run, name=FONT):
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


def style_run(run, size, bold=False, color=DARK):
    set_font_name(run)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color


def add_text(slide, left, top, width, height, text, size=20, bold=False,
             color=DARK, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    """Add a text box. Pass a list of strings to get one paragraph per item."""
    box = slide.shapes.add_textbox(left, top, width, height)
    frame = box.text_frame
    frame.word_wrap = True
    frame.vertical_anchor = anchor
    lines = text if isinstance(text, list) else [text]
    for i, line in enumerate(lines):
        para = frame.paragraphs[0] if i == 0 else frame.add_paragraph()
        para.alignment = align
        run = para.add_run()
        run.text = line
        style_run(run, size, bold, color)
    return box


def add_title(slide, text):
    return add_text(slide, MARGIN, Inches(0.4), SLIDE_W - 2 * MARGIN, Inches(1.0),
                    text, size=32, bold=True, color=ACCENT, anchor=MSO_ANCHOR.MIDDLE)


def build(output_path):
    prs = Presentation()
    prs.slide_width, prs.slide_height = SLIDE_W, SLIDE_H

    slide = prs.slides.add_slide(prs.slide_layouts[BLANK])
    add_title(slide, "제목")
    add_text(slide, MARGIN, Inches(1.6), SLIDE_W - 2 * MARGIN, Inches(5.0),
             ["첫 번째 요점", "두 번째 요점"], size=22)

    prs.save(output_path)


if __name__ == "__main__":
    build(sys.argv[1])
```

저장소 루트에서 실행한다: `python scripts/build-presentation-v<N>.py "presentation/<주제>_발표자료_v<N>.pptx"`. 출력 폴더가 없으면 먼저 만든다.

## 2. 프레젠테이션과 슬라이드

```python
prs = Presentation()                 # new file from the built-in 4:3 template
prs = Presentation("template.pptx")  # existing file or template; also accepts a file-like object
prs.save("out.pptx")                 # path or file-like object

prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)  # 16:9
prs.slide_width, prs.slide_height = Inches(10), Inches(7.5)      # 4:3

# Document properties
props = prs.core_properties
props.title, props.author, props.subject = "제목", "작성자", "주제"
props.keywords, props.category, props.comments = "AI, 보고서", "발표", "설명"

# Layouts in the default template:
# 0 Title, 1 Title and Content, 2 Section Header, 3 Two Content, 4 Comparison,
# 5 Title Only, 6 Blank, 7 Content with Caption, 8 Picture with Caption,
# 9 Title and Vertical Text, 10 Vertical Title and Text
layout = prs.slide_layouts[6]
layout = prs.slide_layouts.get_by_name("Blank")
slide = prs.slides.add_slide(layout)

# Access
for slide in prs.slides: ...
slide = prs.slides[0]
slide = prs.slides.get(slide_id)
position = prs.slides.index(slide)
slide.slide_id, slide.name, slide.slide_layout.name

# Masters and unused layouts
master = prs.slide_masters[0]
prs.slide_layouts.remove(prs.slide_layouts[7])  # fails if a slide uses the layout

# Background
fill = slide.background.fill
fill.solid()
fill.fore_color.rgb = RGBColor(0xF2, 0xF2, 0xF2)
slide.follow_master_background  # False once the slide has its own background

# Speaker notes
slide.notes_slide.notes_text_frame.text = "발표자 노트"
if slide.has_notes_slide:
    notes = slide.notes_slide.notes_text_frame.text
```

## 3. 플레이스홀더

플레이스홀더 인덱스는 레이아웃에서 정해지므로, 템플릿을 쓰기 전에 `inspect_pptx.py <file> --layouts`를 실행해 확인한다.

```python
slide = prs.slides.add_slide(prs.slide_layouts[1])  # Title and Content
slide.shapes.title.text = "제목"                     # None when the layout has no title

for ph in slide.placeholders:
    print(ph.placeholder_format.idx, ph.placeholder_format.type, ph.name)

body = slide.placeholders[1]          # lookup is by idx, not by list position
body.text_frame.text = "첫 줄"
para = body.text_frame.add_paragraph()
para.text, para.level = "하위 항목", 1

# Content placeholders that accept an object. The method exists only on the
# matching placeholder type (picture, table, or chart placeholder).
picture = slide.placeholders[1].insert_picture("image.png")
frame = slide.placeholders[1].insert_table(rows=3, cols=4)   # frame.table
frame = slide.placeholders[1].insert_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, chart_data)
```

플레이스홀더에 입력한 텍스트는 레이아웃의 글꼴을 물려받는다. 한글에 특정 글꼴이 필요하면 그 런에 `set_font_name`을 적용한다.

## 4. 도형

```python
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE

shapes = slide.shapes

# Auto shapes: RECTANGLE, ROUNDED_RECTANGLE, OVAL, RIGHT_ARROW, CHEVRON,
# STAR_5_POINT, FLOWCHART_PROCESS, CLOUD_CALLOUT, and about 180 more
box = shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1), Inches(2), Inches(3), Inches(1.2))
box.adjustments[0] = 0.2          # corner roundness, 0.0 to 0.5
box.text_frame.text = "도형 안 글자"

# Text box
textbox = shapes.add_textbox(Inches(1), Inches(1), Inches(4), Inches(1))

# Connectors: STRAIGHT, ELBOW, CURVE
line = shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(1), Inches(1), Inches(4), Inches(1))
line.begin_connect(box_a, 3)      # connection site index: 0 top, 1 left, 2 bottom, 3 right
line.end_connect(box_b, 1)

# Freeform polygon
builder = shapes.build_freeform(Inches(1), Inches(1))
builder.add_line_segments([(Inches(2), Inches(1)), (Inches(1.5), Inches(2))], close=True)
polygon = builder.convert_to_shape()

# Group
group = shapes.add_group_shape()
group.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1), Inches(1), Inches(1), Inches(1))
for child in group.shapes: ...

# Common properties
shape.left, shape.top, shape.width, shape.height = Inches(1), Inches(1), Inches(3), Inches(2)
shape.rotation = 45.0
shape.name = "Summary box"
shape.shape_id, shape.shape_type, shape.is_placeholder
shape.has_text_frame, shape.has_table, shape.has_chart
shape.shadow.inherit = False      # remove the theme shadow
```

가운데 정렬: `left = (prs.slide_width - width) // 2`. 길이는 정수이므로 `//`를 쓴다.

## 5. 텍스트

```python
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN

frame = shape.text_frame
frame.word_wrap = True
frame.vertical_anchor = MSO_ANCHOR.MIDDLE            # TOP, MIDDLE, BOTTOM
frame.auto_size = MSO_AUTO_SIZE.NONE                 # SHAPE_TO_FIT_TEXT, TEXT_TO_FIT_SHAPE
frame.margin_left = frame.margin_right = Inches(0.1)
frame.margin_top = frame.margin_bottom = Inches(0.05)

frame.text = "첫 단락\n둘째 단락"      # replaces everything; \n starts a new paragraph
frame.clear()                         # leaves one empty paragraph

para = frame.paragraphs[0]
para.alignment = PP_ALIGN.CENTER      # LEFT, CENTER, RIGHT, JUSTIFY
para.level = 1                        # indent level 0-8
para.line_spacing = 1.2               # multiple of line height, or Pt(24) for exact
para.space_before, para.space_after = Pt(6), Pt(6)
para.add_line_break()                 # line break inside the paragraph

run = para.add_run()
run.text = "강조"
font = run.font
font.size, font.bold, font.italic, font.underline = Pt(24), True, False, True
font.color.rgb = RGBColor(0xC0, 0x00, 0x00)
set_font_name(run, "맑은 고딕")       # helper from section 1

run.hyperlink.address = "https://example.com"

# Shrink text to fit the shape. Needs the .ttf path on Windows, and the file
# must exist, so prefer explicit sizes.
frame.fit_text(font_family="Malgun Gothic", max_size=24,
               font_file=r"C:\Windows\Fonts\malgun.ttf")
```

글머리 기호는 API로 제공되지 않는다. 텍스트 상자에는 글머리 기호가 없으므로 기호를 텍스트에 직접 넣거나(`"• 요점"`), 레이아웃이 글머리 기호를 제공하는 본문 플레이스홀더를 쓴다.

## 6. 그림

```python
# Give one of width or height and the other keeps the aspect ratio
picture = slide.shapes.add_picture("chart.png", Inches(1), Inches(1.5), width=Inches(6))
picture = slide.shapes.add_picture(image_stream, Inches(1), Inches(1.5), height=Inches(4))

# Crop: fraction of the original removed from each side
picture.crop_left, picture.crop_right = 0.1, 0.1
picture.crop_top, picture.crop_bottom = 0.0, 0.2

# Mask to a shape
picture.auto_shape_type = MSO_SHAPE.OVAL

# Border
picture.line.color.rgb = RGBColor(0x80, 0x80, 0x80)
picture.line.width = Pt(1)
```

지원 형식은 PNG, JPEG, GIF, BMP, TIFF 등이다. SVG는 지원하지 않으므로 먼저 PNG로 바꾼다. 그림을 상자 안에 맞추려면 가로세로 비율을 비교해 `width`와 `height` 중 먼저 한계에 닿는 쪽을 지정한다.

## 7. 표

```python
frame = slide.shapes.add_table(rows=4, cols=3, left=Inches(1), top=Inches(1.8),
                               width=Inches(11), height=Inches(2.4))
table = frame.table

table.columns[0].width = Inches(3)
table.rows[0].height = Inches(0.6)

cell = table.cell(0, 0)               # row, column
cell.text = "항목"
cell.vertical_anchor = MSO_ANCHOR.MIDDLE
cell.margin_left = cell.margin_right = Inches(0.1)
cell.fill.solid()
cell.fill.fore_color.rgb = ACCENT

# Text formatting works as in any text frame
for para in cell.text_frame.paragraphs:
    para.alignment = PP_ALIGN.CENTER
    for run in para.runs:
        style_run(run, 16, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF))

# Merge and split
table.cell(1, 0).merge(table.cell(2, 0))      # top-left cell merges through the other
origin = table.cell(1, 0)
origin.is_merge_origin, origin.span_height, origin.span_width
origin.split()

# Style options
table.first_row, table.last_row = True, False
table.first_col, table.last_col = False, False
table.horz_banding, table.vert_banding = True, False

for cell in table.iter_cells(): ...
```

`cell.text`를 먼저 넣고 런의 서식은 그 뒤에 지정한다. 텍스트를 대입하면 런이 새로 만들어지기 때문이다. 행은 API로 추가할 수 없다. 12절을 본다.

## 8. 차트

```python
from pptx.chart.data import BubbleChartData, CategoryChartData, XyChartData
from pptx.enum.chart import (XL_CHART_TYPE, XL_LABEL_POSITION, XL_LEGEND_POSITION,
                             XL_MARKER_STYLE, XL_TICK_LABEL_POSITION)

data = CategoryChartData()
data.categories = ["2023", "2024", "2025"]
data.add_series("매출", (12.5, 18.2, 24.9))
data.add_series("비용", (9.1, 11.4, 13.0))

frame = slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,
                               Inches(1), Inches(1.6), Inches(11), Inches(5), data)
chart = frame.chart
```

자주 쓰는 차트 종류: `COLUMN_CLUSTERED`, `COLUMN_STACKED`, `COLUMN_STACKED_100`, `BAR_CLUSTERED`, `BAR_STACKED`, `LINE`, `LINE_MARKERS`, `PIE`, `DOUGHNUT`, `AREA`, `AREA_STACKED`, `RADAR`, `XY_SCATTER`, `XY_SCATTER_LINES`, `BUBBLE`.

```python
# XY and bubble charts use their own data classes
xy = XyChartData()
series = xy.add_series("측정값")
series.add_data_point(1.0, 2.7)

bubble = BubbleChartData()
series = bubble.add_series("제품")
series.add_data_point(1.0, 2.7, 10)   # x, y, size

# Title and overall font
chart.has_title = True
chart.chart_title.text_frame.text = "연도별 매출"
chart.font.size = Pt(14)
chart.font.name = FONT
chart.chart_style = 10                # built-in style number, 1-48

# Legend
chart.has_legend = True
chart.legend.position = XL_LEGEND_POSITION.BOTTOM
chart.legend.include_in_layout = False

# Axes (not available on pie and doughnut charts)
value_axis = chart.value_axis
value_axis.minimum_scale, value_axis.maximum_scale = 0, 30
value_axis.major_unit = 10
value_axis.has_major_gridlines = True
value_axis.tick_labels.number_format = '0"억"'
value_axis.tick_labels.number_format_is_linked = False
value_axis.has_title = True
value_axis.axis_title.text_frame.text = "억 원"

category_axis = chart.category_axis
category_axis.tick_labels.font.size = Pt(12)
category_axis.tick_label_position = XL_TICK_LABEL_POSITION.LOW
category_axis.reverse_order = False
category_axis.visible = True

# Plot and data labels
plot = chart.plots[0]
plot.gap_width = 80                   # bar and column charts
plot.overlap = -10
plot.vary_by_categories = False
plot.has_data_labels = True
labels = plot.data_labels
labels.number_format, labels.number_format_is_linked = "0.0", False
labels.position = XL_LABEL_POSITION.OUTSIDE_END
labels.show_value = True              # also show_percentage, show_category_name, show_series_name
labels.font.size = Pt(12)

# Series and points
series = plot.series[0]
series.format.fill.solid()
series.format.fill.fore_color.rgb = ACCENT
series.invert_if_negative = False
point = series.points[2]
point.format.fill.solid()
point.format.fill.fore_color.rgb = RGBColor(0xC0, 0x00, 0x00)

# Line charts
series.smooth = True
series.format.line.width = Pt(2.5)
series.marker.style, series.marker.size = XL_MARKER_STYLE.CIRCLE, 8

# Replace the data of an existing chart, keeping its formatting
chart.replace_data(new_data)
```

원형 차트는 계열을 하나만 받는다. 조각에 레이블을 붙이려면 `labels.show_percentage = True`와 `number_format = "0%"`를 지정한다. 다단계 범주: `data.add_category("상반기").add_sub_category("1분기")`.

## 9. 채우기, 선, 색

```python
from pptx.enum.dml import MSO_LINE, MSO_PATTERN, MSO_THEME_COLOR

fill = shape.fill
fill.solid()
fill.fore_color.rgb = RGBColor(0x1F, 0x4E, 0x79)
fill.fore_color.theme_color = MSO_THEME_COLOR.ACCENT_1
fill.fore_color.brightness = 0.4      # -1.0 darker to 1.0 lighter
fill.background()                     # no fill

fill.gradient()
fill.gradient_angle = 90
stops = fill.gradient_stops
stops[0].color.rgb = RGBColor(0x1F, 0x4E, 0x79)
stops[1].color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

fill.patterned()
fill.pattern = MSO_PATTERN.WIDE_UPWARD_DIAGONAL
fill.fore_color.rgb, fill.back_color.rgb = RGBColor(0, 0, 0), RGBColor(255, 255, 255)

line = shape.line
line.color.rgb = RGBColor(0x40, 0x40, 0x40)
line.width = Pt(1.5)
line.dash_style = MSO_LINE.DASH
line.fill.background()                # no outline
```

색: `RGBColor(0x1F, 0x4E, 0x79)` 또는 `RGBColor.from_string("1F4E79")`. 투명도는 API가 없다.

## 10. 동작과 미디어

```python
# Click to open a URL
shape.click_action.hyperlink.address = "https://example.com"

# Click to jump to another slide
shape.click_action.target_slide = prs.slides[0]

# Video (experimental in the library). The poster image shows before playback.
slide.shapes.add_movie("clip.mp4", Inches(1), Inches(1), Inches(8), Inches(4.5),
                       poster_frame_image="poster.png", mime_type="video/mp4")

# Embedded file shown as an icon: Excel, Word, or PowerPoint
from pptx.enum.shapes import PROG_ID
slide.shapes.add_ole_object("data.xlsx", PROG_ID.XLSX, Inches(1), Inches(1))
```

## 11. 읽기와 추출

전체 구조는 `scripts/inspect_pptx.py`로 본다. 원하는 방식으로 추출하려면 다음을 쓴다.

```python
from pptx.enum.shapes import MSO_SHAPE_TYPE


def iter_shapes(shapes):
    """Yield every shape, descending into groups."""
    for shape in shapes:
        yield shape
        if shape.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from iter_shapes(shape.shapes)


for number, slide in enumerate(prs.slides, start=1):
    for shape in iter_shapes(slide.shapes):
        if shape.has_text_frame:
            text = shape.text_frame.text
        if getattr(shape, "has_table", False) and shape.has_table:
            rows = [[cell.text for cell in row.cells] for row in shape.table.rows]
        if getattr(shape, "has_chart", False) and shape.has_chart:
            plot = shape.chart.plots[0]
            categories = list(plot.categories)
            values = {s.name: list(s.values) for s in plot.series}
        if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
            image = shape.image
            with open(f"slide{number}_{shape.shape_id}.{image.ext}", "wb") as f:
                f.write(image.blob)
    if slide.has_notes_slide:
        notes = slide.notes_slide.notes_text_frame.text
```

서식을 유지하면서 텍스트를 바꾸려면 런 단위로 `run.text`를 바꾼다. `text_frame.text`나 `paragraph.text`에 대입하면 런의 서식이 사라진다. 한 구절이 여러 런에 나뉘어 있을 수 있으므로, 먼저 단락 전체 텍스트에서 찾은 뒤 어느 런을 고칠지 정한다.

## 12. XML 우회 방법

다음 작업에는 공식 API가 없다. 비공개 속성을 통해 내부 XML을 직접 고치므로, 결과에 `inspect_pptx.py`를 실행해 확인한다.

```python
import copy


def delete_slide(prs, index):
    id_list = prs.slides._sldIdLst
    slide_id = id_list[index]
    prs.part.drop_rel(slide_id.rId)
    id_list.remove(slide_id)


def move_slide(prs, old_index, new_index):
    id_list = prs.slides._sldIdLst
    slide_id = id_list[old_index]
    id_list.remove(slide_id)
    id_list.insert(new_index, slide_id)


def delete_shape(shape):
    element = shape._element
    element.getparent().remove(element)


def send_to_back(shape):
    tree = shape._element.getparent()
    tree.remove(shape._element)
    tree.insert(2, shape._element)    # positions 0 and 1 hold the group properties


def bring_to_front(shape):
    tree = shape._element.getparent()
    tree.remove(shape._element)
    tree.append(shape._element)


def add_table_row(table):
    """Append a copy of the last row with its text cleared."""
    tbl = table._tbl
    new_row = copy.deepcopy(tbl.tr_lst[-1])
    tbl.append(new_row)
    row = table.rows[len(table.rows) - 1]
    for cell in row.cells:
        cell.text = ""
    return row


def delete_table_row(table, index):
    tbl = table._tbl
    tbl.remove(tbl.tr_lst[index])
```

- 그리는 순서는 슬라이드 안 도형의 순서와 같다. 따라서 앞뒤 순서를 정하는 가장 쉬운 방법은 뒤에 깔릴 도형을 먼저 추가하는 것이다.
- 행을 추가하거나 삭제해도 표의 프레임 높이는 그대로다. `frame.height`를 행 높이의 합으로 지정한다.
- **슬라이드 복제**는 XML로는 믿을 만하게 되지 않는다. 그림, 차트, 링크가 별도의 파트에 있어 함께 복사해야 하기 때문이다. 대신 그 슬라이드를 만드는 함수를 한 번 더 호출한다. 스크립트 없이 파일만 있는 경우에는 텍스트 상자와 자동 도형만 `copy.deepcopy(shape._element)`로 복사해 새 슬라이드의 `shapes._spTree`에 붙이고, 그림과 차트는 옮겨지지 않았다고 사용자에게 알린다.

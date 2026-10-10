"""Print the structure of a .pptx file: size, layouts, slides, shapes, text, notes.

Usage:
    python inspect_pptx.py <file.pptx> [--layouts] [--max-text N]

    --layouts     also list every slide layout and its placeholders
    --max-text N  truncate each text to N characters (default 80, 0 = no limit)
"""

import argparse
import sys

from pptx import Presentation
from pptx.util import Emu


def inches(value):
    return "?" if value is None else f"{Emu(value).inches:.2f}"


def clip(text, limit):
    text = " / ".join(line for line in text.replace("\v", "\n").splitlines() if line.strip())
    if limit and len(text) > limit:
        return text[:limit] + "..."
    return text


def shape_kind(shape):
    try:
        kind = shape.shape_type
    except NotImplementedError:
        return "UNKNOWN"
    return "UNKNOWN" if kind is None else kind.name


def describe_placeholder(shape):
    fmt = shape.placeholder_format
    return f"placeholder idx={fmt.idx} type={fmt.type.name if fmt.type is not None else '?'}"


def print_shape(shape, limit, slide_w, slide_h, indent="    "):
    parts = [f"[{shape.shape_id}] {shape_kind(shape)} \"{shape.name}\""]
    parts.append(
        f"pos=({inches(shape.left)}, {inches(shape.top)}) "
        f"size=({inches(shape.width)} x {inches(shape.height)}) in"
    )
    if shape.is_placeholder:
        parts.append(describe_placeholder(shape))
    print(indent + "  ".join(parts))

    detail = indent + "    "
    if None not in (shape.left, shape.top, shape.width, shape.height) and indent == "    ":
        if (
            shape.left < 0
            or shape.top < 0
            or shape.left + shape.width > slide_w
            or shape.top + shape.height > slide_h
        ):
            print(detail + "WARNING: extends outside the slide")

    if getattr(shape, "has_text_frame", False) and shape.has_text_frame:
        text = shape.text_frame.text
        if text.strip():
            print(detail + f"text: {clip(text, limit)}")
        elif shape.is_placeholder:
            print(detail + "WARNING: empty placeholder")

    if getattr(shape, "has_table", False) and shape.has_table:
        table = shape.table
        print(detail + f"table: {len(table.rows)} rows x {len(table.columns)} cols")
        for r, row in enumerate(table.rows):
            cells = [clip(cell.text, 20) for cell in row.cells]
            print(detail + f"  row {r}: {' | '.join(cells)}")

    if getattr(shape, "has_chart", False) and shape.has_chart:
        chart = shape.chart
        try:
            chart_type = chart.chart_type.name
        except Exception:
            chart_type = "UNKNOWN"
        title = chart.chart_title.text_frame.text if chart.has_title else ""
        print(detail + f"chart: {chart_type} title=\"{title}\"")
        for plot in chart.plots:
            categories = [str(c) for c in plot.categories]
            if categories:
                print(detail + f"  categories: {', '.join(categories)}")
            for series in plot.series:
                print(detail + f"  series \"{series.name}\": {list(series.values)}")

    if shape_kind(shape) == "PICTURE":
        try:
            image = shape.image
            print(detail + f"image: {image.content_type} {image.size[0]}x{image.size[1]} px")
        except Exception:
            print(detail + "image: linked or unreadable")

    if shape_kind(shape) == "GROUP":
        for child in shape.shapes:
            print_shape(child, limit, slide_w, slide_h, indent + "    ")


def main():
    parser = argparse.ArgumentParser(description="Print the structure of a .pptx file.")
    parser.add_argument("path")
    parser.add_argument("--layouts", action="store_true")
    parser.add_argument("--max-text", type=int, default=80)
    args = parser.parse_args()

    # Windows consoles default to a legacy code page that cannot print Korean.
    sys.stdout.reconfigure(encoding="utf-8")

    prs = Presentation(args.path)
    slide_w, slide_h = prs.slide_width, prs.slide_height

    print(f"File: {args.path}")
    print(f"Slide size: {inches(slide_w)} x {inches(slide_h)} in")
    print(f"Slides: {len(prs.slides)}")
    props = prs.core_properties
    print(f"Title: \"{props.title}\"  Author: \"{props.author}\"")

    if args.layouts:
        print("\nLayouts:")
        for m, master in enumerate(prs.slide_masters):
            for i, layout in enumerate(master.slide_layouts):
                print(f"  master {m} layout {i}: \"{layout.name}\"")
                for ph in layout.placeholders:
                    print(f"      {describe_placeholder(ph)} \"{ph.name}\"")

    for number, slide in enumerate(prs.slides, start=1):
        print(f"\nSlide {number}  (id={slide.slide_id}, layout=\"{slide.slide_layout.name}\")")
        if not len(slide.shapes):
            print("    (no shapes)")
        for shape in slide.shapes:
            print_shape(shape, args.max_text, slide_w, slide_h)
        if slide.has_notes_slide:
            notes = slide.notes_slide.notes_text_frame.text
            if notes.strip():
                print(f"    notes: {clip(notes, args.max_text)}")


if __name__ == "__main__":
    main()

"""Extract Figure 1 from a paper PDF.

Strategy: find the text block whose text starts with "Figure 1" (the caption).
Collect drawing/image bounding boxes that sit above the caption on the same page
and horizontally overlap the caption's span. Union them, pad, and render at 3x.
Fallback: crop a fixed-height region directly above the caption, using the
caption's width as the column span.
"""
import sys
import fitz

pdf_path, out_path = sys.argv[1], sys.argv[2]
doc = fitz.open(pdf_path)

def find_caption(doc):
    for pno in range(min(8, len(doc))):
        page = doc[pno]
        for block in page.get_text("blocks"):
            x0, y0, x1, y1, text, *_ = block
            t = " ".join(text.split())
            if t.startswith("Figure 1") or t.startswith("Fig. 1") or t.startswith("Fig 1"):
                return pno, fitz.Rect(x0, y0, x1, y1)
    return None, None

pno, cap = find_caption(doc)
if pno is None:
    print("NO_CAPTION_FOUND")
    sys.exit(1)

page = doc[pno]
pw, ph = page.rect.width, page.rect.height

def hoverlap(a, b):
    return min(a.x1, b.x1) - max(a.x0, b.x0) > 20

# graphics candidates above the caption
regions = []
for d in page.get_drawings():
    r = fitz.Rect(d["rect"])
    if r.y1 <= cap.y0 + 5 and r.height > 2 and r.width > 2 and hoverlap(r, cap):
        regions.append(r)
for img in page.get_images(full=True):
    try:
        for r in page.get_image_rects(img[0]):
            if r.y1 <= cap.y0 + 5 and hoverlap(r, cap):
                regions.append(fitz.Rect(r))
    except Exception:
        pass

fig = None
if regions:
    fig = regions[0]
    for r in regions[1:]:
        fig |= r
    # ignore absurd unions (full-page rules etc.)
    if fig.height < 30 or fig.height > ph * 0.75:
        fig = None

if fig is None:
    # fallback: fixed region above caption, caption-width
    top = max(cap.y0 - 320, 40)
    fig = fitz.Rect(cap.x0, top, cap.x1, cap.y0)

# pad and clip to page
fig = fitz.Rect(max(fig.x0 - 6, 0), max(fig.y0 - 6, 0),
                min(fig.x1 + 6, pw), min(fig.y1 + 4, ph))

pix = page.get_pixmap(clip=fig, matrix=fitz.Matrix(3, 3))
pix.save(out_path)
print(f"OK page={pno} rect={fig} size={pix.width}x{pix.height}")

import drawsvg as draw

IMG_SIZE = 400
MID_POINT = int(IMG_SIZE / 2)
GRIDLINE_COLOR = '#21295C'  # Space Cadet
SHAPES_COLOR = '#1C7293'  # Cerulean

d = draw.Drawing(IMG_SIZE, IMG_SIZE, origin = (0, 0))
d.append(draw.Rectangle(0, 0, IMG_SIZE, IMG_SIZE, fill = 'black', stroke = 'black'))

for i in range(0, IMG_SIZE + 1, 20):
    d.append(
        draw.Line(
            0,
            (i if i < MID_POINT else i - 1),
            IMG_SIZE,
            (i if i < MID_POINT else i - 1),
            stroke = GRIDLINE_COLOR,
            stroke_width = 1,
        )
    )
    d.append(
        draw.Line(
            (i if i < MID_POINT else i - 1),
            0,
            (i if i < MID_POINT else i - 1),
            IMG_SIZE,
            stroke = GRIDLINE_COLOR,
            stroke_width = 1,
        )
    )

d.append(
    draw.Circle(
        MID_POINT, MID_POINT, 190, fill = 'white', stroke_width = 20, stroke=SHAPES_COLOR
    )
)

d.append(
    draw.Text(
        'Δ∂',
        font_family = 'Fira Code',
        font_size = 180,
        x = MID_POINT,
        y = MID_POINT,
        stroke = SHAPES_COLOR,
        fill = SHAPES_COLOR,
        stroke_width = 5,
        text_anchor = 'middle',
        dominant_baseline = 'middle',
    )
)
d.save_svg('logo.svg')

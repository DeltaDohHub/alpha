import drawsvg as draw

IMG_SIZE_WIDTH = 1500
IMG_SIZE_HEIGHT = 500
MID_POINT_WIDTH = int(IMG_SIZE_WIDTH / 2)
MID_POINT_HEIGHT = int(IMG_SIZE_HEIGHT / 2)
GRIDLINE_COLOR = '#21295C'  # Space Cadet

d = draw.Drawing(IMG_SIZE_WIDTH, IMG_SIZE_HEIGHT, origin = (0, 0))
d.append(
    draw.Rectangle(0, 0, IMG_SIZE_WIDTH, IMG_SIZE_HEIGHT, fill = 'black', stroke = 'black')
)

for i in range(0, IMG_SIZE_HEIGHT + 1, 50):
    print(i)
    d.append(
        draw.Line(
            0,
            (i if i < MID_POINT_WIDTH else i - 1),
            IMG_SIZE_WIDTH,
            (i if i < MID_POINT_WIDTH else i - 1),
            stroke = GRIDLINE_COLOR,
            stroke_width = 3,
        )
    )

for i in range(0, IMG_SIZE_WIDTH + 1, 50):
    d.append(
        draw.Line(
            (i if i < MID_POINT_HEIGHT else i - 1),
            0,
            (i if i < MID_POINT_HEIGHT else i - 1),
            IMG_SIZE_HEIGHT,
            stroke = GRIDLINE_COLOR,
            stroke_width = 3,
        )
    )

d.save_svg('bg.svg')

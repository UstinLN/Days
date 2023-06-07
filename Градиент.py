from PIL import Image, ImageDraw


def gradient(color):
    new_image = Image.new('RGB', (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for i in range(256):
        if color == 'R':
            new_color = (i, 0, 0)
        elif color == 'G':
            new_color = (0, i, 0)
        elif color == 'B':
            new_color = (0, 0, i)
        draw.line((i * 2, 0, i * 2, 200), fill=new_color, width=2)
    new_image.save('Градиент.jpg', 'PNG')


gradient('R')

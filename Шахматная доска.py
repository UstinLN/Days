from PIL import Image, ImageDraw


def board(num, size):
    new_image = Image.new("RGB", (num * size, num * size), 'White')
    draw = ImageDraw.Draw(new_image)
    c = 0
    for i in range(0, num * size, size):
        for j in range(0, num * size, size):
            if c % 2 == 0:
                draw.rectangle((i, j, i + size, j + size), fill='Black')
            else:
                draw.rectangle((i, j, i + size, j + size), fill='White')
            c += 1
        if num % 2 == 0:
            c -= 1
        else:
            return 0
    new_image.save('Шахматная доска.jpg', "PNG")


board(8, 50)

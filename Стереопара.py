from PIL import Image, ImageDraw


def makeanagliph(filename, delta):
    im = Image.open(filename)
    x, y = im.size
    im = im.convert('RGB')
    r, g, b = im.split()
    new_image = Image.new('L', (x, y))
    region = r.crop((0, 0, x - delta, y))
    new_image.paste(region, (delta, 0, x, y))
    im2 = Image.merge('RGB', (new_image, g, b))
    im2.save('Стереопара.jpg')


makeanagliph('Рианна.jpg', 9)
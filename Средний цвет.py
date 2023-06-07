from PIL import Image


im = Image.open("Рианна.jpg")
pixels = im.load()
x, y = im.size
sum_pixel = 0
red, blue, green = 0, 0, 0

for i in range(x):
    for j in range(y):
        sum_pixel += 1
        r, g, b = pixels[i, j]
        red += r
        green += g
        blue += b
r = red // sum_pixel
g = green // sum_pixel
b = blue // sum_pixel

print(r, g, b)
from PIL import Image, ImageOps
ImageOps.mirror(Image.open("Рианна.jpg")).save("Рианна3.jpg")
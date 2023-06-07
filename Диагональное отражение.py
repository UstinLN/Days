from PIL import Image, ImageOps
im = Image.open('Рианна.jpg')
im_rotate = im.rotate(90)
im_mirror = ImageOps.mirror(im_rotate)
im_mirror.save('ДиагональноОтраженнаяРиана.jpg')
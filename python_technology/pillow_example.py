from PIL import Image

im = Image.open("Cat_August_2010-4.jpg")

print(im.format, im.size, im.mode)

im.show()

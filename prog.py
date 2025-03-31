from PIL import Image

image = Image.open("monro.jpg")
rgb_image = image.convert("RGB")
red, green, blue = rgb_image.split()
rgb_image = Image.merge("RGB", (red,green,blue))

coordinates = (100, 0, red.width, red.height)
cropped_red = red.crop(coordinates)
coordinates2 = (50, 0, red.width-50, red.height)
cropped_red2 = red.crop(coordinates2)
image3 = Image.blend(cropped_red, cropped_red2, 0.5)

coordinates3 = (0, 0, blue.width-100, blue.height)
cropped_blue = blue.crop(coordinates3)
coordinates4 = (50, 0, blue.width-50, blue.height)
cropped_blue2 = blue.crop(coordinates4)
image4 = Image.blend(cropped_blue, cropped_blue2, 0.5)

coordinates5 = (50, 0, red.width-50, red.height)
cropped_green = green.crop(coordinates5)

final_image = Image.merge("RGB", (image3, cropped_green, image4))
final_image.save('new_image.jpg')
final_image.thumbnail((80, 80))
final_image.save('final_image.jpg')
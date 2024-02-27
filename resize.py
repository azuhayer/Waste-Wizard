from PIL import Image
from os import listdir

image_dir = "images/originals/"

for batch in os.listdir(image_dir):
    for image in os.listdir(image_dir + batch):
        im = Image.open(image_dir + batch + "/" + image)
        im.thumbnail(size)
        im.save("images/thumbs/" + batch + "/" + image[:6] + "_thumb.jpg")
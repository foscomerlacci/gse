# from PIL import Image

# img = Image.open('/home/utente/Immagini/ordini/test_portrait.JPG')
# new_img = img.resize((img.width, img.height), Image.ANTIALIAS)
# quality_val = 60  # you can vary it considering the tradeoff for quality vs performance
# new_img.save("/home/utente/Immagini/ordini/test_portrait_ridotta.JPG",
#              "JPEG", quality=quality_val)
# print(img.width)
# print(img.height)

from PIL import Image, ExifTags
from time import time
import sys

# inizio=time()
# print(inizio)

try:
    # path=sys.argv[1] if len(sys.argv) > 1 else '.'
    path = sys.argv[1]
    image = Image.open(path)
    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation] == 'Orientation':
            break
    exif = dict(image._getexif().items())

    if exif[orientation] == 3:
        image = image.rotate(180, expand=True)
    elif exif[orientation] == 6:
        image = image.rotate(270, expand=True)
    elif exif[orientation] == 8:
        image = image.rotate(90, expand=True)
    new_image = image.resize((int(image.width // 2), int(image.height // 2)), Image.ANTIALIAS)
    # quality_val = 60 ##you can vary it considering the tradeoff for quality
    # vs performance

    new_image.save(
        path, "JPEG", quality=60)
    image.close()

    # fine=time()
    # print(fine)
    #
    # print(inizio,fine,fine-inizio)


except (AttributeError, KeyError, IndexError):
    # cases: image don't have getexif
    pass

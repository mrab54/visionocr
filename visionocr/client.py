from io import BytesIO

from visionocr import VisionOCR
from settings import VISION_KEY, VISION_ENDPOINT

vocr = VisionOCR(endpoint=VISION_ENDPOINT, key=VISION_KEY)

# txt = vocr.image_to_string(image=None, url_image='https://yahoo.com/narwhal.jpg')

with open('/home/mrab/Documents/image.png', 'rb') as f:
    image = f
    #image = BytesIO(f.read())
    txt = vocr.image_to_string(image=image, image_url=None)
    print(txt)

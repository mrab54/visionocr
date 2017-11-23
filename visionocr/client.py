from io import BytesIO

from visionocr import VisionOCR
from settings import REGION, KEY

vocr = VisionOCR(region=REGION, key=KEY)

# txt = vocr.image_to_string(image=None, url_image='https://yahoo.com/narwhal.jpg')

with open('c:\Users\mrab\Documents\stock.jpg', 'rb') as f:
    image = f
    #image = BytesIO(f.read())
    txt = vocr.image_to_string(image=image, image_url=None)
    print(txt)

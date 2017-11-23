from visionocr import VisionOCR
from settings import REGION, KEY

vocr = VisionOCR(region=REGION, key=KEY)

# txt = vocr.image_to_string(image=None, url_image='https://yahoo.com/narwhal.jpg')

txt = vocr.image_to_string(image='/home/narwhal.jpg', image_url=None)

print(txt)

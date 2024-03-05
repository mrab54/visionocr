import logging
import time
import requests
from builder import TextBuilder

logger = logging.getLogger(__name__)


class VisionOCR(object):
    _maxNumRetries = 10

    def __init__(self, endpoint, key):
        self.endpoint = endpoint
        self.key = key
        self.url = f'https://{endpoint}/computervision/imageanalysis:analyze?api-version=2024-02-01&features=read'

    def process_request(self, json, data, headers, params):
        result = None

        response = requests.request(
            'post', self.url, json=json, data=data, headers=headers, params=params)

        if response.status_code == 200 or response.status_code == 201:
            if 'content-length' in response.headers and int(response.headers['content-length']) == 0:
                result = None
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
                if 'application/json' in response.headers['content-type'].lower():
                    result = response.json() if response.content else None
                elif 'image' in response.headers['content-type'].lower():
                    result = response.content
        else:
            logger.error("Error code: {}".format(response.status_code))
            logger.error("Message: {}".format(response.json()))
        return result

    def image_to_string(self, image=None, image_url=None):
        params = {}
        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = self.key
        json = None
        data = None

        if image is not None:
            data = image.read()
            headers['Content-Type'] = 'application/octet-stream'
        elif image_url is not None:
            headers['Content-Type'] = 'application/json'
            json = {'url': image_url}
        else:
            return None

        result = self.process_request(json, data, headers, params)

        return TextBuilder.build(result)

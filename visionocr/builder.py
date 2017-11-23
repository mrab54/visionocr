class TextBuilder(object):
    def __init__(self):
        pass

    @staticmethod
    def build(response):
        built_text = []

        for region in response['regions']:
            for line in region['lines']:
                for word in line['words']:
                    built_text.append(word['text'])
                    built_text.append(' ')
                built_text.append('\n')
            built_text.append('\n\n')
        return ''.join(built_text)


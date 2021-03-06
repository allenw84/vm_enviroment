import requests
from time import time


class Video(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    def __init__(self):
        buffer_frame =[]
        self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]
        image = requests.get('http://140.114.79.179:8000',timeout = 1,headers={'Connection':'close'})
        self.frames = image
        for files in image:
            if ".jpg" in files:
                print(files)
                buffer_frame.append(image.content)

    def get_frame(self):
        return self.frames[int(time()) % 2]
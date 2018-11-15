# -*- coding: utf-8 -*-
# python -m SimpleHTTPServer 
import requests

PORT = 8000
URL = 'localhost:{port}'.format(port=PORT)


buffer_frame = [] 
#if request進來 :
image = requests.get('',timeout = 0.1)
for files in image:
    if ".jpg" in files:
        print(files)
        buffer_frame.append(image.content)

'''
with open('picture.jpg', 'wb') as file:
    file.write(response.content)
    file.close()
'''



if __name__	== '__main__':
    print ('hello')

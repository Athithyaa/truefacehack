from pytube import YouTube
import os

yt = YouTube("https://www.youtube.com/watch?v=cqgi1IjDoU8")
framesPersecond = 60

yt.set_filename('vid1')
size = len(yt.get_videos())
if size > 1:
	video = yt.get_videos()[size-2]
else:
	video = yt.get_videos()[0]

try:
	os.remove('tmp/vid1.mp4')
except OSError:
	print 'Some Problem Occured. Please try again!'

video.download('tmp/')

import cv2

vidcap = cv2.VideoCapture('tmp/vid1.mp4')
success, image = vidcap.read()
count = 0
success = True
while success:
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    if count % framesPersecond == 0:
    	cv2.imwrite("tmp/frame%d.jpg" % count, image)  # save frame as JPEG file
    count += 1

import requests
import base64
import json
import csv
from time import sleep

# Creating a collection
headers = {
    "x-api-key": "k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
    "Content-Type": "application/json",
}


url = "https://api.chui.ai/v1/identify"

temp_index = []
for i in range(count):
	if i % framesPersecond == 0:
		temp_index.append(i)

for i  in range(temp_index):
		data = {
		    "img":base64.b64encode(open('tmp/frame'+str(i)+'.jpg','rb').read()),
		    "collection_id": "ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMDjsKkJDA"
		}

		r  = requests.post(url,data=json.dumps(data),headers=headers)

		print r.json()


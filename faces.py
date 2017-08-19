import requests
import cv2
import json

headers = {
  "x-api-key":"k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
  "Content-Type":"image/jpeg",

}

url = "https://api.chui.ai/v1/facedetect"

r  = requests.post(url,data=open('frames/frame22.jpg','rb').read(),headers=headers)

data = r.json()

img = cv2.imread('frames/frame22.jpg')

count = 1
for face in data['faces']:
	x1 = int(face['bounding_box'][0])
	x2 = int(face['bounding_box'][1])
	y1 = int(face['bounding_box'][2])
	y2 = int(face['bounding_box'][3])
	image_patch = img[x2:y2,x1:y1]
	cv2.imwrite("face"+str(count)+".png", image_patch)
	count += 1
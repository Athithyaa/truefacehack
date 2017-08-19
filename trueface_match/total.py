# Adding the first profile
import requests
import base64
import json


#Creating a colelction
headers = {
  "x-api-key":"k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
  "Content-Type":"application/json",
}

url = "https://api.chui.ai/v1/collection"

data = {
  "name":"Celebrities",
  "unknowns":"false"
}

r  = requests.post(url,data=json.dumps(data),headers=headers)

print r.content

temp = json.loads(r.content)
collection_id = str(temp['data']['collection_id'])


#Adding the first profile
headers = {
  "x-api-key":"k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
  "Content-Type":"application/json",

}

url = "https://api.chui.ai/v1/enroll"

data = {
  "img0":base64.b64encode(open('0.jpg','rb').read()),
  "img1":base64.b64encode(open('1.jpg','rb').read()),
  "img2":base64.b64encode(open('2.jpg','rb').read()),
  "img3":base64.b64encode(open('3.jpg','rb').read()),
  "name":"Emilia Clarke",
  "collection_id":collection_id
}

r  = requests.post(url,data=json.dumps(data),headers=headers)
print r.json()
# Adding the Second profile

data = {
  "img0":base64.b64encode(open('01.png','rb').read()),
  "img1":base64.b64encode(open('11.jpg','rb').read()),
  "img2":base64.b64encode(open('13.jpg','rb').read()),
  "name":"Lord of the Rings Lady",
  "collection_id":collection_id
}

r  = requests.post(url,data=json.dumps(data),headers=headers)
print r.json()

url = "https://api.chui.ai/v1/identify"

data = {
  "img":base64.b64encode(open('face1.png','rb').read()),
  "collection_id":collection_id
}

r  = requests.post(url,data=json.dumps(data),headers=headers)

print r.json()




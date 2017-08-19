import requests
import base64
import json

headers = {
  "x-api-key":"k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
  "Content-Type":"application/json",

}

url = "https://api.chui.ai/v1/enroll"

data = {
  "img0":base64.b64encode(open('01.jpg','rb').read()),
  "img1":base64.b64encode(open('11.jpg','rb').read()),
  "img2":base64.b64encode(open('13.jpg','rb').read()),
  "name":"Lord of the Rings Lady",
  "collection_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMDjrNAIDA"
}

r  = requests.post(url,data=json.dumps(data),headers=headers)
print r.json()
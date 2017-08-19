import requests
import base64
import json

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
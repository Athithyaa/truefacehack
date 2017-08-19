import requests
import base64
import json

headers = {
  "content-type":"application/json",
  "x-api-key":"k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2"
}

url = "https://api.chui.ai/v1/train"


data = {
  "collection_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMDjrNAIDA"
}

r  = requests.post(url,data=json.dumps(data),headers=headers)

print r.json()
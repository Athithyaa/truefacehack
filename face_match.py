# import requests
# import base64
# import json

headers = {
  "x-api-key":"k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
  "Content-Type":"application/json",

}

url = "https://api.chui.ai/v1/match"

data = {
  "img":base64.b64encode(open('face1.png','rb').read()),
  "id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgMDjlYULDA"
}

r  = requests.post(url,data=json.dumps(data),headers=headers)

print r.json()


import requests
import base64
import json

headers = {
  "x-api-key":"k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
  "Content-Type":"application/json",
}

url = "https://api.chui.ai/v1/identify"


data = {
  "img":base64.b64encode(open('face1.png','rb').read()),
  "collection_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMDjrNAIDA"
}

r  = requests.post(url,data=json.dumps(data),headers=headers)

print r.json()
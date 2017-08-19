import requests
import base64
import json

headers = {
  "content-type":"application/json",
  "x-api-key":"k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2"

}

url = "https://api.chui.ai/v1/collection"


data = {
  "enrollment_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpFbnJvbGxtZW50GICAgIDE25QJDA",
  "collection_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMCn7tQIDA"
}

r  = requests.put(url,data=json.dumps(data),headers=headers)

print r.json()
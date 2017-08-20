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

data = {
    "img":base64.b64encode(open('trueface_identity/mrauch.jpg','rb').read()),
    "collection_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMDjsKkJDA"
}

r  = requests.post(url,data=json.dumps(data),headers=headers)

print r.json()

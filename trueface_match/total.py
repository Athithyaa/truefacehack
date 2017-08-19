# Adding the first profile
import requests
import base64
import json
import csv

# Creating a colelction
headers = {
    "x-api-key": "k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
    "Content-Type": "application/json",
}

url = "https://api.chui.ai/v1/collection"

data = {
    "name": "Celebrities",
    "unknowns": "false"
}

r = requests.post(url, data=json.dumps(data), headers=headers)

print r.content

temp = json.loads(r.content)
collection_id = str(temp['data']['collection_id'])

# Adding the first profile
headers = {
    "x-api-key": "k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
    "Content-Type": "application/json",
}

url = "https://api.chui.ai/v1/enroll"

with open('../data/wiki.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        filename = '../data/wiki/'
        data = {
            "img0": base64.b64encode(open(filename + row[1], 'rb').read()),
            "name": row[0]
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        print r.json()

# Adding the Second profile

url = "https://api.chui.ai/v1/identify"

data = {
    "img": base64.b64encode(open('face1.png', 'rb').read()),
    "collection_id": collection_id
}

r = requests.post(url, data=json.dumps(data), headers=headers)

print r.json()

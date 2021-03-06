# Adding the first profile
import requests
import base64
import json
import csv
from time import sleep

# Creating a colelction
headers = {
    "x-api-key": "0a4Vb652vN8fRvRB4oalu3veppkte6847k8RQqGd",
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
    "x-api-key": "0a4Vb652vN8fRvRB4oalu3veppkte6847k8RQqGd",
    "Content-Type": "application/json",
}

enroll_url = "https://api.chui.ai/v1/enroll"
update_collection_url = "https://api.chui.ai/v1/collection"
count = 0

with open('../data/wiki.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        filename = '../data/wiki/'
        image_data = {
            "img0": base64.b64encode(open(filename + row[1], 'rb').read()),
            "name": row[0]
        }
        enroll_response = requests.post(enroll_url, data=json.dumps(image_data), headers=headers)
        enroll_response = enroll_response.json()
        print enroll_response
        if enroll_response['message'] != u'No face detected !':
            update_collection_data = {
                "enrollment_id": enroll_response['data']['enrollment_id'],
                "collection_id": collection_id,
            }
            collection_response = requests.put(update_collection_url, data=json.dumps(update_collection_data),
                                               headers=headers)
            print collection_response.json()
            sleep(0.5)
            count += 1

        if count == 2:
            break

# training

training_url = "https://api.chui.ai/v1/train"
data = {
    "collection_id": collection_id
}
training_response = requests.post(training_url, data=json.dumps(data), headers=headers)
print training_response.json()

sleep(15)

identify_url = "https://api.chui.ai/v1/identify"

data = {
    "img": base64.b64encode(open('mrauch.jpg', 'rb').read()),
    "collection_id": collection_id
}

identify_response = requests.post(identify_url, data=json.dumps(data), headers=headers)

print identify_response.json()

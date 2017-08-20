# Adding the first profile
import requests
import base64
import json
import csv
from time import sleep


collection_id = "ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMDjsKkJDA"
start_count  = 81
final_count = 160

# Adding the first profile
headers = {
    "x-api-key": "k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
    "Content-Type": "application/json",
}

enroll_url = "https://api.chui.ai/v1/enroll"
update_collection_url = "https://api.chui.ai/v1/collection"
count  = 0

with open('data/wiki.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if count >= start_count and count <= final_count:
            filename = 'data/wiki/'
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
        elif count > final_count :
            break
        else:
            count += 1



# training

training_url = "https://api.chui.ai/v1/train"
data = {
    "collection_id": collection_id
}
training_response = requests.post(training_url, data=json.dumps(data), headers=headers)
print training_response.json()

sleep(15)
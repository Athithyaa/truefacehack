import httplib, urllib, base64, json
import urllib
import csv
headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
    'Ocp-Apim-Subscription-Key': '94e6fcf4707944ae829634493cfe1ecd',
}


file_count = 0
file_location = '../data/wiki_new/'

writer=csv.writer(open(file_location+"wiki_new.csv",'wb'))

with open('../data/wiki.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:

        if file_count < 25:  
            celeb_details = []     
            celebrity_name = row[0]
            file_count = file_count + 1
            celeb_details.append(celebrity_name)


            params = urllib.urlencode({
                # Request parameters
                'q': celebrity_name,
            })

            try:
                count = 0

                conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
                conn.request("POST", "/bing/v5.0/images/search?%s" % params, "{body}", headers)
                response = conn.getresponse()
                data = json.loads(response.read())
                for links in data['value']:
                    print(links['thumbnailUrl'])
                    filename =  "pics/"+ celebrity_name+str(count)+".jpg"
                    if count < 5:
                        celeb_details.append(filename)
                        urllib.urlretrieve(links['thumbnailUrl'], "../data/pics/"+ celebrity_name+str(count)+".jpg")
                        count = count + 1
                writer.writerow(celeb_details)
                conn.close()
            except Exception as e:
                print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
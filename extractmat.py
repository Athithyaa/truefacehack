import scipy.io as sio
import csv

matdata = sio.loadmat('data/wiki.mat')
dlen = len(matdata['wiki']['name'][0][0][0])

with open('data/wiki.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    for i in range(0, dlen):
        if (len(matdata['wiki']['name'][0][0][0][i]) > 0) and (len(matdata['wiki']['full_path'][0][0][0][i]) > 0):
            csvwriter.writerow([matdata['wiki']['name'][0][0][0][i][0].encode('utf-8'),
                             matdata['wiki']['full_path'][0][0][0][i][0].encode('utf-8')])


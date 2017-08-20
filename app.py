import json
import logging

import base64
import os
import random
import requests
from flask import Flask, render_template, request
from logging import Formatter, FileHandler
from pytube import YouTube
from time import sleep
import urllib
import cv2
import os

from forms import *

app = Flask(__name__)

app.config.from_object('config')

def readPoster(poster_url):
    path = 'static/img/poster.jpg'

    try:
        os.remove(path)
    except OSError:
        pass
    except IOError:
        pass
    urllib.urlretrieve(poster_url, "static/img/poster.jpg")



    headers = {
        "x-api-key": "k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
        "Content-Type": "application/json",
    }


    url = "https://api.chui.ai/v1/identify"

    data = {
        "img":base64.b64encode(open('static/img/poster.jpg','rb').read()),
        "collection_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgKDK6OEJDA"
    }

    r  = requests.post(url,data=json.dumps(data),headers=headers)
    name = r.json()

    headers = {
        "x-api-key": "k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
        "Content-Type": "image/jpeg",

    }

    url = "https://api.chui.ai/v1/facedetect"

    r = requests.post(url, data=open(path, 'rb').read(), headers=headers)

    data = r.json()
    count = 0
    img = cv2.imread(path)
    try:
        for face in data['faces']:
            x1 = int(face['bounding_box'][0])
            x2 = int(face['bounding_box'][1])
            y1 = int(face['bounding_box'][2])
            y2 = int(face['bounding_box'][3])

            cv2.putText(img, name['data'][count]['name'], (x1 + 10, x2 - 10), 0, 1, (0, 255, 0))
            cv2.rectangle(img, (x1, x2), (y1, y2), (0, 255, 0), 2)
            cv2.imwrite(path, img)
            count += 1
    except:
        pass
    return path

def scandirs(path):
    for root, dirs, files in os.walk(path):
        for currentFile in files:
            print "processing file: " + currentFile
            exts = ('.png', '.jpg')
            if any(currentFile.lower().endswith(ext) for ext in exts):
                os.remove(os.path.join(root, currentFile))

def readVideo(you_url):
    yt = YouTube(you_url)
    framesPersecond = 100

    yt.set_filename('vid1')
    size = len(yt.get_videos())
    if size > 1:
        video = yt.get_videos()[size - 2]
    else:
        video = yt.get_videos()[0]

    try:
        scandirs('tmp/')
    except OSError:
        pass

    try:
        os.remove('static/img/1.jpg')
        os.remove('static/img/2.jpg')
        os.remove('static/img/3.jpg')
    except OSError:
        pass

    try:
        os.remove('tmp/vid1.mp4')
    except OSError:
        pass

    video.download('tmp/')

    import cv2

    vidcap = cv2.VideoCapture('tmp/vid1.mp4')
    success, image = vidcap.read()
    count = 0
    success = True
    while success:
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        if count % framesPersecond == 0:
            cv2.imwrite("tmp/frame%d.jpg" % count, image)  # save frame as JPEG file
        count += 1

    # Creating a collection
    headers = {
        "x-api-key": "k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
        "Content-Type": "application/json",
    }

    id_url = "https://api.chui.ai/v1/identify"

    temp_index = []
    success_path = []
    for i in range(count):
        if i % framesPersecond == 0:
            temp_index.append(i)

    for i in range(len(temp_index)):
        t = temp_index[i]
        headers = {
            "x-api-key": "k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
            "Content-Type": "application/json",
        }

        id_data = {
            "img": base64.b64encode(open('tmp/frame' + str(t) + '.jpg', 'rb').read()),
            "collection_id": "ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgKDK6OEJDA"
        }

        r = requests.post(id_url, data=json.dumps(id_data), headers=headers)

        name = r.json()

        path = 'tmp/frame' + str(t) + '.jpg'

        headers = {
            "x-api-key": "k9smH5hhw3J2joOc6cIv8TO5t8iudeI3llnr34D2",
            "Content-Type": "image/jpeg",
        }

        url = "https://api.chui.ai/v1/facedetect"

        r = requests.post(url, data=open(path, 'rb').read(), headers=headers)

        data = r.json()
        # print name,path

        try:
            img = cv2.imread(path)
            count = 0
            for face in data['faces']:
                x1 = int(face['bounding_box'][0])
                x2 = int(face['bounding_box'][1])
                y1 = int(face['bounding_box'][2])
                y2 = int(face['bounding_box'][3])

                cv2.putText(img, name['data'][count]['name'], (x1 + 10, x2 - 10), 0, 1, (0, 255, 0))
                cv2.rectangle(img, (x1, x2), (y1, y2), (0, 255, 0), 2)
                cv2.imwrite(path, img)
                count += 1
                success_path.append(path)
        except KeyError:
            continue
    ind = 1
    if len(success_path) < 3:
        for item in success_path:
            img = cv2.imread(item)
            cv2.imwrite("static/img/" + str(ind) + ".jpg", img)
            ind += 1
    else:
        ind2 = 1
        success_items = random.sample(range(1, len(success_path)), 3)
        for item in success_items:
            img = cv2.imread(success_path[item])
            cv2.imwrite("static/img/" + str(ind2) + ".jpg", img)
            ind2 += 1


@app.route('/', methods=['GET', 'POST'])
def home():
    form = HomeForm(request.form)
    images = ['/static/img/obama1.png', '/static/img/obama1.png', '/static/img/obama1.png']
    if request.method == 'POST':
        youtubelink = form.name.data
        readVideo(youtubelink)
        images = ['/static/img/1.jpg', '/static/img/2.jpg', '/static/img/3.jpg']
        return render_template('forms/home.html', form=form, images=images)
    return render_template('forms/home.html', form=form, images=images)


@app.route('/poster', methods=['GET', 'POST'])
def poster():
    form = PosterForm(request.form)
    images = ['/static/img/obama1.png']
    if request.method == 'POST':
        posterlink = form.name.data
        readPoster(posterlink)
        images = ['/static/img/poster.jpg']
        return render_template('forms/poster.html', form=form, images=images)
    return render_template('forms/poster.html', form=form, images=images)


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')

    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

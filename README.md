How to Run
The entire thing is flask. Install all the dependecies (pyTube, openCV, Flask)

Run the code python app.py

For questions/suggestions and issues. Contact any of the contributors.

Inspiration
We have always been interested in breaking down every teaser for game of thrones. But sometimes, it is very difficult to identify every character that appears on the teaser. By using Trueface now we can know!!!

Alternatively, when we were building the website, we are very much aware about the captcha system as extra layer of security to avoid spammers, web crawlers and robots. But just take a look at this -> https://www.youtube.com/watch?v=MADwrNfX_tQ

What it does
You can search youtube videos for popular celebrities. You can also search any picture in the internet as well!

How we built it
The front end was Flask (we used Python a lot!!!!!! So we preferred. ) The backend was powered by Trueface API. For training images we used Bing Search from RAPID API marketplace and also OpenCV to draw text and rectangles.

Challenges we ran into
There was few bugs in the API that we ran into. Some solved, some still present. We initially tried training 63000 celebrities from the WIKI dataset. However, the API will not support multiple calls and crashes with a Multiple requests error or Deadline Exceeded error.

When training with more than 5 images randomly available from the Internet, The API returns Deadline exceeded error and was temporarily fixed by replacing it with a different image.

Accomplishments that we're proud of
The code works perfectly (still slow though)

What we learned
Using Trueface.ai. It is an amazing API and with proper training set it performs really well.

What's next for truefacehack
Train better with more training images.

Contribute/Help fix bugs in Trueface.AI

Built With
python
css
html
javascript
flask
trueface
youtube
opencv
rapidapi
bing-search-api

# Spotify Scraper Webapp
### https://spotify-fire.herokuapp.com/
### This tool uses the spotify api alongside the genius api to allow users to search for any artist and will show a random song by that artist, as well as a a sample of the song , the lyrics of the song, as well as a hyperlink that will show you similar songs. A user can also click on the image to link to the full song on spotify
## Technologies Used
##### Python, HTML, CSS, AWS Cloud 9, Heroku, Github
## Libraries Used
##### OS, Random, Spotipy
## Frameworks Used
##### Flask
## APIs Used
##### Spotify, Genius
## Steps to set up this application
##### 1. Clone the repository with the following link: https://github.com/NJIT-CS490-SP21/project1-trp35.git
##### 2. run ```pip install -r requirements.txt ``` to install all necessary python packages for the application to run properly
##### 3. Set up Spotify Developer account with https://developer.spotify.com/documentation/web-api/quick-start/
##### 4. Once you obtain the proper authorization credentials, create a .env file within the main directory and export those credentials there. (i.e. ```export SPOTIPY_CLIENT_ID='TOKEN'```)
##### 5. Set up Genius credentials using https://genius.com/api-clients and sign up for an api to get a client access token and then add that to the .env file as well (i.e ```export GENIUS_ACCESS_TOKEN='TOKEN'```)
##### 6. Run ```python app.py``` on the Cloud 9 terminal and preview the application.
##### 7. The site is also running running on Heroku @ https://spotify-fire.herokuapp.com/
## a. What are at least 3 technical issues you encountered with your project? How did you fix them?
##### 1. While working on deploying my code with Flask, I ran into multiple errors. The first being that once I created my app on Heroku, I was having trouble actually deploying my code on the app. After more research I was able to find this link, https://stackabuse.com/deploying-a-flask-application-to-heroku/. Where it gave more flask related steps to deploying, so from there I was able to successfully deploy my app. The next issue I ran into this was with deploying any changes I made. Using "git push heroku master" was not working and was throwing various errors. After more research, I found a command on stackOverflow "git push heroku HEAD:master" that resolved this issue for me.
##### 2. Ran into issue authorizing spotipy while deploying to heroku. I was getting authorization errors when the app was deployed to heroku, but after more research, I learned about config vars in heroku using https://devcenter.heroku.com/articles/config-vars and set them using the Heroku dashboard.
##### 3. Initializing git, when I tried using git on my project, it wouldn't let me use my actual password as the password, so after doing some more research, I found https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token. I learned that to get over this problem, I needed to set a personal access token on github, which provided a token which I used for my pasword instead.
##### 4. My website has functionality where you can search for any artist and in that I ran into technical issues with how to get that information passed from html to flask. I found https://www.askpython.com/python-modules/flask/flask-forms through research and learned how to use GET and POST with forms to pass data to the backend and use that as input data with the spotipy API
##### 5. Another techincal issue I ran into was regarding how to href to local pages within my templates directory. I found the documentation for url_for and realized that the parameter passed is the name of the method in app.py and not the app.route.
##### 6. One technical issue I ran into was when searching for uncommon artists or artists that did not exist on Spotify, I would get lots of different eerrors regarding getting top tracks as well as the hyperlink to the genius lyrics. To overcome this issue, I made an html page designed for errors that states that certain info could not be found. I used various if statements to do checks on whether certain data was there and if it was not then I would redirect to that error page.
##### 7. Another technical issue I had was with the Spotify logo I put at the top of all my pages. I would use the url to display the image, but sometimes the logo would not appear randomly. To overcome this issue, I simply downloaded the image and uploaded it into the static directory and called it from there so I could load it locally, and avoid this issue.
##### 8. Lastly, one thing I had a technical issue with was having my album cover image as a hyperlink. Initially, my image was centered and the entire webpage where the image was would be they hyperlink which was an issue because a lot of times I would accidentally click on it. But after looking at https://stackoverflow.com/questions/29978500/only-make-a-centered-image-a-link-instead-of-the-whole-parent-div I realized that I have to display the image as an inline rather than a block, so that the hyperlink would only apply to the image.
## b. What are known problems, if any, with your project? 
##### Certain audios do not have any preview url given, but my website still shows the audio media player without anything to play.
## c. What would you do to improve your project in the future? 
##### To improve my project, I would try to include more visuals or graphics as the layout of the website is simple right now. I would also like to reformat the way my similar tracks page looks, as it just lists the 5 songs with hyperlinks without any other graphics. I also think it would be interesting to add the functionality that it always produces a random artist, rather than hard coding a list of my favorite artists.
##### Another thing I would like to improve my project would be with adding additional features such as displaying a youtube video of the song or displaying more information about an artist such as the number of streams they have.
##### I would also like to consider incorporating JavaScript into my project to make things more interactive and dynamic because currently to update the website with one of my favorite artists you have to refresh the page, but if there was a button or textbox that would update as I typed in a name, that would be interesting

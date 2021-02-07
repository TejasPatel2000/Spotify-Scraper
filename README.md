# project1-trp
Project 1
## Technologies Used
###### Python, HTML, CSS, AWS Cloud 9, Heroku, Github
## Libraries Used
###### OS, Random, Spotipy
## Frameworks Used
###### Flask
## APIs Used
###### Spotify
## Steps to set up this application
###### 1. Clone the repository with https://github.com/NJIT-CS490-SP21/project1-trp35.git
###### 2. run ```python pip install -r requirements.txt ```
###### 3. Set up Spotify Developer account with https://developer.spotify.com/documentation/web-api/quick-start/
###### 4. Once you obtain the proper authorization credentials, create a .env folder within the main directory and export those credentials there.
###### 5. Run ```python python app.py``` on the Cloud 9 terminal and preview the application. (Or you could view on Heroku, but that was not required for milestone 1, so I will be adding those instructions later) 
## a. What are at least 3 technical issues you encountered with your project? How did you fix them?
###### 1. While working on deploying my code with Flask, I ran into multiple errors. The first being that once I created my app on Heroku, I was having trouble actually deploying my code on the app. After more research I was able to find this link, https://stackabuse.com/deploying-a-flask-application-to-heroku/. Where it gave more flask related steps to deploying, so from there I was able to successfully deploy my app. The next issue I ran into this was with deploying any changes I made. Using "git push heroku master" was not working and was throwing various errors. After more research, I found a command on stackOverflow "git push heroku HEAD:master" that resolved this issue for me.
###### 2. Ran into issue authorizing spotipy while deploying to heroku. I was getting authorization errors when the app was deployed to heroku, but after more research, I learned about config vars in heroku using https://devcenter.heroku.com/articles/config-vars and set them using the Heroku dashboard.
###### 3. Initializing git, when I tried using git on my project, it wouldn't let me use my actual password as the password, so after doing some more research, I found https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token. I learned that to get over this problem, I needed to set a personal access token on github, which provided a token which I used for my pasword instead.
###### 4. My website has functionality where you can search for any artist and in that I ran into technical issues with how to get that information passed from html to flask. I found https://www.askpython.com/python-modules/flask/flask-forms through research and learned how to use GET and POST with forms to pass data to the backend and use that as input data with the spotipy API
###### 5. Another techincal issue I ran into was regarding how to href to local pages within my templates directory. I found the documentation for url_for and realized that the parameter passed is the name of the method in app.py and not the app.route.
## b. What are known problems, if any, with your project? 
###### Sometimes the Spotify Logo I put in the top left header does not load for some reason. Most of the time it works though, so I am still working on getting that functionality. A potential solution that I am going to implement is that I just download the image and keep it locally within one of my directories that way it always loads.
###### Another known issue is that when you search for an artist and the name does not exist, it throws an error, so something I would do to fix that would be that if there are no results for that artist than I would display my own 404 error page so it looks nicer, and could have more functionality, like just redirecting back to the home page.
## c. What would you do to improve your project in the future? 
###### To improve my project, I would try to include more visuals or graphics as the layout of the website is simple right now. I would also like to reformat the way my similar tracks page looks, as it just lists the 5 songs with hyperlinks without any other graphics. I also think it would be interesting to add the functionality that it always produces a random artist, rather than hard coding a list of my favorite artists.

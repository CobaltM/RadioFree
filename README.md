
# Project Description
A web music streaming service which broadcasts a host’s music to be synchronously listened to by providing a website link to their "room". The website includes embedded links to music playlists . When people visit the room, they are synced to the playlist. 
The website will also have a database of users storing their relation to other users including friends and statistics on the user.
This application allows users to share and analyze their music in a live format and fills an unfilled niche of users, such as those who wish to feel as though they’re listening to a record at home with their closest friends with the convenience the internet can offer.

This project aims to provide users with a social media infused way to share their favorite songs and playlists.  Listeners will be able to chat with one another and broadcast their own playlists to their friends while they are using other social media elements.


# Installing server
## Prerequisite software 
### Install a locally hosted mysql server
#### windows
http://www.wampserver.com/en/ 
#### mac
https://www.mamp.info/en/downloads/
#### linux
https://bitnami.com/stack/lamp/installer 
#### optionally download mysql workbench to help use your server
https://dev.mysql.com/downloads/workbench/ 
####
if possible host it on port 3306 with root as username and no password
### Install the most recent version of python 2.7
https://www.python.org/getit/ 
### Install the most recent version of node js
https://nodejs.org/en/download/ 
### clone our github repository and unzip it 
https://github.com/CobaltM/RadioFree/tree/Development?files=1 
# File setup
## MySql server setup
1. create a databasue named “radiofreedatabase”
2. from the “validation_and_testing” directory of the cloned github repository 
3. open the .sql script 
4. copy and run its contents into a script in the new database 
5. if necessary configure “cfgconnection.py” under python_scripts, registration directory to match your database server  connections 
6. changing the macos value to true automatically configures for mamp servers 
## edit app.js in the unzipped repository and change the value of pythonPath on line 13 to the location of your python executable file 
# Starting the server
create a terminal/cmd prompt from the unzipped repository directory 
## run the following commands 
pip install mysql-connector 
##### for mac/linux run “sudo pip install mysql-connector” 
node app.js
# the website should be locally accessible at localhost:3000 from your internet browser


# Our Team
## Ethan Caldwell
### Team Leader
Highly flexible programmer with background in both teaching programming and researching social media data.  Have a background in mathematics including optimization and linear programming which coupled with another brief research project experience has made me a highly capable computer scientist specifically in regard to algorithmic studies. I hope that my accolades will allow me to provide valuable insight into our architectural design of our project.




## Paul Trimor
### Principal Programmer
I have over 4 years of experience working with database management systems. In 2015, I was hired as a technical assistant for a data analytics company, “Data Profits”. My main responsibilities was to develop and maintain a Wordpress website along with debugging SQL code and working with Microsoft SQL Server suite. Afterwards, was hired at AMAC Research at Georgia Tech as a student programmer. At AMAC, I write javascript and php scripts to help basic business operations. I will graduate with a degree in computer science December 2018. 

## Princeton Nelson
### Principal Programmer
Princeton has an Associate of Computer Science from Atlanta Metropolitan College and is currently pursuing a Bachelors of Computer Science. Princeton has experience working with Django and AngularJS. He has had 2.5 years experience working for JTE Technologies where he designed the software system using modern web frameworks.Princeton has also worked as a Software Engineer where he has employed front-end and backend skills.
 
## Hao Nguyen
### Front End Developer
For the summer of 2017, I joined a research program under Dr. Ashwin Ashok. I was responsible to test the sweat production and nerve reaction with Grove GSR and organized the data with Excel. The main goal of the project was exploring the idea of music therapy in medical treatment, and our approaches were building a test model, testing on ourselves, and collecting data for the musical diagnosis on how different types of music could affect on an individual’s nervous system. Afterward, I have some mining experience through data mining projects. Through Data Mining class at GSU, I explored mining techniques with python, R, and Matlab to forecast the future crime rates of Chicago in 5 years using past crime rates. I chose to retake Data Mining in Hong Kong to explore the different approach. The project was mainly using Weka and applying multiple mining techniques to analyze the SAS healthcare data.



## Tim Harrison
### Analyst
Tim has Bachelors of Science in Physics from Georgia Tech. He has experience in working inside a laboratory conducting experiments and writing lab reports. In addition, Tim also has mathematical and statistical knowledge and programming skills. He has worked in various computing projects. Tim is a seasoned world traveler. 

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
1. create a database named “radiofreedatabase”
2. from the “validation_and_testing” directory of the cloned github repository 
3. open the .sql script 
4. copy and run its contents into a script in the new database 
5. if necessary configure “cfgconnection.py” under python_scripts, registration directory to match your database server  connections 
6. changing the macos value to true automatically configures for mamp servers 
7. edit app.js in the unzipped repository and change the value of pythonPath on line h14 to the location of your python executable file 
# Starting the server
create a terminal/cmd prompt from the unzipped repository directory /
## run the following commands /
pip install mysql-connector /
##### for mac/linux run “sudo pip install mysql-connector” /
node app.js
# the website should be locally accessible at localhost:3000 from your internet browser

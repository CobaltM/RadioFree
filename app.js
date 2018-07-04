var express = require('express');
var app = express();
var path    = require("path");
var PythonShell = require('python-shell');

var options = {
  mode: 'text',
  pythonPath: 'C:/Python27/python.exe',
  pythonOptions: ['-u'],
};
//these don't matter yet, and are subject to change, but will be helpful later
 

app.use(express.static("public"));


app.get('/', function (req, res) {
 res.sendFile(path.join(__dirname+'/HTML forms/login.html'));
})
app.get('/register', function (req, res) {
 res.sendFile(path.join(__dirname+'/HTML forms/userRegister.html'));
})
app.post('/', function(req,res){
	
	res.redirect(307,'/register');







})
var server = app.listen(3000, function () {
 var host = server.address().address
 var port = server.address().port
 console.log("Example app listening at http://%s:%s", host, port)
})
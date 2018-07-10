var express = require('express');
var app = express();
var path    = require("path");
var PythonShell = require('python-shell');

var options = {
  mode: 'text',
  pythonPath: 'C:/Python27/python.exe',
  pythonOptions: ['-u'],
  scriptPath: path.join(__dirname+'/registrar')
};
//these don't matter yet, and are subject to change, but will be helpful later
 

app.use(express.static("public"));


app.get('/', function (req, res) {
 res.sendFile(path.join(__dirname+'/HTML forms/login.html'));
 console.log(Validation('username','password!1A'));
 
})
app.get('/register', function (req, res) {
 res.sendFile(path.join(__dirname+'/HTML forms/userRegister.html'));
})
app.post('/', function(req,res){
	
	res.redirect(307,'/register');







})
app.get('/member',function(req,res){
	res.sendFile(path.join(__dirname+'/HTML forms/memberPage.html'));
})
app.post('/register',function(req,res){
	console.log('post successful');
	if(Validation(req.body.registerBox.username,req.body.registerBox.password)){
		res.redirect(307,'/member');
	}
})
var server = app.listen(3000, function () {
 var host = server.address().address
 var port = server.address().port
 console.log("Example app listening at http://%s:%s", host, port)
})



function Validation(un,pw){
	options.args=[un,pw];
	var pshel = new PythonShell('/Registration.py',options);
	pshel.on('message',function(message){
		test=message[0];
		if(test=="3"){
			console.log('passes!');
		}
		else{
			console.log('fails!');
		}
});
}
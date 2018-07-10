var express = require('express');
var app = express();
var path    = require("path");
var bodyParser     = require("body-parser");
var PythonShell = require('python-shell');
var valid;

var options = {
  mode: 'text',
  pythonPath: 'C:/Python27/python.exe',
  pythonOptions: ['-u'],
  scriptPath: path.join(__dirname+'/registrar')
};
//these don't matter yet, and are subject to change, but will be helpful later
 

app.use(express.static("public"));
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

app.get('/', function (req, res) {
 res.sendFile(path.join(__dirname+'/HTML forms/login.html'));
 //Validation('username','password!1A');
 
})
app.get('/register', function (req, res) {
 res.sendFile(path.join(__dirname+'/HTML forms/userRegister.html'));
})
app.post('/', function(req,res){
	res.redirect(307,'/register');
})
app.post('/member',function(req,res){
	res.sendFile(path.join(__dirname+'/HTML forms/memberPage.html'));
})
app.post('/register',function(req,res){
	console.log('post successful');
	un=req.body.user;
	console.log(un);
	pw=req.body.pass;
	console.log(pw);
	options.args=[un,pw];
	PythonShell.run('/Registration.py',options,function(err,results){
		if(err) throw err;
		console.log(results);
		if(ValidationReg(results)){
			PythonShell.run('/addUser.py',options,function(err,result){
				if(err) throw err;
				console.log(result);
			});
			res.redirect(307,'/member');
		}
		else{
			//put notification
		}
	});
})
app.post('/login',function(req,res){
	console.log('post successful');
	un=req.body.username;
	console.log(un);
	pw=req.body.password;
	console.log(pw);
	options.args=[un,pw];
	PythonShell.run('/Login.py',options,function(err,results){
		if(err) throw err;
		console.log(results);
		if(ValidationLog(results)){
			res.redirect(307,'/member');
		}
	});
		
})
var server = app.listen(3000, function () {
 var host = server.address().address
 var port = server.address().port
 console.log("Example app listening at http://%s:%s", host, port)
})


function ValidationReg(mess){
	test=mess[0];
		if(test=="3"){
			console.log('passes!');
			return true;
		}
		else{
			console.log('fails!');
			return false;
		}
}
function ValidationLog(mess){
	test=mess[0];
	if(test=="1"){
		console.log('passes!');
		return true;
	}
	else{
			console.log('fails!');
			return false;
		}
}
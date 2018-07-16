var express = require('express');
var app = express();
var path    = require("path");
var bodyParser     = require("body-parser");
var PythonShell = require('python-shell');
var valid;

var options = {
  mode: 'text',
  pythonPath: 'C:/python27/python.exe',
  pythonOptions: ['-u'],
  scriptPath: path.join(__dirname+'/python_scripts')
};

/* Server Routing Section */

app.use(express.static("public"));

app.use(bodyParser.urlencoded({
    extended: true
}));

app.use(bodyParser.json());

// GET Request 

app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname+'/HTML_forms/login.html'));
    //Validation('username','password!1A'); 
})

app.get('/register', function (req, res) {
    res.sendFile(path.join(__dirname+'/HTML_forms/userRegister.html'));
})

// Creating a room 
app.get('/createRoom', function(req, res) {
	res.sendFile(path.join(__dirname+'/HTML_forms/createRoom.html'));
	PythonShell.run('/room/addRoom.py', options, function(err, results) {
		
	})
})

// Get unique Room 
app.get('/broadcasting-*', function(req, res) {

	var userId = req.params[0];
	console.log(userId);

	res.sendFile(path.join(__dirname)+'/HTML_forms/roomPage.html');

});

// Post Request

app.post('/', function(req,res){
    res.redirect(307,'/register');
})

app.post('/member', function(req,res){
    res.sendFile(path.join(__dirname+'/HTML_forms/memberPage.html'));
})

app.post('/register',function(req,res){	

    un=req.body.user;	
    pw=req.body.pass;	
    var ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
	
	console.log(ip);
    console.log('post successful');
    console.log(pw);
    console.log(un);

    options.args=[un,pw,ip];

    PythonShell.run('/registrar/Registration.py', options, function(err,results){    	
    	if(err) throw err; 
    	console.log(results);		
		if(ValidationReg(results)){
			PythonShell.run('/registrar/addUser.py', options,function(err,result){
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

	un=req.body.username;
	pw=req.body.password;

    console.log('post successful');	
	console.log(un);
	console.log(pw);

	options.args=[un,pw];
	
	PythonShell.run('/registrar/Login.py',options,function(err,results){		
		if(err) throw err;		
		console.log(results);
		if(ValidationLog(results)){		
			res.redirect(307,'/member');
		}
	});
			
})

app.post('/createRoom', function(req, res) {
	
	// Get and Process Form data 
	var eggs = req.body; 
	console.log(eggs);
	res.sendFile(path.join(__dirname+'/HTML_forms/createRoom.html'));
	PythonShell.run('/room/addRoom.py', options, function(err, results) {
		
	})

	// Execute Database command to save to database get 
	PythonShell.run('/room/createRoom.py/', options, function(err, results){
		if (err) throw err; 
		console.log(results); 



	})


})


/* Server Configuration Section */ 

var server = app.listen(3000, function () {
	var host = server.address().address
	var port = server.address().port
	console.log("Example app listening at http://%s:%s", host, port)
}); 
/* Python output interpreters */
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
var express = require('express');
var app = express();
var path    = require("path");
var bodyParser     = require("body-parser");
var cookieParser = require('cookie-parser'); 
var socket = require('socket.io');
var PythonShell = require('python-shell');
var valid;


var options = {
  mode: 'text',
  pythonPath: 'C:/python27/python.exe', 
  pythonOptions: ['-u'],
  scriptPath: path.join(__dirname+'/python_scripts')
};

/* Server Routing Section */
app.use(cookieParser());
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
	res.redirect('/room');
})

// Get unique Room 
app.get('/broadcasting-*', function(req, res) {

	var userId = req.params[0];
	console.log(userId);

	res.redirect('/room/');

});
app.use('/broadcasting-*/script.js',function(req,res){
	res.sendFile(path.join(__dirname+'/public/script.js'));
});
app.use('/broadcasting-*/styleRoomPage.css',function(req,res){
	res.sendFile(path.join(__dirname+'/public/styleRoomPage.css'));
});
app.get('/room/',function(req,res) {
	res.sendFile(path.join(__dirname+'/HTML_forms/roomPage.html'));
// Post Request
});
app.use('/room/script.js',function(req,res){
	res.sendFile(path.join(__dirname+'/public/script.js'));
});
app.use('/room/styleRoomPage.css',function(req,res){
	res.sendFile(path.join(__dirname+'/public/styleRoomPage.css'));
});
app.get('/room/logo.png',function(req,res){
	res.sendFile(path.join(__dirname+'/public/logo.png'));
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

	// Set the username in the cookie to be used again. 
	res.cookie('username', un);
				
	PythonShell.run('/registrar/Login.py',options, function(err,results){		
		if(err) throw err;		
		console.log(results);
		if(ValidationLog(results)){		
			res.redirect(307,'/member');
		} else {
			
		}
	});
			
})

app.post('/createRoom', function(req, res) {
	console.log("POST CREATE ROOM");
	// Get and Process Form data 
	res.sendFile(path.join(__dirname+'/HTML_forms/createRoom.html'));

		console.log("request object" + req); 
		console.log("Request body" + req.body);
		console.log("user name: " + req.cookies);

		// Get the values to be inserted in room with Python 
		var username = "white"; 
		var roomname = req.body[0];
		var maxListeners = req.body[1];
		var spotifyURI= req.body[2];
		var description= req.body[3];

		options.args = [username, roomname, maxListeners, spotifyURI, description];

		PythonShell.run('/room/addRoom.py', options, function(err, results) {
			if(err) throw err;		
				console.log(results);

		})

})


/* Server Configuration Section */ 

var server = app.listen(3000, function () {
	var host = server.address().address
	var port = server.address().port
	console.log("Example app listening at http://%s:%s", host, port)
}); 




var io = socket(server);

io.on('connection',function(socket){
	console.log('test',socket.id);
	socket.on('chat',function(data){
		io.sockets.emit('chat',data);
	});
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
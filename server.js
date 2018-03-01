var express = require('express');
var app = express();
var bodyParser     = require("body-parser");
var path    = require("path");
var dateformat = require('dateformat');
var isValidDate = require('is-valid-date');
var PythonShell = require('python-shell');

var options = {
  mode: 'text',
  pythonPath: 'C:/Python27/python.exe',
  pythonOptions: ['-u'],
  scriptPath: 'C:/Users/ethan/Desktop/server/resources',
  args: ["-q","Ferrets","-d","data","-t2","Thu Jan 25 00:00:00 +0000 2018"]
};
 

app.use(express.static("public"));


app.get('/', function (req, res) {
 res.sendFile(path.join(__dirname+'/proto2.html'));
})

app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

app.post('/', function(req,res){
	if(Validation(req.body.hashtagname,req.body.startdate,req.body.enddate)){
		options.args=transform(req.body.hashtagname,req.body.startdate,req.body.enddate);
	}
	//console.log(options.args);
	PythonShell.run('tweepy_download.py', options, function (err, results) {
 		if (err) throw err;
 			 console.log('results: %j', results);
});







})
var server = app.listen(3000, function () {
 var host = server.address().address
 var port = server.address().port
 console.log("Example app listening at http://%s:%s", host, port)
})









function Validation(ht,sd,ed){
			
			var htrx = /(#?\w+){1}(,#?\w+)*$/;
			ret=true;
			if(htrx.test(ht)==false){
				return false;
			}
			if(isValidDate(sd)==false&&sd!=""){
				return false;
			}
			if(isValidDate(ed)==false&&ed!=""){
				return false;
			}
			return true;
		}


function transform(ht,sd,ed){
			var start1="",start2="",end1="",end2 = "";
			var s,sp;
			if(sd!=""){
				start1="-t1";
				sp=sd.split("/");
				s=sp[1]+"/"+sp[0]+"/"+sp[2];
				start2=dateformat(s,"ddd mmm dd ")+"00:00:00 +0000 "+dateformat(s,"yyyy");
			}
			if(ed!=""){
				end1="-t2";
				sp=ed.split("/");
				s=sp[1]+"/"+sp[0]+"/"+sp[2];
				end2=dateformat(s,"ddd mmm dd ")+"00:00:00 +0000 "+dateformat(s,"yyyy");
			}
			var ret=["-q",ht,"-d","data",start1,start2,end1,end2];

			return(ret);
		}
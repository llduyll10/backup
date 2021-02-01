var env = process.env.NODE_ENV;


var express = require('express');
var http = require('http');
var logger = require('morgan');
var passport  = require('passport');
var config = require(__dirname +'./config/database');
var mongoose = require('mongoose');

var path = require('path');
var handlebars  = require('express-handlebars');

var session = require('express-session')
var bodyParser = require('body-parser');
var cookieParser = require('cookie-parser');
var fs = require('fs')

var cors = require('cors')
// conect database
mongoose.connect(config.database);

var app = express();
app.use(cors());

// create a write stream (in append mode)
app.use(logger('dev'));
var accessLogStream = fs.createWriteStream(__dirname + '/access.log', {flags: 'a'})
app.use(logger('combined', {stream: accessLogStream}))

// body parser 
app.use(cookieParser());
app.use(bodyParser.json({limit: '2mb'}) );
app.use(bodyParser.urlencoded({
  limit: '2mb',
  extended: true,
  parameterLimit:30
}));

app.use(passport.initialize());
app.use(passport.session());
require('./config/passport')(passport)

app.set('views', path.resolve(__dirname, 'views'));
var hbs = handlebars.create({
   defaultLayout: 'main'
});
app.engine('handlebars', hbs.engine);
app.set('view engine', 'handlebars');

// add route to app
var server = http.createServer(app);
fs.readdirSync('./controllers').forEach(function (controller) {
  if(controller.substr(-3) === '.js') {
    var routeApi = require('./controllers/' + controller);
    routeApi(app); //Pass it here
  }
});

// handel not found route
app.use(function(req,res){
    res.status(200).send({success: false, msg: 'Route not found.'});
 });

 // set port
app.set('port', 9000);
// start server
server.listen(app.get('port'), function(){
  console.log('The App Store server listening on port ' + app.get('port') + ' and NODE_ENV: ' + env);
});
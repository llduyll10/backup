var env = process.env.NODE_ENV

var express = require('express')
var http = require('http')
var path = require('path')

var config = require('./config/database');

var session = require('express-session')
var bodyParser = require('body-parser')
var fs = require('fs')


var mongoose = require('mongoose');
mongoose.connect(config.database, {useNewUrlParser:true, useUnifiedTopology:true, useCreateIndex:true});

var cors = require('cors')
const passport = require('passport')

var port = 3000

var app = express()

app.use(cors())

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended:true}))

app.use(passport.initialize())
app.use(passport.session())
require('./config/passport')(passport)

//Add route to app
var server = http.createServer(app)
fs.readdirSync('./controllers').forEach(function(controller){
    if(controller.substr(-3) === '.js'){
        var routeApi = require('./controllers/' + controller)
        routeApi(app)
    }
})

app.set('port', port)


server.listen(app.get('port'), function(){
    console.log('App listening port ' + app.get('port'))
})
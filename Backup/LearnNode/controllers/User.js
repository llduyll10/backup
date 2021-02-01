var User = require('../models/User')
var jwt = require('jwt-simple')
var config = require('../config/database')
var bcrypt = require('bcrypt')
var message = require('../common/message')
module.exports = function(app, io){

    //Sign up
    app.post('/api/signup', makeSignUp)

    function makeSignUp(req, res){
        bcrypt.genSalt(10, function (err, salt) {
            if (err) {
                return res.json({ success: false, msg: err.message })
            }
            bcrypt.hash(req.body.password, salt, function (err, hash) {
                console.log('hash pwd')
                if (err) return res.json({ success: false, msg: err.message })
                else {
                    createUser(hash)
                }
            })
        })

        function createUser(password){
            User.findOne({
                email:req.body.email
            }).exec((function(err, user){
                if(user && user._id){
                    res.json({
                        success:false,
                        msg: 'Email is already exist'
                    })
                }
                else{
                    var obj = {
                        email: req.body.email,
                        username: req.body.username,
                        password: password
                    }
                    var newUser = new User(obj)
                    newUser.save(function(err, user){
                        if(err) return res.json({success:false, msg:err.message})
                        else return res.json({success:true, msg: message.create_sucess})
                    })
                }
            }))
        }
    }

    //Authenticate
    app.post('/api/login', login)
    function login(req, res){
        if(!req.body.email){
            res.status(200).send({success:false, msg:message.no_email})
        }
        else{
           User.findOne({email:req.body.email}).exec((function(err,user){
               if(user){
                   user.comparePassword(req.body.password, function(err, isMatch){
                       if(isMatch && !err){
                           var u = JSON.parse(JSON.stringify(user))
                           delete u.password
                           if(config.admin.includes(req.body.email)){
                               u.isAdmin = true
                           }
                           res.status(200).send({
                               success:true,
                               token: jwt.encode(u, config.secret),
                               user: u
                           })
                       }
                       else{
                           res.status(200).send({success:false, msg: message.pwd_error})
                       }
                   })
               }
               else{
                   res.status(200).send({success:false, msg: message.not_exist})
               }
           }))
        }
    }

}
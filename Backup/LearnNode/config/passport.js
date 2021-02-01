var JwtStrategy = require('passport-jwt').Strategy;
var ExtractJwt = require('passport-jwt').ExtractJwt;

var User = require('../models/User')
var config = require('../config/database')

module.exports = function(passport){
    var option = {}
    option.jwtFromRequest = ExtractJwt.fromAuthHeaderAsBearerToken();
    option.jwtFromRequest = ExtractJwt.versionOneCompatibility({ authScheme:'Token' });
    option.secretOrKey = config.secret;
    passport.use(new JwtStrategy(option, function(jwt_payload, done){
        User.findOne({_id: jwt_payload.id}, function(err, user){
            if(err){
                return done(err, false)
            }
            if(user){
                done(null, user)
            }
            else{
                done(null, false)
            }
        })
    }))
}
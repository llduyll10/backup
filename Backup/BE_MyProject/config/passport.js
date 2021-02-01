

var  JwtStrategy = require('passport-jwt').Strategy
var ExtractJwt = require('passport-jwt').ExtractJwt

var config = require(__dirname+'../config/database')
var User = require(__dirname+'../models/User')

module.exports = function(passport){
    var otps = {}
    otps.jwtFromRequest = ExtractJwt.fromAuthHeader()
    otps.jwtFromRequest = ExtractJwt.versionOneCompatibility({authSchema:'Token'})
    otps.secretOrKey = config.secret
    passport.use(new JwtStrategy(otps, function(jwt_payload,done){
        User.findOne({id:jwt_payload.id},function(err,user){
            if(err){
                return done(err,false)
            }
            if(user){
                done(null,user)
            }
            else{
                done(null,false)
            }
        })
    }))
}
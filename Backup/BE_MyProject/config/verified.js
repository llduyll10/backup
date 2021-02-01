var passport = require('passport')

module.exports = function(req, res, next){
    passport.authenticate('jwt',{session:false},(err,user,info,status)=>{
        console.log('hahaha',info)
        if(info){
            if (info.toString() === 'Error: No auth token') {
                return res.status(200).send({success: false, msg: 'Authentication failed. No auth token'});
            }
            if (info.message === 'invalid token' ) {
            	return res.status(200).send({success: false, msg: 'Authentication failed. Invalid token'});
            }
        }
        return next()
    })(req,res,next)
}
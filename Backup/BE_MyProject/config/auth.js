var jwt = require('jwt-simple')
var User = require(__dirname+'../models/User')
var getToken = require(__dirname+'../config/token')
var config = require(__dirname+'../config/database')

const auth = async(req,res,next) =>{
    try{
        var token = getToken(req.headers)
        if(token){
            var user = jwt.decode(token,config.secret)
            console.log(user)
            await User.findOne({_id:user._id})
                .exec(function(err,user){
                    if(err){
                        return res.status(401).send({
                            success: false,
                            msg:err.message+'haha'
                        })
                        
                    }
                    if(user && !err){
                        req.user = user
                        req.token = token
                    }
                    next()
                })
        }
        else{
            res.status(401).send({
                success: false,
                msg:'Please provide token'
            })
        }

    }
    catch(e){
        res.status(401).send({
            success: false,
            msg:'Please authenticate'
        })
    }
}

module.exports = auth
var Product = require('../models/Product')
var config = require('../config/database')
var verified = require('../config/verified')
var getToken = require('../config/token')
var message = require('../common/message')
var jwt = require('jwt-simple')

module.exports = function(app, io){
    app.post('/api/product/create', verified, function(req, res){
        var token = getToken(req.headers)
        if(token){
            var user = jwt.decode(token, config.secret)
            var product = new Product(req.body)
            product.user = user._id
            product.save(function(err, r){
                if(err) res.json({success:false, msg: err.message})
                else res.json({success:true, msg: message.create_sucess})
            })
        }
        else{
            return res.json({success:false, msg: message.no_token})
        }
    })

    app.get('/api/product/:id', verified, function(req, res){
        var token = getToken(req.headers)
        if(token){
            Product.findOne({_id: req.params.id})
                    .populate('user', 'username')
                    .exec(function(err, r){
                        res.json(r || {})
                    })
        }
        else{
            return res.json({success:false, msg: message.no_token})
        }
    })

    //Get list product of user
    app.get('/api/product/:id/list', verified, function(req, res){
        var token = getToken(req.headers)
        if(token){
            var idUser = req.params.id
            Product.find({user:idUser}).sort({createdAt: -1})
                    .exec(function(err, r){
                        res.json(r || [])
                    })
        }
        else{
            return res.json({success:false, msg: message.no_token})
        }
    })
}
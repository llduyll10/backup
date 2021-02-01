var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var bcrypt = require('bcrypt');
const validator = require('validator')
var Task = require(__dirname+'../models/Task')

var userSchema = new Schema({
    phone: {
        type:String,
        default:000
    },
    password: {
        type:String,
        trim:true

    },
    email:{
        type:String,
        trim:true,
        required:true,
        validate(value){
            if(!validator.isEmail(value)){
                throw new Error('Email is invalid')
            }
        }
    },
    name:{
        type:String,
        trim:true
    },
    status:String,
})


userSchema.methods.comparePassword = function(pw,cb){
    bcrypt.compare(pw,this.password,function(err,isMatch){
        if(err){
            return cb(err)
        }
        cb(null,isMatch)
    })
}


const User = mongoose.model('User', userSchema)

module.exports = User;
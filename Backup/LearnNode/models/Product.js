var mongoose = require('mongoose')
var Schema = mongoose.Schema

var ProductSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    productType:String,
    user: {type: Schema.Types.ObjectId, ref:'User'}
},{timestamps:true})

module.exports = mongoose.model('Product', ProductSchema)
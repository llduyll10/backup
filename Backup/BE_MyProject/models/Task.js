var mongoose = require('mongoose');
var Schema = mongoose.Schema;


var taskSchema = new Schema({
    owner:{
        type:Schema.Types.ObjectId,
        ref:'User',
        required: true
    },
    name:{
        type:String,
        trim:true
    },
    status:String,
    description:String
})
taskSchema.index({name: 'text', status: 'text'});
const Task = mongoose.model('Task', taskSchema)

module.exports = Task;
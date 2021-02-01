var User = require(__dirname+'../models/User')
var Task = require(__dirname+'../models/Task')
var jwt = require('jwt-simple');
var config = require(__dirname+'../config/database');
var bcrypt = require('bcrypt');
var getToken = require(__dirname+'../config/token')
var verified = require(__dirname+'../config/verified')
var auth = require(__dirname+'../config/auth')

module.exports = function (app, io) {
    app.post('/api/task', auth, function (req, res) {
        var token = getToken(req.headers)
        if (token) {
            var user = jwt.decode(token, config.secret)
            if (user.status === 'ACTIVE') {
                var task = {
                    name: req.body.name,
                    description: req.body.description,
                    status: req.body.status,
                    owner: user._id
                }
                var taskAdd = new Task(task);
                taskAdd.save(function (err, succ) {
                    if (err) {
                        res.json({
                            success: false,
                            msg: err.message
                        })
                    }
                    else {
                        res.json({
                            success: true,
                            msg: 'Thêm thành công'
                        })
                    }
                })
            }
        }
        else {
            res.status(401).send({
                success: false,
                msg: 'Vui lòng đăng nhập'
            })
        }
    })

    //Get task
    app.get('/api/task', auth, function (req, res) {
        var token = getToken(req.headers);
        if (token) {
            var user = jwt.decode(token, config.secret);
            Task.find({ owner: user._id }).populate('user').exec(function (err, cr) {
                res.json(cr || []);
            });
        } else {
            res.json({ success: false, msg: 'No token provided.' });
        }
    })
    app.post('/api/task/:id', auth, async function (req, res) {
        var token = getToken(req.headers);
        if (!token) {
            return res.json({ success: false, msg: 'No token provided.' });
        }
        var user = jwt.decode(token, config.secret);

        const updates = Object.keys(req.body)

        try {
            const task = await Task.findOne({ _id: req.params.id, owner: user._id })

            if (!task) {
                return res.status(404).send()
            }

            updates.forEach((update) => task[update] = req.body[update])
            await task.save()
            res.status(200).send({success:true,msg:'Cập nhật thành công'})
        } catch (e) {
            res.status(400).send(e)
        }
    })
    //Delete Task
    app.delete('/api/task/:id',auth,async function(req,res){
        var token = getToken(req.headers)
        if(!token){
            return res.json({ success: false, msg: 'No token provided.' })
        }
        var user = jwt.decode(token,config.secret)
        try{
            task = await Task.findOneAndDelete({_id:req.params.id,owner:user._id})
            if(!task){
                return res.status(404).send()
            }
            await task.save()
            res.status(200).send({success:true,msg:'Xoá thành công'})
        }
        catch(e){
            res.status(400).send(e)
        }
    })
    //Search task
    app.get('/api/task/:search',auth,async function(req,res){
        var skip = parseInt(req.query.skip || 0)
        var limit = parseInt(req.query.limit || 25)
        Task.find({$text:{$search:req.params.search}})
            .skip(skip)
            .limit(limit)
            .exec(function(err,val){
                res.json(val || [])
            })
    })

}
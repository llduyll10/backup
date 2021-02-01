var User = require(__dirname+'../models/User')
var jwt = require('jwt-simple');
var config = require(__dirname+'../config/database');
var bcrypt = require('bcrypt');
var getToken = require(__dirname+'../config/token')
var auth = require(__dirname+'../config/auth')
var Task = require(__dirname+'../models/Task')
module.exports = function (app, io) {
    app.post('/api/signup', makeSignup)

    function makeSignup(req, res) {
        if (!req.body.email || !req.body.password) {
            res.status(200).send({
                success: false,
                msg: 'Email, Password bắt buộc.'
            })
        }
        else {
            bcrypt.genSalt(10, function (err, salt) {
                if (err) {
                    return res.json({ success: false, msg: err.message })
                }
                bcrypt.hash(req.body.password, salt, function (err, hash) {
                    if (err) {
                        return res.json({ success: false, msg: err.message });
                    } else {
                        createUser(hash)
                    }
                })
            })

            function createUser(pass) {
                User.findOne({
                    email: req.body.email,
                    status: 'ACTIVE'
                }).exec((function (err, user) {
                    if (user && user._id) {
                        res.json({
                            success: false,
                            msg: 'Email đã tồn tại'
                        })
                    }
                    else {
                        var objUser = {
                            email: req.body.email,
                            password: pass,
                            name: req.body.name,
                            type: 'USER',
                            status: 'ACTIVE',
                            isAdmin: false,
                            createDate: new Date()
                        }
                        var newUser = new User(objUser);
                        newUser.save(function (err, user) {
                            if (err) {
                                return res.json({
                                    success: false,
                                    msg: err.message
                                })
                            }
                            else {
                                return res.json({
                                    success: true,
                                    msg: 'Đăng ký thành công'
                                })
                            }
                        })
                    }
                }))
            }
        }
    }

    //Authenticate
    app.post('/api/login', function (req, res) {
        if (!req.body.email || !req.body.password) {
            res.status(200).send({
                success: false,
                msg: 'Email bắt buộc.'
            })
        }
        else {
            User.findOne({ email: req.body.email })
                .exec(function (error, user) {
                    if (user) {
                        console.log(user)
                        user.comparePassword(req.body.password, function (err, isMatch) {
                            if (isMatch && !err) {
                                var userFind = JSON.parse(JSON.stringify(user))
                                delete userFind.password
                                if (config.admin.includes(req.body.email)) {
                                    userFind.isAdmin = true
                                }
                                res.status(200).send({
                                    success: true,
                                    token: jwt.encode(userFind, config.secret),
                                    name: userFind.name,
                                    isAdmin: userFind.isAdmin,
                                    msg: 'Đăng nhập thành công'
                                })
                            }
                            else {
                                res.status(200).send({
                                    success: false,
                                    msg: 'Sai mật khẩu.'
                                })
                            }
                        })
                    }
                    else {
                        res.status(200).send({
                            success: false,
                            msg: 'Tài khoản không tồn tại.'
                        })
                    }
                })
        }
    })

    //Get infor user
    app.get('/api/me', auth, function (req, res) {
        var user = req.user
        delete user._id
        delete user.password
        res.status(200).send({
            success: true,
            msg: 'Success',
            user: user
        })
    })
    //Delete user
    app.delete('/api/admin/delete/:id', auth, async (req, res) => {
        var token = getToken(req.headers)
        var user = jwt.decode(token, config.secret)
        var idDelete = req.params.id
        if (!token) {
            return res.json({
                success: false,
                msg: 'No token provided.'
            })
        }
        if (token && !user.isAdmin) {
            return res.json({
                success: false,
                msg: 'User is not permisson'
            })
        }
        try {
            task = await Task.deleteMany({ owner: idDelete })
            user = await User.deleteOne({ _id: idDelete })
            if (!user) {
                return res.json({
                    success: false,
                    msg: 'DELETE faile'
                })
            }
            res.status(200).send({
                success: true,
                msg: 'Xoá thành công'
            })
        } catch (e) {
            res.status(500).send({
                success: false,
                msg: e.message
            })
        }
    })
    //Get all user
    app.get('/api/list-user',auth,async function(req,res){
        var token = getToken(req.headers)
        var user  = jwt.decode(token,config.secret)
        if(!token){
            return res.json({
                success:false,
                msg: 'No token provided.'
            })
        }
        if(token && !user.isAdmin){
            return res.json({
                success:false,
                msg:'User is not permisson'
            })
        }
        await User.find()
                .exec()
                .then(val => {
                    res.json({
                        listUser: val.map(user => {
                            return {
                                email: user.email,
                                name: user.name,
                                phone: user.phone,
                                status: user.status,
                                id: user._id
                            }
                        })
                    })
                })
                .catch(e=>{
                    return res.json({
                        success: false,
                        msg: e
                    })
                })
    })
    //Get Detail User with Task 
    app.get('/api/user/:id', auth, async function (req, res) {
        var token = getToken(req.headers)
        var idUser = req.params.id

        if (!token) {
            return res.json({
                success: false,
                msg: 'No token provided.'
            })
        }      
        //Join Task collection to User collection
        var userFind = await User.findOne({ _id: idUser })
            .select('email name')
        delete userFind._id
        await Task.find({ owner: idUser })
            .populate('User', 'email')
            .exec()
            .then(val => {
                res.json({
                    userFind,
                    tasks: val.map(task => {
                        return {
                            description: task.description,
                            status: task.status,
                            taskName: task.name
                        }
                    })
                })
            })

    })
}
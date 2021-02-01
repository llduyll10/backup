module.exports = function(headers){
    if(headers && headers.authorization){
        var arr = headers.authorization.split(' ')
        if(arr.length === 2){
            return arr[1]
        }
        else{
            return null
        }
    }
    else{
        return null
    }
}
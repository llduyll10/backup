var reverse = function(x){
    var result = 0;
    list = [...x.toString()]
    list.reverse()
    if(list[list.length-1] == "-"){
        list.pop()
        result = -Number(list.join(""))
    }
    else{
        result = Number(list.join(""))
    }
    if(result < Math.pow(-2,31) || result > Math.pow(2,31)){
        return 0
    }
    return result
}
var x = -120
console.log(reverse(x))
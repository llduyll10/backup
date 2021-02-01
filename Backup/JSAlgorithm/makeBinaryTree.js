var binary = {}
var arr = [8,5,10,3,6,12];

function makeBinary(binary, number){
    if(binary.val === undefined){
        binary.val = number
    }
    //Xét node trái
    else if(number > binary.val){
        if(binary.right === undefined){
            binary.right = {val:number}
        }
        else{
            binary.right = makeBinary(binary.right, number)
        }
    }
    //Xét node phải
    else{
        if(binary.left === undefined){
            binary.left = {val:number}
        }
        else{
            binary.left = makeBinary(binary.left, number)
        }
    }
    return binary
}

var abc = [3,9,20,null,null,15,7]

for(let i in abc){
    makeBinary(binary, abc[i])
}

console.log(binary)


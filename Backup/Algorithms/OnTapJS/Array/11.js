//Array.forEach()
//Excute a provided function once for each array element

const array1 = ['a', 'b', 'c']
array1.forEach(ele => console.log(ele))

function flattern(arr){
    const result = []
    arr.forEach((i)=>{
        if(Array.isArray(i)){
            result.push(...flattern(i))
        }else{
            result.push(i)
        }
    })
    return result
}

const nested = [1, 2, 3, [4, 5, [6, 7], 8, 9]]
console.log('nested',flattern(nested));


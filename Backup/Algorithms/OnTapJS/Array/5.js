//Array.entries()
//Return a new Array Iterator contains the key/value pairs for each index in the array
const array1 = ['a','b','c']
const iterator1 = array1.entries()

console.log(iterator1.next().value)

//Iterating with index and element
const a = ['a','b','c']
for (const[index,ele] of a.entries()){
    console.log(index, ele)
}

//Using a for ... of loop
var b = ['a', 'b', 'c']
var iter = a.entries()
for (let e of iter){
    console.log(e)
}
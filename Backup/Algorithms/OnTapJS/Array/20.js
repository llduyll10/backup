// Array.reduce()
// Execute a reducer function (that you provide) on each element of the array
// Resulting in single output value

// The reducer function take 4 arguments
// 1/ Accumulator
// 2/ Current Value
// 3/ Current Index 
// 4/ Source Array

// Your reducer function's returned value is assigned to the accuulator, whose value is remembered accross each iteration
// throughout the array, and ultimately becomes the final, single resulting value

const array1 = [1, 2, 3, 4];
const reducer = (a, b) => a + b

console.log(array1.reduce(reducer));

//Grouping objects by a property
let people = [
    { name: 'Alice', age: 21 },
    { name: 'Max', age: 20 },
    { name: 'Jane', age: 20 }
];
function groupBy(objArr, property){
    return objArr.reduce(function(acc,obj){
        let key = obj[property]
        if(!acc[key]){
            acc[key] =[]
        }
        acc[key].push(obj)
        return acc
    },{})
}
let groupPeople = groupBy(people,'age')
console.log(groupPeople);

//Remove duplicate items in an array
let myArray = ['a', 'b', 'a', 'b', 'c', 'e', 'e', 'c', 'd', 'd', 'd', 'd']
let myOrderedArray = myArray.reduce(function(accumulator,currentValue){
    if(accumulator.indexOf(currentValue) === -1){
        accumulator.push(currentValue)
    }
    return accumulator
},[])
console.log();
// Using Set and Array.from() to remove duplicate items in an array
let orderedArray = Array.from(new Set(myArray))
console.log(orderedArray);
//Array.every()
//Use for testing whether all elements in the array pass the test implemented by the provided function
//Return a boolean value

const isBelowThreshold = (currentValue) => currentValue < 40
const arr1 = [1, 30, 39, 29, 10, 13];
console.log(arr1.every(isBelowThreshold))

//Examples

//Testing size of all array elements
function isBigEnough(ele, index, arr){
    return ele > 10
}
const arr2 = [12, 5, 8, 130, 44]
console.log(arr2.every(isBigEnough))


//Using arrow functions
console.log('Using arrow functions', arr2.every(x => x >= 10))
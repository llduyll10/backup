// Array.reduceRight()
// Applies a function against an accumulator and each value of the array (from right to left) 
// to reduce it to a single value

const array1 = [[0,1], [2,3], [4,5]].reduceRight(
    (accumulator, currentValue) => accumulator.concat(currentValue)
)
console.log(array1);
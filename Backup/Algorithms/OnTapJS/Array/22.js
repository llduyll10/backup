// Array.reverse()
// Method reverse an array in place. The first array element becomes the last,
// and the last array element becomes the first

const array1 = ['one', 'two', 'three']
console.log('array1: ', array1);
const reversed = array1.reverse()
console.log('reversed: ', reversed);

// Careful: reverse is destructive -- it changes the original array.
console.log('array1: ', array1 );
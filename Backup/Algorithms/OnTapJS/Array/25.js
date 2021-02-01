// Array.some()
// Method tests whether at least one element in the array passes the test implemented by the provided function
// It returns a A Boolean value

const array = [1, 2, 3, 4, 5];
// checks whether an element is even
const even = (element) => element % 2 === 0;
console.log(array.some(even));
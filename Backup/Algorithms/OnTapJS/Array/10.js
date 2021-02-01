// Array.findIndex()
// Return the index of first element in array that satisfies the provide testing function
// Otherwise, it returns -1, indicating that no element passed the test
const array1 = [5, 12, 8, 130, 44];

const isLargeNumber = (ele) => ele > 13

console.log(array1.findIndex(isLargeNumber));

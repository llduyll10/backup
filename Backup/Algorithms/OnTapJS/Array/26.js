// Array.sort()
// Methods sorts the elements of an array in place and returens the sorted array
// The default sort is ascending, built upon converting the elements into strings,
// then comparing their sequences of UTF-16 code units values
//The time and space complexity of the sort cannot be guaranteed as it depends on the implements


const months = ['March', 'Jan', 'Feb', 'Dec'];
months.sort();
console.log(months);
// expected output: Array ["Dec", "Feb", "Jan", "March"]

const array1 = [1, 30, 4, 21, 100000];
array1.sort();
console.log(array1);
// expected output: Array [1, 100000, 21, 30, 4]
//Array.fill()
//Changes all elements in an array to a static value
//from a start index(default 0) to an end index (default array.length)
//Returns the modified array


const arr1  = [1, 2, 3, 4];

// fill with 0 from position 2 until position 4
console.log(arr1.fill(0,2,4))

//fill with 5 in position 1
console.log(arr1.fill(5,1))

//fill 6 in all element
console.log(arr1.fill(6))
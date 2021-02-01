// Array.filter()
// Creates a new array with all elements that pass the test implemented by the provided function
const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];
const results = words.filter(word => word.length > 6)
console.log('results', results)
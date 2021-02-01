// Learn about from

// Array from a String
a = Array.from('foo')
console.log('Array from a String',a)

//Sequence generator (range)
const range = (start, stop, step) => Array.from({length: (stop-start)/step + 1}, (_,i)=>start + (i*step))
console.log(range(1,10,1))

//Generate the alphabet using function Range 
console.log(range('A'.charCodeAt(0),'Z'.charCodeAt(0),1).map(x=>String.fromCharCode(x)))
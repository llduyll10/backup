/**
 * @param {string} S
 * @return {string}
 */
var removeDuplicates = function(S) {
    var stack = []
    for(let s of S){
        s === stack[stack.length-1] ? stack.pop() : stack.push(s)
    }
    return stack.join('')
};
var s = "abbaca"
console.log(removeDuplicates(s))
/**
 * @param {string} s
 * @return {string}
 */
var makeGood = function(s) {
    let stack = ['']
    for(c of s){
        let top = stack[stack.length - 1]
        if(top.toLowerCase() === c.toLowerCase() && top !== c){
            stack.pop()
        }
        else{
            stack.push(c)
        }
    }
    return stack.join('')
};
var  s = "leEeetcode"
console.log(makeGood(s))
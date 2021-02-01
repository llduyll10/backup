/**
 * @param {string[]} ops
 * @return {number}
 */
//Bỏ từng phần tử vào stack và xử lý từ từ
var calPoints = function(ops) {
    let stack = []
    ops.forEach(op =>{
        if(parseInt(op)){
            stack.push(parseInt(op))
        }
        else if(op === '+'){
            stack.push((stack[stack.length-1] ||0) + (stack[stack.length-2] ||0))
        }
        else if(op === 'D'){
            stack.push((stack[stack.length-1] || 0) * 2)
        }
        else if(op === 'C'){
            stack.pop()
        }
    })
    return stack.reduce((u,v) => u+v, 0)
};
var ops = ["5","2","C","D","+"]
console.log(calPoints(ops))
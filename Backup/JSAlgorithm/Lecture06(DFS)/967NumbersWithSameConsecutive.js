/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var numsSameConsecDiff = function(n, k) {
    let res = []
    var compose = function(A){
        if(A.length === n){
            res.push(A)
        }
        else{
            let lastDigit = Number(A[A.length-1])
            if(lastDigit - k >= 0) compose(`${A}${lastDigit-k}`)
            if(lastDigit + k <= 9 && k > 0) compose(`${A}${lastDigit+k}`)
        }
    }
    for(let i = 0; i < 10; i++){
        if(n > 1 && i === 0) continue
        compose(`${i}`)
    }
    return res
};


console.log(numsSameConsecDiff(3, 7))
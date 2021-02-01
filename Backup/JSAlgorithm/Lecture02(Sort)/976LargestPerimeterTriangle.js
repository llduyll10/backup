/**
 * @param {number[]} A
 * @return {number}
 */
var largestPerimeter = function(A) {
    A.sort((a,b) => b-a) //Sort giam dan
    const N = A.length - 2
    for(let i = 0; i<N; i++){
        if(A[i] < A[i+1] + A[i+2]) 
        {
            return A[i] + A[i+1] + A[i+2]
        }
    }
    return 0
};
var a =[2,1,2]
console.log(largestPerimeter(a))
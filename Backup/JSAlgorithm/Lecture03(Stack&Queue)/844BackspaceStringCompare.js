/**
 * @param {string} S
 * @param {string} T
 * @return {boolean}
 */
var backspaceCompare = function(S, T) {
    let S_Stack = []
    let T_Stack = []
    for(let i = 0; i< S.length; i++){
        if(S[i] !== '#'){
            S_Stack.push(S[i])
        }
        else{
            //Yêu cầu do nếu là ký tự '#' là phải xoá đi trong stack 1
            S_Stack.pop()
        }
    }
    for(let i = 0; i< T.length; i++){
        if(T[i] !== '#'){
            T_Stack.push(T[i])
        }
        else{
            T_Stack.pop()
        }
    }
    if(S_Stack.join('') === T_Stack.join('')){
        return true
    }
    else{
        return false
    }
};
var S = "ab#c", T = "ad#c"
console.log(backspaceCompare(S,T))
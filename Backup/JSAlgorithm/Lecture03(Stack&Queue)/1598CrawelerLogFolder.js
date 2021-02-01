/**
 * @param {string[]} logs
 * @return {number}
 */
// Ý tưởng là nếu ../ thì sẽ giảm độ sâu đi 1 đơn vị
var minOperations = function(logs) {
    let deep = 0
    for(let log of logs){
        if(log === './'){
            continue
        }
        else if(log === '../'){
            deep--
        }
        else{
            deep++
        }

        if(deep < 0){
            deep = 0
        }
    }
    return deep
};

var logs = ["d1/","d2/","../","d21/","./"]
console.log(minOperations(logs))
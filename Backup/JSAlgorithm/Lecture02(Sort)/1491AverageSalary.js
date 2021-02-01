/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function(salary) {
    return salary.reduce(
        (acc,curr) => acc + curr,
        0 - Math.min(...salary) - Math.max(...salary) //Gán giá trị ban đầu ( ở đây là biến acc)
    ) / (salary.length - 2) //Sau khi tính xong thì chia cho length - 2 ( do đã loại bỏ min và max)
};


salary = [4000,3000,1000,2000]
console.log(average(salary))
var twoSum = function(nums, target){
    let res = []
    let map = new Map()
    for(let i = 0; i< nums.length; i++){
        //Nếu mà có rồi thì trả về res vì chỉ có duy nhất 1 cặp trong 1 array
        if(map.has(target - nums[i])){
            res.push(map.get(target-nums[i]));
            res.push(i)
            return res
        }
        //Nếu chưa có thì set lại cho "từ điển" map 1 cặp "key-value" là "num[i] - i"
        map.set(nums[i],i)
    }
}
var nums = [3,2,4], target = 6
console.log(twoSum(nums,target))
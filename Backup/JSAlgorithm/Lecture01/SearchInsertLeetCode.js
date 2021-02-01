var searchInsert = function(nums, target){
    for(let i = 0; i < nums.length; i++){
        if(target == nums[i] || target < nums[i]){
            return i
        }
    }
    return nums.length
}
var nums = [1,3,5,6], target = 5
console.log(searchInsert(nums,target))
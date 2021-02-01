/**
 * https://leetcode.com/problems/remove-element/
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 * Time O(n) - n is the no. of items in nums
 * Space O(1)
 * Optimized run time
 */

 var removeElement = function(nums, val){
    if(!nums.length ){
        // when there is no nums in the array return 0
        return 0
    }
    if(val === undefined){
        throw new Error('argument val cannot be undefined for removeElement function')
    }
    let index = 0
    for(let i = 0; i<nums.length; i++){
        if(nums[i] !== val){
            nums[index] = nums[i]
            index ++
        }
    }
    return index
    
 }
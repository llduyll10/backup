//Remove Duplicates from Sorted Array


// Khi sử dụng để làm việc
var removeDuplicates = function(nums){
    let newArr = [...new Set(nums)]
    return newArr 
}

//Không làm thay đổi địa chỉ bộ nhớ
var removeDuplicate = function(nums){
    let i = 0;
    for(let j = 0; j<nums.length; j++){
        if(nums[j] != nums[i]){
            nums[++i] =nums[j] // câu này tương đương với 2 lệnh : i = i + 1; nums[i] = nums[j]
        }
    }
    return ++i
}

var nums = [0,0,1,1,1,2,2,3,3,4]
console.log(removeDuplicates(nums))
console.log(removeDuplicate(nums))
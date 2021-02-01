/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 * Khoảng cách lớn nhất của i và j là bằng k 
 */
var containsNearbyDuplicate = function(nums,k){
    var map = new Map()
    for(let i = 0; i< nums.length; i++){
        //Kiểm tra xem trong từ điển có lưu giá trị index thoả mãn không
        // i - map.get(nums[i]) <= k
        //Ý nghĩa là lấy giá trị index hiện tại trừ đi giá trị index mà lưu trong từ điển
        // Nếu 2 giá trị đó trừ nhau mà nhỏ hơn k
        // Thì có nghĩa là 2 thằng đó cách nhau 1 khoảng cách thoả yêu cầu
        if(map.has(nums[i]) && i - map.get(nums[i]) <= k){ 
            return true
        }
        //Nếu chưa có thì lưu giá trị vào từ điển theo dạng: 
        // { nums[i], i }
        map.set(nums[i],i)
    }
    return false
}

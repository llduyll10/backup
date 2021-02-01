var threeSum = function(nums){
    nums.sort((a,b) => a-b) //Sắp xếp tăng dần 
    let results = []
    for(let i = 0; i<nums.length; i++){
        let j = i + 1
        let k = nums.length - 1
        while( j < k){
            const sum = nums[i] + nums[j] + nums[k]
            if(sum === 0){ //Trường hợp tổng bằng không thì ta tăng j giảm k
                results.push([nums[i], nums[j], nums[k]])
                while(j<k && nums[i] == nums[j+1]){
                    j++;
                }
                j++;
                while(k > j && nums[k] == nums[k-1]){
                    k--;
                }
                k--;
            }
            else if(sum<0){ //Nếu tổng < 0 thì ta tăng j 
                j++;
            }
            else{ //Tổng > 0 thì ta giảm k
                k--;
            }
            while(i < nums.length - 1 && nums[i] == nums[i+1]){
                i++;
            }
        }
    }   
    return results
}

var nums = [-1,0,1,2,-1,-4]
console.log(threeSum(nums))
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let setNum1 = new Set(nums1) // Tạo ra mảng không trùng lặp
    console.log()
    return [...new Set(nums2.filter(num => setNum1.has(num)))] //Trả về mảng không trùng lặp num2 lọc ra nếu thoả yêu cầu
};
var nums1 = [1,2,2,1], nums2 = [2,2]
console.log(intersection(nums1, nums2))
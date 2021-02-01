// Xử lý với mảng
// 1/Khai báo
var arr = []

// 2/Thêm phần tử vào đầu mảng
// array.unshift()
arr.unshift(1,2)
console.log(arr)

// 3/Thêm phần tử vào cuối mảng
// array.push()
arr.push(3,4)
console.log(arr)

// 4/Chèn vào vị trí chỉ định
//  array.splice(vị trí muốn chèn, 0, giá trị)
arr.splice(2,0,5)
console.log(arr)

// 5/Lấy kích thược của mảng
// array.length

// 6/Truy cập phần tử trong mảng
// arr[vị trí muốn lấy giá trị]
console.log(arr[2])

// 7/Xoá phần tử cuối khỏi mảng
// arr.pop() sẽ xoá phần tử cuối và trả về giá trị vừa xoá

console.log(arr.pop())

// 8/Xóa phần tử ở bất kỳ vị trí nào trong mảng
// arary.splice(vị trí muốn xoá, số phần tử muốn xoá)

//Ví dụ: remove 2 phần tử bắt đầu từ vị trí 2
var A1 = [1,2,3,4,5,6]
console.log(A1.splice(2,2))

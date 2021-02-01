// 1/Lấy mã ASCII của ký tự
// string.charCodeAt(vị trí của ký tự trong chuỗi cần tra mã)
var str = 'Hello'
console.log(str.charCodeAt(0))

// 2/Trả về ký tự theo vị trí trong chuối
// str.charAt(vị trí muốn lấy)
console.log(str.charAt(1))

// 3/Chuyển từ một số Unicode thành chữ cái
// String.fromCharCode(số unicode)
console.log(String.fromCharCode(72))

// 4/Chuyển chuỗi thành số 
// parseInt()

// 5/Chuyển số thành chuỗi
// toString()

// 6/ Chuyển in hoa thành in thường ký tự ASCII
// má ký tự +32 => chuyển thành in Thường
// mã ký tự -32 => chuyển thành in Hoa
var s = 'a'
var c = s.charCodeAt(0) -32
console.log(String.fromCharCode(c))
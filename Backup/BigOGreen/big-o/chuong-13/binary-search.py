# Ta thấy theo cách trên ta phải duyệt từng phần tử của mảng để tìm vị trí của xx, giả sử xx nằm ở cuối mảng vậy ta phải duyệt đúng nn lần (với nn là số lượng phần tử của mảng, nn có thể lên tới 105). Tuy nhiên theo dữ kiện đề bài ta đã có mảng này đã được sắp xếp tăng dần, vậy lợi dụng tính chất này ta có thể rút ngắn số lần lặp để tìm vị trí của xx thông qua cách là ta sẽ khởi tạo biến left và right với left ban đầu là 0 (vị trí bắt đầu mảng) và right là n - 1n−1 (vị trí kết thúc mảng), lặp lại trong khi left \le rightleft≤right:

# Tính giá trị mid = (left + right)/2mid=(left+right)/2 (vị trí chính giữa của leftleft và rightright).

# Nếu giá trị tại vị trí mid của mảng chính là xx thì kết thúc việc tìm và trả về kết quả.

# Ngược lại nếu giá trị tại vị trí mid của mảng lớn hơn xx suy ra ta không cần tìm từ mid trở lên right nữa vì chắc chắn những giá trị này cũng lớn hơn xx -> thiết lập right = mid – 1.

# Bằng không thì giá trị tại vị trí mid của mảng sẽ nhỏ hơn xx suy ra ta cũng không cần tìm từ mid trở về left nữa vì chắc chắn những giá trị này cũng nhỏ hơn xx -> thiết lập left = mid + 1left=mid+1.

#Vi mang tang dan => dung binanry search
def binanry_search(arr,left,right,x):
    while left < right:
        mid =(left + right) // 2
        if arr[mid] == x:
            return mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1
n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(binanry_search(arr, 0, n-1, x))
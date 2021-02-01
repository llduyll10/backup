def tinhFibonnacci(n):
    if n == 0 or n == 1 :
        return 1
    return tinhFibonnacci(n-1) +  tinhFibonnacci(n-2)

n = int(input())
print(tinhFibonnacci(n))
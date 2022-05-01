# cách lấy input vào trong 1 dòng
n = int(input())
arr = []
arr = list(map(int, input().split(' ')))  # oneline
for i in arr:
    print(i)
print(1/n * sum(arr))

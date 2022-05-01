def getValue(arr, start, end):
    index = start
    key = arr[index]  # đặt phần tử để so sánh là phần tử đầu

    while start < end:
        # đặt điều kiện để phần tử start không chạy quá ra ngoài arr
        while start < len(arr) and arr[start] <= key:
            start += 1
        while arr[end] > key:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[index] = arr[index], arr[end]

    return end


def quick(arr, start, end):
    if start <= end:
        value = getValue(arr, start, end)
        quick(arr, start, value - 1)  # gọi hàm cho 2 bên tiếp tục
        quick(arr, value + 1, end)
    return arr


arr = [5, 4, 3]
print(quick(arr, 0, len(arr) - 1))

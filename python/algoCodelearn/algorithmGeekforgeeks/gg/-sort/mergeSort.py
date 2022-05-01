def mergeSort(arr):
    if len(arr) <= 1: #nếu độ dài dãy = 1 --> return 
        return arr
    else:
        left = arr[:len(arr) // 2] #chia dãy arr làm 2 dãy LEFT và RIGHT 
        right = arr[len(arr) // 2:]
        mergeSort(left)#gọi hàm
        mergeSort(right)
        i = 0 #i, j, k lần lượt là các phần tử của các dãy left, right, arr to.
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]: #so sánh các phần tử left và right, phần tử nào bé hơn sẽ được vào dãy arr trước
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left): #các phần tử trong dãy RIGHT đã vào hết nhưng LEFT vẫn còn
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right): #tương tự như trên
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


print(mergeSort([5, 4, 3, 0]))

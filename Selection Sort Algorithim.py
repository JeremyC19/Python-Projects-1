def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]


nums = [5, 9, 1, 2, 4, 8, 6, 3, 7]
print("This is the unsorted list ")
print(nums)
selection_sort(nums)
print("This is the sorted list ")
print(nums)
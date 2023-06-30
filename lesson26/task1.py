def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
arr = [2,4,7,8]
target = 2
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(result)

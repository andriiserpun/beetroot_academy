def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left, right = arr[:mid], arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
def merge(left, right):
    merged = []
    left_index, right_index = 0,0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    return merged

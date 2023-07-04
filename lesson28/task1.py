def bubble_sort_modified(arr):
    n = len(arr)
    for i in range(0, n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
# данный вид отсортировки уместен в том случае, если список уже частично отсортирован.
# И чтобы ускорить процесс отсортировки, можно сортировать с противоположного направления

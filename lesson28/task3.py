import random
import copy
from timeit import timeit
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    equal = [i for i in arr if i == pivot]
    return quicksort(left) + equal + quicksort(right)
arr1 = [random.randint(1, 10000) for i in range(10000)]
sorted_numbers1 = quicksort(arr1)
print(copy.deepcopy(sorted_numbers1))

arr2 = [random.randint(1, 100000) for i in range(100000)]
sorted_numbers2 = quicksort(arr2)
print(copy.deepcopy(sorted_numbers2))

p = timeit(lambda: quicksort(copy.deepcopy(arr1)), number=1)
print("Время выполнения", p)

p = timeit(lambda: quicksort(copy.deepcopy(arr2)), number=1)
print("Время выполнения", p)
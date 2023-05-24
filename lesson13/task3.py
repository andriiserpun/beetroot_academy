nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
def choose_func(nums: list, func1, funс2):
    if (num > 0 for num in nums):
        print(nums1)
        return nums1
    else:
        print(nums2)
        return nums2
def square_nums(nums):
    return [num ** 2 for num in nums]
def remove_negatives(nums):
    return [num for num in nums if num > 0]
result1 = choose_func(nums1, square_nums, remove_negatives)
result2 = choose_func(nums2, square_nums, remove_negatives)
print(result1)
print(result2)


# assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
# assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

# def choose_func(nums: list, func1, func2):
#     pass
#
# # Assertions
#
# nums1 = [1, 2, 3, 4, 5]
#
# nums2 = [1, -2, 3, -4, 5]
#
# def square_nums(nums):
#     return [num ** 2 for num in nums]
#
# def remove_negatives(nums):
#     return [num for num in nums if num > 0]
#
# assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
# assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
#

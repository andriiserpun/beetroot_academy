class Mathematicians:
    pass
    def square_nums(self, nums):
        return [num ** 2 for num in nums]
    def remove_positives(self, nums):
        return [num for num in nums if num <= 0]
    def filter_leaps(self, nums):
        return [ num for num in nums if num % 4 == 0]

m = Mathematicians()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
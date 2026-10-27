
def merge_sort(nums):
    # merge two sorted arrays
    def merge(left, right):
        i = j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

assert merge_sort([]) == []
assert merge_sort([1]) == [1]
assert merge_sort([2, 1]) == [1, 2]
assert merge_sort([1, 5, 2, 3]) == [1, 2, 3, 5]
assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert merge_sort([1, 1, 1]) == [1, 1, 1]
assert merge_sort([4, 2, 2, 3, 1]) == [1, 2, 2, 3, 4]
assert merge_sort([10, -1, 0, 7, 7]) == [-1, 0, 7, 7, 10]
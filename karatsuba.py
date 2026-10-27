def karatsuba(x:int, y:int):
    n = max(len(str(int(x))),len(str((int(y)))))
    if n == 1:
        return x * y
    
    m = n / 2
    exp = 10 ** m

    
    a = x // exp
    b = x % exp
    c = y // exp
    d = y % exp

    p = a + b
    q = c + d

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    pq = karatsuba(p, q)
    adbc = pq - ac - bd

    return 10 ** n * ac + 10 ** m * adbc + bd

def check(x, y):
    assert round(karatsuba(x, y)) == (x * y)

check(5, 1)
check(56, 12)
check(5678, 1234)
check(0, 1234)
check(9, 9)
check(10, 10)
check(99, 99)
check(123, 456)
check(5678, 12)
check(7, 123456)
check(999, 999)
check(12345, 67890)
check(1234567, 89)

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

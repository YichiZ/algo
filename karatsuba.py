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

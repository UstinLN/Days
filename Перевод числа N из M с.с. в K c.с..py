def to_Decimal(n, b):
    d = 0
    i = 0
    c = 0
    if type(n) == int:
        while n != 0:
            d += (n % 10) * pow(b, i)
            n //= 10
            i += 1
        return d
    else:
        while int(c) < 0:
            c = n * 10
            d += int(c) * pow(b, i - 1)
            i -= 1
        return d


def to_Base(n, k):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        digit = n % k
        res = digits[digit] + res
        n //= k
    return res


def convert_N(n, A, k):
    dec = to_Decimal(A, n)
    res = to_Base(dec, k)
    return res


n = int(input())
A = int(input())
k = int(input())
res = convert_N(n, A, k)
print(res)




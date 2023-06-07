N = int(input())
print('Инверсия: ', ~N)
print('Инверсия: ', bin(~N))

N2 = N & 1
N4 = N & 2
N8 = N & 3
print('И: ', N2, N4, N8)
print('И: ', bin(N2), bin(N4), bin(N8))

N2 = N | 1
N4 = N | 2
N8 = N | 3
print('ИЛИ: ', N2, N4, N8)
print('ИЛИ: ', bin(N2), bin(N4), bin(N8))

N2 = N ^ 1
N4 = N ^ 2
N8 = N ^ 3
print('XOR: ', N2, N4, N8)
print('XOR: ', bin(N2), bin(N4), bin(N8))

N2 = N >> 1
N4 = N >> 2
N8 = N >> 3
print('Сдвиг вправо: ', N2, N4, N8)
print('Сдвиг вправо: ', bin(N2), bin(N4), bin(N8))

N2 = N << 1
N4 = N << 2
N8 = N << 3
print('Сдвиг влево: ', N2, N4, N8)
print('Сдвиг влево: ', bin(N2), bin(N4), bin(N8))
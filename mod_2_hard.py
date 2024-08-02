n = int (input ('Введите число '))
r = 2
b = [n]
for r in range (2, n // r):
    if n % r == 0:
        b.append (int (n / r))
        b.append (r)
        n = int (n / r)
        if n % r == 0:
            b.append (int (n / r))
    elif n < 1:
        break
b = set (b)
b = list (b)
b = sorted (b)
c = []
for i in range (len (b)):
    y = b[i]
    m = int (b[i] / 2)
    a = []
    if b[i] % 2 == 0:
        m = m - 1
    for j in range (m):
        a.append (j + 1)
        a.append (b[i] - j - 1)
    c = (c + a)
print ('Пароль ', ''.join (str (item) for item in c))

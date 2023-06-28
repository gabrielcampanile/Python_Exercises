# 25**(1/2)
# 125**(1/3)
# oi*5
# =*20

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))
s = n1 + n2 + n3
p = n1 * n2 * n3
e = n1 ** n2 ** n3
d = n1 / n2 / n3
di = n1 // n2 // n3
r = n1 % n2 % n3
print(f'A soma é {s}, o produto é {p} e a potência é {e}!', end=' ')
print(f'A divisão é {d}, \na divisão inteira é {di} e o resto é {r}.')

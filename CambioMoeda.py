nome = input('Nome do usuário: ')
print(f'Olá, {nome}! Bem-vindo(a) ao exchange online.')
r = float(input('Por favor, digite o valor em reais (R$) que deseja trocar: '))
d = r/5.199
dc = r/3.873
da = r/3.579
p = r/0.028
e = r/5.594
l = r/6.337
print('Essas são as suas opções de câmbio de acordo com a cotação atual:')
print(f'Dólar Americano = {d:.3f}$\nDólar Canadense = {dc:.3f}$\nDólar Australiano = {da:.3f}$')
print(f'Peso Argentino = {p:.3f}¢\nEuro = {e:.3f}€\nLibra = {l:.3f}£')
print('Agradecemos a preferência!')
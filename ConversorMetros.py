M = float(input('Digite um valor em metros: '))
dM = M*10
cM = M*100
mmM = M*1000
print(f'{M} metros equivalem a {dM} decâmetros, {cM} centímetros e {mmM} milímetros.')
DM = float(input('Digite um valor em decâmetros: '))
mD = DM/10
cmD = DM*10
mmD = DM*100
print(f'{DM} decâmetros equivalem a {mD} metros, {cmD} centímetros e {mmD} milímetros.')
CM = float(input('Digite um valor em centímetros: '))
mC = CM/100
dmC = CM/10
mmC = CM*10
print(f'{CM} centímetros equivalem a {mC} metros, {dmC} decâmetros e {mmC} milímetros.')
MM = float(input('Digite um valor em milímetros: '))
mM = MM/1000
dmM = MM/100
cmM = MM/10
print(f'{MM} milímetros equivalem a {mM} metros, {dmM} decâmetros e {cmM} centímetros.')

# print(f'O valor {M} em metros equivale a: {dM}dm, {cM}cm e {mmM}mm!')
# print(f'O valor {DM} em decâmetros equivale a: {mD}m, {cmD}cm e {mmD}mm!')
# print(f'O valor {CM} em centímetros equivale a: {mC}m, {dmC}dm e {mmC}mm!')
# print(f'O valor {MM} em milímetros equivale a: {mM}m, {dmM}dm e {cmM}cm!')

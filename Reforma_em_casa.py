altura = float(input())
comprimento = float(input())
largura = float(input())

area_piso = largura * comprimento
volume_sala = largura * comprimento * altura
area_parede =  2 * altura * largura + 2* altura * comprimento

print(f'{area_piso:.0f}')
print(f'{volume_sala:.0f}')
print(f'{area_parede:.0f}')

dividendo = float(input())
divisor = float(input())

divisao = dividendo // divisor
resto = dividendo % divisor
divisao = round(divisao,2)
resto = round(resto,2)
print(f'{divisao:.4f}')
print(f'{resto:.4f}')

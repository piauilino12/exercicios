minutos = int(input().strip())

horas = minutos // 60
resto = minutos % 60

print(f'{horas}h{resto}min')

raio = float(input())

circunferencia =2 * 3.141592 * raio
a_circulo = 3.141592 * (raio*raio)
a_esfera = 4 * 3.141592 * (raio*raio)
v_esfera = 4/3 * 3.141592 * (raio**3)

print(f'{circunferencia:.6f}')
print(f'{a_circulo:.6f}')
print(f'{a_esfera:.6f}')
print(f'{v_esfera:.6f}')

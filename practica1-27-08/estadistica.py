import math
print("Ingrese 10 números separados por espacios:")
n = input().split()

numeros = []
for num_str in n:
    numeros.append(float(num_str))

s = 0
for num in numeros:
    s += num
p = s / len(numeros)

scuadrados= 0
for i, num in enumerate(numeros):
    d = num - p
    cuad = d*d
    scuadrados += cuad

desviacion = math.sqrt(scuadrados / (len(numeros) - 1))

print(f"\nEl promedio es {promedio:.2f}")
print(f"La desviación estándar es {desviacion:.5f}")

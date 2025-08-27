import math
print("Ingrese 10 números: ")
num =[]
for i in range(10):
    numero = float(input(f"Número {i+1}: "))
    num.append(numero)
s=0
for j in num:
    s+= j
p = s/len(num)
scuadrados = 0
for j in num:
    d = j-p
    scuadrados += d**2
desv =math.sqrt(scuadrados/(len(num)-1))

print(f"El promedio es {p:.2f}")
print(f"La desviación estándar es {desv: .5f}") 

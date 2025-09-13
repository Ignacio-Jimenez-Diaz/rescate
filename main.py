resultados = []
for _ in range(100):
    suma = 0
    for _ in range(5):
        suma += 0.1
    resultados.append(suma)

for i, valor in enumerate(resultados, 1):
    print(f"Iteración {i}: {valor}")
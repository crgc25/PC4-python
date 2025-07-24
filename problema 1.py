import requests

url = "https://raw.githubusercontent.com/gdelgador/ProgramacionPython202506/main/Modulo4/src/temperaturas.txt"

response = requests.get(url)
if response.status_code == 200:
    lineas = response.text.strip().split('\n')
else:
    print("Error al acceder al fichero")
    lineas = []

temperaturas = []

for linea in lineas:
    partes = linea.split(',')
    if len(partes) == 2:
        fecha, temp_str = partes
        try:
            temp = float(temp_str)
            temperaturas.append(temp)
        except ValueError:
            print(f"Valor de temperatura inválido: {temp_str}")

if temperaturas:
    promedio = sum(temperaturas) / len(temperaturas)
    max_temp = max(temperaturas)
    min_temp = min(temperaturas)
else:
    promedio = max_temp = min_temp = 0

with open('resumen_temperaturas.txt', 'w') as f:
    f.write(f"Temperatura promedio: {promedio:.2f}\n")
    f.write(f"Temperatura máxima: {max_temp:.2f}\n")
    f.write(f"Temperatura mínima: {min_temp:.2f}\n")

import os

def guardar_tabla(n):
    """Genera y guarda la tabla de multiplicar de n en el archivo 'tabla-n.txt'."""
    filename = f"tabla-{n}.txt"
    with open(filename, "w") as archivo:
        for i in range(1, 11):
            resultado = n * i
            archivo.write(f"{n} x {i} = {resultado}\n")
    print(f"Tabla de {n} guardada en {filename}.")

def leer_tabla(n):
    """Lee y muestra el contenido del archivo 'tabla-n.txt'."""
    filename = f"tabla-{n}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as archivo:
            print(f"Contenido de {filename}:")
            print(archivo.read())
    else:
        print(f"El archivo {filename} no existe.")

def mostrar_linea_m(n, m):
    """Muestra la línea m del archivo 'tabla-n.txt'."""
    filename = f"tabla-{n}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= len(lineas):
                print(f"Línea {m} de {filename}: {lineas[m-1].strip()}")
            else:
                print(f"El archivo {filename} solo tiene {len(lineas)} líneas.")
    else:
        print(f"El archivo {filename} no existe.")

def solicitar_numero(mensaje):
    """Solicita un número entre 1 y 10, validando la entrada."""
    while True:
        try:
            num = int(input(mensaje))
            if 1 <= num <= 10:
                return num
            else:
                print("Por favor, ingrese un número entre 1 y 10.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

def menu():
    """Menú principal del programa."""
    while True:
        print("\n--- Menú ---")
        print("1. Guardar la tabla de multiplicar de un número")
        print("2. Mostrar la tabla de multiplicar de un número")
        print("3. Mostrar una línea específica de la tabla")
        print("4. Salir")
        opción = input("Seleccione una opción: ")

        if opción == '1':
            n = solicitar_numero("Ingrese un número entre 1 y 10 para guardar su tabla: ")
            guardar_tabla(n)
        elif opción == '2':
            n = solicitar_numero("Ingrese un número entre 1 y 10 para leer su tabla: ")
            leer_tabla(n)
        elif opción == '3':
            n = solicitar_numero("Ingrese un número entre 1 y 10 para leer su tabla: ")
            m = solicitar_numero("Ingrese la línea que desea mostrar (1-10): ")
            mostrar_linea_m(n, m)
        elif opción == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2, 3 o 4.")

if __name__ == "__main__":
    menu()

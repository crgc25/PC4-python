import os

def contar_lineas_codigo(ruta_archivo):
    """
    Cuenta las líneas de código en un archivo Python, excluyendo comentarios y líneas en blanco.
    """
    lineas_codigo = 0
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea_stripped = linea.strip()
                if linea_stripped == "" or linea_stripped.startswith('#'):
                    continue
                lineas_codigo += 1
        return lineas_codigo
    except Exception as e:
        return None

def main():
    ruta = input("Ingresa la ruta del archivo .py: ").strip()

    if not os.path.isfile(ruta):
        return
    if not ruta.lower().endswith('.py'):
        return

    resultado = contar_lineas_codigo(ruta)
    if resultado is not None:
        print(f"El número de líneas de código en '{ruta}': {resultado}")

if __name__ == "__main__":
    main()

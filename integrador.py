import csv

ARCHIVO_CSV = "paises.csv"
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]


# ----------------------------------------
# FUNCIONES AUXILIARES GENERALES
# ----------------------------------------

def normalizar(texto):
    """Formatea el texto a minúsculas y sin tildes, para comparar sin errores"""

    texto = texto.strip().lower()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")

    return texto


def pedir_texto(mensaje):
    """Pide un texto y repite hasta que no esté vacío ni sea solo números"""

    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: el campo no puede estar vacío.")
        elif valor.replace(" ", "").isdigit():
            print("Error: el campo no puede ser solo números.")
        else:
            return valor


def pedir_entero(mensaje, minimo=0):
    """Pide un número entero mayor o igual a 'minimo' y repite hasta que sea válido, el mínimo por defecto es 0"""

    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: el campo no puede estar vacío.")
            continue
        try:
            numero = int(valor)
        except ValueError:
            print("Error: ingresá un número entero válido (sin puntos ni letras).")
            continue
        if numero < minimo:
            print(f"Error: el número debe ser mayor o igual a {minimo}.")
            continue
        return numero


# =====================
# MANEJO DEL ARCHIVO CSV
# ======================

def cargar_paises():
    """Lee los países del CSV y devuelve una lista de diccionarios."""
    paises = []
    try:
        with open(ARCHIVO_CSV, "r", newline="", encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo)
            # Verificamos que el encabezado es el que esperamos
            if lector.fieldnames != CAMPOS:
                print("Error: el encabezado del CSV no tiene el formato esperado.")
                return paises
            # start=2 porque la fila 1 es el encabezado
            for numero_fila, fila in enumerate(lector, start=2):
                try:
                    nombre = fila["nombre"].strip()
                    continente = fila["continente"].strip()
                    poblacion = int(fila["poblacion"])
                    superficie = int(fila["superficie"])
                    # Si algún dato es inválido, lanzamos ValueError a propósito para omitir la fila
                    if not nombre or not continente or poblacion < 0 or superficie <= 0:
                        raise ValueError
                    paises.append({"nombre": nombre, "poblacion": poblacion,
                                   "superficie": superficie, "continente": continente})
                except (ValueError, TypeError, AttributeError):
                    print(f"Aviso: se omitió la fila {numero_fila} por tener datos inválidos.")
    except FileNotFoundError:
        print(f"No se encontró {ARCHIVO_CSV}. Se creará al guardar los datos.")
    except OSError as error:
        print(f"No se pudo leer el archivo: {error}")
    return paises


def guardar_paises(paises):
    """Guarda la lista completa en el archivo CSV"""

    try:
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(paises)
        return True
    except OSError as error:
        print(f"No se pudo guardar el archivo: {error}")
        return False


# ------------------------------------------
# FUNCIONALIDADES DEL SISTEMA
# ------------------------------------------

def mostrar_paises(lista):
    """Muestra una lista de países con el total al final"""

    if not lista:
        print("No hay países para mostrar.")
        return

    print("\n--- LISTADO DE PAÍSES ---")

    for p in lista:
        print("------------------------------")
        print("Nombre:", p["nombre"])
        print("Población:", p["poblacion"])
        print("Superficie:", p["superficie"], "km2")
        print("Continente:", p["continente"])

    print("------------------------------")
    print("Total de países:", len(lista))

def agregar_pais(paises):
    """Agrega un país nuevo (sin campos vacíos ni nombres repetidos) y guarda el CSV"""

    nombre = pedir_texto("Nombre: ")
    continente = pedir_texto("Continente: ")
    # Se compara normalizado para detectar duplicados aunque cambien mayúsculas o tildes
    if any(normalizar(p["nombre"]) == normalizar(nombre) for p in paises):
        print("Ya existe un país con ese nombre.")
        return
    poblacion = pedir_entero("Población: ", 0)
    superficie = pedir_entero("Superficie en km2: ", 1)
    paises.append({"nombre": nombre, "poblacion": poblacion,
                   "superficie": superficie, "continente": continente})
    if guardar_paises(paises):
        print("País agregado correctamente.")


def actualizar_pais(paises):
    """Actualiza población y superficie de un país existente."""
    nombre = normalizar(pedir_texto("Nombre del país a actualizar: "))
    for pais in paises:
        if normalizar(pais["nombre"]) == nombre:
            pais["poblacion"] = pedir_entero("Nueva población: ", 0)
            pais["superficie"] = pedir_entero("Nueva superficie en km2: ", 1)
            if guardar_paises(paises):
                print("Datos actualizados correctamente.")
            return
    print("No se encontró ese país.")


def buscar_pais(paises):
    """Busca países por nombre (coincidencia parcial o exacta)."""
    consulta = normalizar(pedir_texto("Nombre o parte del nombre: "))
    encontrados = [p for p in paises if consulta in normalizar(p["nombre"])]
    mostrar_paises(encontrados)


def filtrar_paises(paises):
    """Filtra países por continente, rango de población o rango de superficie."""
    print("1. Continente  2. Rango de población  3. Rango de superficie")
    opcion = input("Opción de filtro: ").strip()
    if opcion == "1":
        continente = normalizar(pedir_texto("Continente: "))
        resultado = [p for p in paises if normalizar(p["continente"]) == continente]
    elif opcion in ("2", "3"):
        minimo = pedir_entero("Valor mínimo: ", 0 if opcion == "2" else 1)
        maximo = pedir_entero("Valor máximo: ", minimo)
        clave = "poblacion" if opcion == "2" else "superficie"
        resultado = [p for p in paises if minimo <= p[clave] <= maximo]
    else:
        print("Opción de filtro inválida.")
        return
    mostrar_paises(resultado)


def ordenar_paises(paises):
    """Ordena países por nombre, población o superficie (ascendente o descendente)."""
    print("Ordenar por: 1. Nombre  2. Población  3. Superficie")
    opcion = input("Opción: ").strip()
    if opcion not in ("1", "2", "3"):
        print("Opción inválida.")
        return
    descendente = input("¿Descendente? (s/n): ").strip().lower()
    if descendente not in ("s", "n"):
        print("Ingresá s o n.")
        return
    claves = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    # Para el nombre se ordena el texto normalizado; para los números, el valor tal cual
    ordenados = sorted(paises, key=lambda p: normalizar(p[claves[opcion]])
                       if opcion == "1" else p[claves[opcion]],
                       reverse=(descendente == "s"))
    mostrar_paises(ordenados)


def mostrar_estadisticas(paises):
    """Muestra mayor/menor población, promedios y cantidad de países por continente."""
    if not paises:
        print("No hay datos para calcular estadísticas.")
        return
    mayor = max(paises, key=lambda p: p["poblacion"])
    menor = min(paises, key=lambda p: p["poblacion"])
    promedio_poblacion = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_superficie = sum(p["superficie"] for p in paises) / len(paises)
    # Diccionario que cuenta cuántos países hay por continente
    por_continente = {}
    for pais in paises:
        continente = pais["continente"]
        por_continente[continente] = por_continente.get(continente, 0) + 1
    print(f"Mayor población: {mayor['nombre']} ({mayor['poblacion']:,})")
    print(f"Menor población: {menor['nombre']} ({menor['poblacion']:,})")
    print(f"Promedio de población: {promedio_poblacion:,.2f}")
    print(f"Promedio de superficie: {promedio_superficie:,.2f} km2")
    print("Cantidad de países por continente:")
    for continente, cantidad in por_continente.items():
        print(f"  {continente}: {cantidad}")


# --------------------------
# MENÚ Y PROGRAMA PRINCIPAL
# --------------------------

def mostrar_menu():
    """Imprime las opciones del menú principal."""
    print("\n=== GESTIÓN DE PAÍSES ===")
    print("1. Lista de países")
    print("2. Agregar país")
    print("3. Actualizar población y superficie")
    print("4. Buscar por nombre")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Mostrar estadísticas")
    print("8. Guardar y salir")


def main():
    """Carga los datos y ejecuta el menú hasta que el usuario elija salir."""
    paises = cargar_paises()
    opcion = ""
    while opcion != "8":
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()
        if opcion == "1":
            mostrar_paises(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais(paises)
        elif opcion == "5":
            filtrar_paises(paises)
        elif opcion == "6":
            ordenar_paises(paises)
        elif opcion == "7":
            mostrar_estadisticas(paises)
        elif opcion == "8":
            if guardar_paises(paises):
                print("Datos guardados. Hasta luego.")
        else:
            print("Opción inválida. Elegí un número del menú.")


main()
# =============================================================
# TPI - Programación 1 | UTN - Tecnicatura en Programación
# Gestión de Datos de Países en Python
# =============================================================

import csv
import os

# Nombre del archivo de datos
ARCHIVO_CSV = "paises.csv"

# Campos del dataset
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]


# ============================================================
# LECTURA Y ESCRITURA DEL ARCHIVO CSV
# ============================================================

# Esta función básicamente recorre el CSV línea por línea
# y arma un diccionario por cada país. Si una fila tiene un campo vacío
# o un dato que no es número, no rompe el programa: la salta y avisa.
def cargar_paises(archivo):
    """
    Lee el archivo CSV y retorna una lista de diccionarios.
    Controla errores de formato y filas incompletas.
    """
    paises = []

    if not os.path.exists(archivo):
        print(f"[AVISO] El archivo '{archivo}' no existe. Se iniciará con lista vacía.")
        return paises

    try:
        with open(archivo, encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for numero_fila, fila in enumerate(lector, start=2):
                # Verificar que ningún campo esté vacío
                if not all(campo in fila and fila[campo].strip() != "" for campo in CAMPOS):
                    print(f"[ERROR] Fila {numero_fila} incompleta, se omite: {dict(fila)}")
                    continue
                try:
                    paises.append({
                        "nombre":     fila["nombre"].strip(),
                        "poblacion":  int(fila["poblacion"].strip()),
                        "superficie": int(fila["superficie"].strip()),
                        "continente": fila["continente"].strip()
                    })
                except ValueError:
                    print(f"[ERROR] Fila {numero_fila} con datos no numéricos, se omite: {dict(fila)}")

    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo CSV: {e}")

    return paises


def guardar_paises(paises, archivo):
    """
    Guarda la lista de diccionarios en el archivo CSV.
    """
    try:
        with open(archivo, "w", encoding="utf-8", newline="") as f:
            escritor = csv.DictWriter(f, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(paises)
        print(f"[OK] Datos guardados en '{archivo}'.")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo: {e}")


# ============================================================
# VISUALIZACIÓN
# ============================================================

def mostrar_paises(lista, titulo="Lista de países"):
    """
    Imprime una lista de países en formato de tabla con encabezado.
    """
    if not lista:
        print("  [INFO] No se encontraron países con ese criterio.")
        return

    print(f"\n  === {titulo} ({len(lista)} país/es) ===")
    print(f"  {'NOMBRE':<25} {'POBLACIÓN':>15} {'SUPERFICIE (km²)':>18} {'CONTINENTE':<15}")
    print("  " + "-" * 77)

    for p in lista:
        print(
            f"  {p['nombre']:<25} "
            f"{p['poblacion']:>15,} "
            f"{p['superficie']:>18,} "
            f"{p['continente']:<15}"
        )
    print()


# ============================================================
# VALIDACIÓN DE ENTRADAS DE USUARIO
# ============================================================

def pedir_texto(mensaje):
    """
    Solicita al usuario un texto no vacío. Repite hasta obtenerlo.
    """
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  [ERROR] Este campo no puede estar vacío. Intente nuevamente.")


def pedir_entero_positivo(mensaje):
    """
    Solicita al usuario un número entero positivo. Repite hasta obtenerlo.
    """
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("  [ERROR] Ingrese un número entero positivo válido (sin decimales ni letras).")


# ============================================================
# FUNCIONALIDAD 1: AGREGAR PAÍS
# ============================================================

def agregar_pais(paises):
    """
    Agrega un nuevo país a la lista.
    No permite campos vacíos ni países duplicados.
    """
    print("\n  ── AGREGAR PAÍS ──")

    nombre = pedir_texto("  Nombre del país: ")

    # Verificar duplicado
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"  [ERROR] El país '{nombre}' ya existe en el sistema.")
            return

    poblacion  = pedir_entero_positivo("  Población (hab.): ")
    superficie = pedir_entero_positivo("  Superficie (km²): ")
    continente = pedir_texto("  Continente: ")

    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    guardar_paises(paises, ARCHIVO_CSV)
    print(f" [OK] País '{nombre}' agregado y guardado correctamente.")


# ============================================================
# FUNCIONALIDAD 2: ACTUALIZAR PAÍS
# ============================================================

def actualizar_pais(paises):
    """
    Actualiza la población y la superficie de un país existente.
    """
    print("\n  ── ACTUALIZAR PAÍS ──")

    nombre = pedir_texto("  Nombre exacto del país a actualizar: ")

    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"\n  País encontrado: {p['nombre']}")
            print(f"  Población actual:  {p['poblacion']:,} hab.")
            print(f"  Superficie actual: {p['superficie']:,} km²")

            p["poblacion"] = pedir_entero_positivo(" Nueva población (hab.): ")
            p["superficie"] = pedir_entero_positivo(" Nueva superficie (km²): ")

guardar_paises(paises, ARCHIVO_CSV)

print(f" [OK] Datos de '{p['nombre']}' actualizados y guardados.")
return

    print(f"  [INFO] No se encontró el país '{nombre}'.")


# ============================================================
# FUNCIONALIDAD 3: BUSCAR PAÍS POR NOMBRE
# ============================================================

def buscar_pais(paises):
    """
    Busca países por coincidencia parcial o exacta del nombre.
    """
    print("\n  ── BUSCAR PAÍS ──")

    termino = pedir_texto("  Ingrese nombre o parte del nombre: ")

    resultados = [p for p in paises if termino.lower() in p["nombre"].lower()]

    mostrar_paises(resultados, f"Resultados para '{termino}'")


# ============================================================
# FUNCIONALIDAD 4: FILTROS
# ============================================================

def filtrar_por_continente(paises):
    """
    Filtra países que pertenecen al continente indicado.
    """
    print("\n  ── FILTRAR POR CONTINENTE ──")

    # Mostrar continentes disponibles
    continentes = sorted(set(p["continente"] for p in paises))
    print("  Continentes disponibles:", ", ".join(continentes))

    continente = pedir_texto("  Ingrese el continente: ")

    resultados = [p for p in paises if p["continente"].lower() == continente.lower()]

    mostrar_paises(resultados, f"Países en {continente.capitalize()}")


def filtrar_por_poblacion(paises):
    """
    Filtra países dentro de un rango de población (mínimo y máximo).
    """
    print("\n  ── FILTRAR POR RANGO DE POBLACIÓN ──")

    minimo = pedir_entero_positivo("  Población mínima: ")
    maximo = pedir_entero_positivo("  Población máxima: ")

    if minimo > maximo:
        print("  [ERROR] El mínimo no puede ser mayor que el máximo.")
        return

    resultados = [p for p in paises if minimo <= p["poblacion"] <= maximo]

    mostrar_paises(resultados, f"Países con población entre {minimo:,} y {maximo:,} hab.")


def filtrar_por_superficie(paises):
    """
    Filtra países dentro de un rango de superficie en km².
    """
    print("\n  ── FILTRAR POR RANGO DE SUPERFICIE ──")

    minimo = pedir_entero_positivo("  Superficie mínima (km²): ")
    maximo = pedir_entero_positivo("  Superficie máxima (km²): ")

    if minimo > maximo:
        print("  [ERROR] El mínimo no puede ser mayor que el máximo.")
        return

    resultados = [p for p in paises if minimo <= p["superficie"] <= maximo]

    mostrar_paises(resultados, f"Países con superficie entre {minimo:,} y {maximo:,} km²")


def menu_filtros(paises):
    """
    Submenú para elegir el tipo de filtro a aplicar.
    """
    print("\n  ── FILTRAR PAÍSES ──")
    print("  1. Por continente")
    print("  2. Por rango de población")
    print("  3. Por rango de superficie")
    print("  0. Volver al menú principal")

    opcion = input("  Seleccione una opción: ").strip()

    if opcion == "1":
        filtrar_por_continente(paises)
    elif opcion == "2":
        filtrar_por_poblacion(paises)
    elif opcion == "3":
        filtrar_por_superficie(paises)
    elif opcion == "0":
        return
    else:
        print("  [ERROR] Opción no válida.")


# ============================================================
# FUNCIONALIDAD 5: ORDENAMIENTOS
# ============================================================

# Acá sorted() no toca la lista original "paises", sino que
# devuelve una lista nueva ya ordenada. Por eso es seguro usarla para
# mostrar distintos órdenes sin perder el orden en que se cargó el CSV.
def ordenar_paises(paises):
    """
    Ordena y muestra la lista de países según el criterio elegido
    (nombre, población o superficie) en dirección ascendente o descendente.
    No modifica la lista original.
    """
    print("\n  ── ORDENAR PAÍSES ──")
    print("  ¿Por qué criterio?")
    print("  1. Nombre")
    print("  2. Población")
    print("  3. Superficie")
    print("  0. Volver")

    criterio = input("  Seleccione criterio: ").strip()

    claves = {"1": "nombre", "2": "poblacion", "3": "superficie"}

    if criterio == "0":
        return
    if criterio not in claves:
        print("  [ERROR] Opción no válida.")
        return

    clave = claves[criterio]

    print("  ¿En qué dirección?")
    print("  1. Ascendente (A→Z / menor a mayor)")
    print("  2. Descendente (Z→A / mayor a menor)")

    direccion = input("  Seleccione dirección: ").strip()

    if direccion not in ("1", "2"):
        print("  [ERROR] Opción no válida.")
        return

    reverso = (direccion == "2")

    # Para nombre usamos lower() para que el orden no dependa de mayúsculas
    if clave == "nombre":
        ordenados = sorted(paises, key=lambda p: p["nombre"].lower(), reverse=reverso)
    else:
        ordenados = sorted(paises, key=lambda p: p[clave], reverse=reverso)

    dir_texto = "descendente" if reverso else "ascendente"
    mostrar_paises(ordenados, f"Países ordenados por {clave} ({dir_texto})")


# ============================================================
# FUNCIONALIDAD 6: ESTADÍSTICAS
# ============================================================

def mostrar_estadisticas(paises):
    """
    Calcula y muestra estadísticas generales del dataset:
    - País con mayor y menor población
    - Promedio de población y superficie
    - Cantidad de países por continente
    """
    print("\n  ── ESTADÍSTICAS ──")

    if not paises:
        print("  [INFO] No hay datos suficientes para calcular estadísticas.")
        return

    # País con mayor y menor población
    mayor_pob = max(paises, key=lambda p: p["poblacion"])
    menor_pob = min(paises, key=lambda p: p["poblacion"])

    # Promedios
    total_paises  = len(paises)
    promedio_pob  = sum(p["poblacion"]  for p in paises) / total_paises
    promedio_sup  = sum(p["superficie"] for p in paises) / total_paises

    # Cantidad por continente usando diccionario
    por_continente = {}
    for p in paises:
        cont = p["continente"]
        por_continente[cont] = por_continente.get(cont, 0) + 1

    print(f"\n  Total de países registrados: {total_paises}")
    print(f"\n  País con MAYOR población: {mayor_pob['nombre']} "
          f"({mayor_pob['poblacion']:,} hab.)")
    print(f"  País con MENOR población: {menor_pob['nombre']} "
          f"({menor_pob['poblacion']:,} hab.)")
    print(f"\n  Promedio de población:  {promedio_pob:,.0f} hab.")
    print(f"  Promedio de superficie: {promedio_sup:,.0f} km²")

    print("\n  Países por continente:")
    for cont, cantidad in sorted(por_continente.items()):
        print(f"    • {cont}: {cantidad} país/es")

    print()


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def mostrar_menu():
    """
    Imprime el menú principal de opciones en consola.
    """
    print("\n" + "=" * 52)
    print("   GESTIÓN DE DATOS DE PAÍSES  |  UTN Prog. 1")
    print("=" * 52)
    print("  1. Ver todos los países")
    print("  2. Agregar un país")
    print("  3. Actualizar datos de un país")
    print("  4. Buscar país por nombre")
    print("  5. Filtrar países")
    print("  6. Ordenar países")
    print("  7. Ver estadísticas")
    print("  0. Guardar y salir")
    print("=" * 52)


def main():
    """
    Punto de entrada del programa.
    Carga los datos y ejecuta el bucle principal del menú.
    """
    print("\n  Bienvenido al sistema de gestión de países - UTN TPI")

    paises = cargar_paises(ARCHIVO_CSV)
    print(f"  [OK] {len(paises)} países cargados desde '{ARCHIVO_CSV}'.")

    # Mapa de opciones → funciones
    acciones = {
        "1": lambda: mostrar_paises(paises, "Todos los países"),
        "2": lambda: agregar_pais(paises),
        "3": lambda: actualizar_pais(paises),
        "4": lambda: buscar_pais(paises),
        "5": lambda: menu_filtros(paises),
        "6": lambda: ordenar_paises(paises),
        "7": lambda: mostrar_estadisticas(paises),
    }

    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción: ").strip()

        if opcion == "0":
            guardar_paises(paises, ARCHIVO_CSV)
            print("  ¡Hasta luego!\n")
            break
        elif opcion in acciones:
            acciones[opcion]()
        else:
            print("  [ERROR] Opción no válida. Intente nuevamente.")


# Punto de entrada
if __name__ == "__main__":
    main()

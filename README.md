#  Gestión de Datos de Países en Python

**Trabajo Práctico Integrador (TPI) | Programación 1**  
**Tecnicatura Universitaria en Programación — UTN (A Distancia)**

---

##  Descripción

Aplicación de consola desarrollada en **Python 3** que permite gestionar un dataset de países del mundo. El sistema lee y escribe datos desde un archivo CSV, y ofrece un menú interactivo con funcionalidades de búsqueda, filtrado, ordenamiento y estadísticas.

---

##  Integrantes

|Luca Vaccaro|
|Rosario Mallon|


---

##  Requisitos

- Python **3.8** o superior
- No se requieren librerías externas (solo módulos de la biblioteca estándar: `csv`, `os`)

---

##  Cómo ejecutar el programa

1. Clonar o descargar el repositorio.
2. Asegurarse de que `paises.py` y `paises.csv` estén en la **misma carpeta**.
3. Abrir una terminal en esa carpeta y ejecutar:

```bash
python paises.py
```

> En algunos sistemas puede ser necesario usar `python3 paises.py`

---

##  Estructura del repositorio

```
TPI-Paises-Python/
│
├── paises.py          # Código fuente principal del programa
├── paises.csv         # Dataset base con países del mundo
├── README.md          # Este archivo
└── documentacion.pdf  # Informe académico del proyecto
```

---

##  Dataset (paises.csv)

Cada fila representa un país con los siguientes campos:

| Campo | Tipo | Descripción |
|---|---|---|
| `nombre` | string | Nombre del país |
| `poblacion` | int | Cantidad de habitantes |
| `superficie` | int | Superficie en km² |
| `continente` | string | Continente al que pertenece |

**Ejemplo:**
```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```

---

##  Funcionalidades del sistema

### Menú principal

```
====================================================
   GESTIÓN DE DATOS DE PAÍSES  |  UTN Prog. 1
====================================================
  1. Ver todos los países
  2. Agregar un país
  3. Actualizar datos de un país
  4. Buscar país por nombre
  5. Filtrar países
  6. Ordenar países
  7. Ver estadísticas
  0. Guardar y salir
====================================================
```

### Detalle de opciones

**1. Ver todos los países**
Muestra el dataset completo en formato de tabla.

**2. Agregar un país**
Solicita nombre, población, superficie y continente. No permite campos vacíos ni países duplicados.

**3. Actualizar un país**
Busca el país por nombre exacto y permite modificar su población y superficie.

**4. Buscar por nombre**
Busca por coincidencia parcial o exacta (no distingue mayúsculas/minúsculas).

**5. Filtrar países**
- Por continente
- Por rango de población (mín. y máx.)
- Por rango de superficie (mín. y máx.)

**6. Ordenar países**
- Por nombre, población o superficie
- Ascendente o descendente

**7. Estadísticas**
- País con mayor y menor población
- Promedio de población y de superficie
- Cantidad de países por continente

---

##  Ejemplos de entrada/salida

### Buscar un país
```
Ingrese nombre o parte del nombre: arg

  === Resultados para 'arg' (1 país/es) ===
  NOMBRE                     POBLACIÓN   SUPERFICIE (km²)  CONTINENTE
  ─────────────────────────────────────────────────────────────────
  Argentina               45.376.763        2.780.400      América
```

### Filtrar por continente
```
Ingrese el continente: Europa

  === Países en Europa (11 país/es) ===
  NOMBRE                     POBLACIÓN   SUPERFICIE (km²)  CONTINENTE
  ...
```

### Estadísticas
```
  Total de países registrados: 42

  País con MAYOR población: China (1.402.112.000 hab.)
  País con MENOR población: Uruguay (3.518.552 hab.)

  Promedio de población:  168.543.200 hab.
  Promedio de superficie: 1.843.291 km²

  Países por continente:
    • África: 9 país/es
    • América: 12 país/es
    • Asia: 11 país/es
    • Europa: 8 país/es
    • Oceanía: 2 país/es
```

---

##  Validaciones implementadas

- Campos vacíos bloqueados en toda entrada de usuario.
- Datos no numéricos detectados y rechazados.
- Filas del CSV con formato inválido son ignoradas con mensaje de aviso.
- Países duplicados no permitidos al agregar.
- Rango inválido (mínimo > máximo) detectado en filtros.
- Búsquedas sin resultados informadas con mensaje claro.

---

## Decisiones de diseño

- El programa guarda los cambios en el CSV automáticamente al agregar
  o actualizar un país, además de al salir, para no perder información
  si la consola se cierra de forma inesperada.

---

##  Documentación y Video

- 📄 **Informe PDF:** [Enlace al PDF o subido en la raíz del repositorio]
- 🎥 **Video demostrativo:** [Pegar aquí el link de YouTube/Drive con acceso público]

---

## 📚 Conceptos aplicados

- Listas y diccionarios (estructuras de datos)
- Funciones con responsabilidad única
- Estructuras condicionales y repetitivas
- Lectura y escritura de archivos CSV (módulo `csv`)
- Ordenamiento con `sorted()` y funciones lambda
- Estadísticas básicas (máximo, mínimo, promedio, conteo)
- Manejo de errores con `try/except`

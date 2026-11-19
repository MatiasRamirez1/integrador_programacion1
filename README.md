# Sistema de Gestión de Países 🌎

## 1. Descripción del programa

El proyecto consiste en un sistema de gestión de países desarrollado en Python, que permite administrar información mediante un menú interactivo por consola.

El programa trabaja con un archivo CSV (`paises.csv`) donde almacena los datos de cada país: nombre, población, superficie y continente.

A través de las diferentes opciones del menú, el usuario puede consultar, agregar, actualizar, buscar, filtrar y ordenar países, además de obtener estadísticas generales.

## 2. Instrucciones de uso

### Requisitos

- Tener Python 3 instalado.
- No requiere instalar librerías externas, ya que utiliza el módulo `csv`, incluido en Python.

### Ejecución

1. Descargar el proyecto y guardar sus archivos en una misma carpeta.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

4. Una vez iniciado el programa, aparecerá el menú principal:

```text
=== GESTIÓN DE PAÍSES ===
1. Lista de países
2. Agregar país
3. Actualizar población y superficie
4. Buscar por nombre
5. Filtrar países
6. Ordenar países
7. Mostrar estadísticas
8. Guardar y salir

Elegí una opción:
```

5. Ingresar el número correspondiente a la operación deseada y seguir las instrucciones que aparecen en pantalla.
6. Para finalizar, seleccionar la opción 8. Los datos se guardarán en el archivo CSV.

**Nota:** Si el archivo `paises.csv` no existe al iniciar el programa, se informará por pantalla y se creará automáticamente cuando se guarden los datos.

## 3. Ejemplos de entradas y salidas

### Ejemplo 1: Agregar un país

**Entrada:**

```text
Elegí una opción: 2
Nombre: Argentina
Continente: América
Población: 46000000
Superficie en km2: 2780400
```

**Salida:**

```text
País agregado correctamente.
```

### Ejemplo 2: Buscar un país

**Entrada:**

```text
Elegí una opción: 4
Nombre o parte del nombre: arg
```

**Salida:**

```text
--- LISTADO DE PAÍSES ---
------------------------------
Nombre: Argentina
Población: 46000000
Superficie: 2780400 km2
Continente: América
------------------------------
Total de países: 1
```

### Ejemplo 3: Validación de datos

**Entrada:**

```text
Elegí una opción: 2
Nombre: Argentina
Continente: América
```

**Salida:**

```text
Ya existe un país con ese nombre.
```

El sistema evita registrar países duplicados, incluso cuando se utilizan diferencias de mayúsculas, minúsculas o tildes.

### Ejemplo 4: Mostrar estadísticas

**Salida de ejemplo:**

```text
Mayor población: Argentina (46,000,000)
Menor población: Uruguay (3,500,000)
Promedio de población: 24,750,000.00
Promedio de superficie: 1,500,000.00 km2
Cantidad de países por continente:
  América: 2
```

*Los valores son ilustrativos y dependen de los países registrados en el archivo CSV.*

## 4. Participación de los integrantes

El proyecto fue desarrollado en conjunto por los siguientes integrantes: Matías Ramirez y Gonzalo Larraburú.
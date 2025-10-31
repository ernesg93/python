# 🧠 **Profundizando en PROGRAMACIÓN FUNCIONAL: Lambdas y Closures**

## 🎯 **LAMBDA FUNCTIONS (Funciones Anónimas)**

### **¿QUÉ SON?**
# Funciones sin nombre, definidas en una sola línea.

#python
# Sintaxis básica
# lambda argumentos: expresion
#

### **EJEMPLOS PRÁCTICOS:**

#python
# 1. Función simple
cuadrado = lambda x: x ** 2

# print(cuadrado(5))  # 25

# 2. Múltiples parámetros
suma = lambda a, b: a + b
multiplicar = lambda x, y, z: x * y * z

# 3. Con condicionales
es_par = lambda n: True if n % 2 == 0 else False
absoluto = lambda x: x if x >= 0 else -x

# print(es_par(4))
# print(absoluto(-3))
#

### **DIFERENCIA vs FUNCIONES NORMALES:**

#python
# Lambda (anónima)
cuadrado = lambda x: x ** 2

# Función normal
def cuadrado(x):
    return x ** 2

# Ambas hacen lo mismo, pero lambda es más concisa
#

### **USOS COMUNES DE LAMBDA:**

#### **A. Con `map()` - Aplicar función a cada elemento**
#python
numeros = [1, 2, 3, 4, 5]

# Duplicar cada número
duplicados = list(map(lambda x: x * 2, numeros))

# print(duplicados)
# [2, 4, 6, 8, 10]

# Convertir a string
strings = list(map(lambda x: f"Numero: {x}", numeros))

# print(strings)
# ['Numero: 1', 'Numero: 2', 'Numero: 3', 'Numero: 4', 'Numero: 5']
#

#### **B. Con `filter()` - Filtrar elementos**
#python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solo pares
pares = list(filter(lambda x: x % 2 == 0, numeros))

# [2, 4, 6, 8, 10]

# Mayores que 5
grandes = list(filter(lambda x: x > 5, numeros))

# [6, 7, 8, 9, 10]
#

#### **C. Con `sorted()` - Ordenamiento personalizado**
#python
personas = [("Ana", 25), ("Juan", 30), ("Maria", 20)]

# Ordenar por edad
por_edad = sorted(personas, key=lambda persona: persona[1])

# print(por_edad)
# [('Maria', 20), ('Ana', 25), ('Juan', 30)]

# Ordenar por longitud del nombre
por_nombre = sorted(personas, key=lambda persona: len(persona[0]))

# print(por_nombre)
# [('Ana', 25), ('Juan', 30), ('Maria', 20)]
#

## 🏰 **CLOSURES (Cierres)**

### **¿QUÉ SON?**
# Funciones que **recuerdan** el entorno donde fueron creadas, incluso después de que ese entorno haya terminado.

### **ANATOMÍA DE UN CLOSURE:**

#python
def fabrica_saludo(prefijo):
    # ↑
    # Función externa (outer function)
    
    def saludar(nombre):
        # ↑
        # Función interna (inner function) - ESTE ES EL CLOSURE
        return print(f"{prefijo} {nombre}!")
    
    return saludar  # ← Devuelve la función, no la ejecuta

# masculino = fabrica_saludo("El Dios")
# femenino = fabrica_saludo("La Diosa")
# masculino("Ernesto")
# femenino("Danelis")
#

### **EJEMPLO PASO A PASO:**

#python
# 1. Crear el closure
def crear_contador():
    cuenta = 0  # Variable "recordada"
    
    def incrementar():
        nonlocal cuenta  # Permite modificar la variable externa
        cuenta += 1
        return cuenta
    
    return incrementar

# 2. Usarlo
mi_contador = crear_contador()

# print(mi_contador())  # 1
# print(mi_contador())  # 2
# print(mi_contador())  # 3

# Cada closure mantiene SU PROPIO estado
# otro_contador = crear_contador()

# print(otro_contador())  # 1 (independiente del primero)
#

### **CLOSURES EN EL MUNDO REAL:**

#### **A. Fabricas de Funciones Personalizadas**
#python
def crear_potencia(exponente):
    def potencia(base):
        return base ** exponente
    return potencia

# Crear funciones específicas
cuadrado = crear_potencia(2)
cubo = crear_potencia(3)

# print(cuadrado(5))  # 25
# print(cubo(3))      # 27
#

#### **B. Configuración de Comportamiento**
#python
def crear_validador(minimo, maximo):
    def validar(valor):
        return minimo <= valor <= maximo
    return validar

# Validadores específicos
es_edad_valida = crear_validador(0, 120)
es_porcentaje = crear_validador(0, 100)

# print(es_edad_valida(25))    # True
# print(es_porcentaje(150))    # False
#

#### **C. Callbacks con Estado**
#python
def crear_reintentos(intentos_maximos):
    intentos = 0
    
    def reintentar():
        nonlocal intentos
        if intentos < intentos_maximos:
            intentos += 1
            return f"Intento {intentos} de {intentos_maximos}"
        return "Límite alcanzado"
    
    return reintentar

reintentar_3_veces = crear_reintentos(3)
reintentar_2_veces = crear_reintentos(2)

# print(reintentar_2_veces())  # "Intento 1 de 2"
# print(reintentar_2_veces())  # "Intento 2 de 2"
# print(reintentar_2_veces())  # "Límite alcanzado"
# print(reintentar_3_veces())  # "Intento 1 de 3"
# print(reintentar_3_veces())  # "Intento 2 de 3"
# print(reintentar_3_veces())  # "Intento 3 de 3"
# print(reintentar_3_veces())  # "Límite alcanzado"
#

## 🔥 **COMBINANDO LAMBDA + CLOSURES**

### **EL CÓDIGO "MÁGICO" EXPLICADO:**

#python
# La fábrica de validadores de triángulos
is_compliant = lambda eq_sides, less_or_equal: lambda sides: (
    sides.count(0) == 0 and 
    max(sides) <= sum(sides) / 2 and 
    (len(set(sides)) <= eq_sides if less_or_equal else len(set(sides)) == eq_sides)
)

# Desglosado en funciones normales:
def crear_validador_triangulo(eq_sides, less_or_equal):
    def validador(sides):
        # Validación básica
        if sides.count(0) > 0:
            return False
        
        # Desigualdad triangular
        if max(sides) > sum(sides) / 2:
            return False
        
        # Condición de lados únicos
        lados_unicos = len(set(sides))
        if less_or_equal:
            return lados_unicos <= eq_sides
        else:
            return lados_unicos == eq_sides
    
    return validador
#

# ### **¿POR QUÉ USAR ESTE PATRÓN?**

# #### **VENTAJAS:**
# 1. **DRY (Don't Repeat Yourself)**: La lógica de validación se escribe una vez
# 2. **Flexibilidad**: Fácil crear nuevas variantes
# 3. **Encapsulación**: El estado se mantiene privado
# 4. **Composabilidad**: Puedes combinar closures

# #### **DESVENTAJAS:**
# 1. **Legibilidad**: Puede ser confuso para principiantes
# 2. **Debugging**: Más difícil de depurar
# 3. **Performance**: Pequeña sobrecarga vs funciones simples

## 🎨 **PATRONES AVANZADOS**

### **A. DECORADORES (Usando Closures)**
#python
def mi_decorador(funcion_original):
    def funcion_envuelta(*args, **kwargs):
        print("Antes de ejecutar")
        resultado = funcion_original(*args, **kwargs)
        print("Después de ejecutar")
        return resultado
    return funcion_envuelta

@mi_decorador
def saludar(nombre):
    print(f"Hola {nombre}")

# saludar("Juan")
# Antes de ejecutar
# Hola Juan
# Después de ejecutar
#

### **B. FUNCIONES DE ORDEN SUPERIOR**
#python
def aplicar_operaciones(datos, *operaciones):
    """Aplica múltiples operaciones a los datos"""
    resultados = []
    for operacion in operaciones:
        resultados.append(operacion(datos))
    return resultados

# Usando lambdas como operaciones
datos = [1, 2, 3, 4, 5]
resultados = aplicar_operaciones(
    datos,
    lambda x: sum(x),           # Suma total
    lambda x: max(x),           # Máximo
    lambda x: [n*2 for n in x]  # Duplicados
)

# print(resultados)
# [15, 5, [2, 4, 6, 8, 10]]
#

# ## 💡 **BUENAS PRÁCTICAS**

# ### **CUÁNDO USAR LAMBDAS:**
# - ✅ Operaciones simples de una línea
# - ✅ Callbacks y funciones de orden superior
# - ✅ Cuando la legibilidad no se ve afectada

# ### **CUÁNDO USAR CLOSURES:**
# - ✅ Cuando necesitas "recordar" estado entre llamadas
# - ✅ Para crear fábricas de funciones
# - ✅ Para implementar decoradores
# - ✅ Cuando quieres encapsular lógica compleja

# ### **CUÁNDO EVITARLOS:**
# - ❌ Lógica compleja (usa funciones normales)
# - ❌ Cuando reduce la legibilidad
# - ❌ Para código que otros desarrolladores deben mantener

# **¿Quieres que practiquemos con ejercicios específicos de lambdas y closures?** 😊
# ¡Excelente pregunta! Los `*` en los parámetros de funciones son **operadores de desempaquetado** y tienen diferentes significados según su posición:

## 📚 **TIPOS DE `*` EN PARÁMETROS:**

### **1. `*args` - RECIBIR MÚLTIPLES ARGUMENTOS POSICIONALES**


def funcion(*args):
    # args es una TUPLA con todos los argumentos posicionales
    print(f"Tipo: {type(args)}")  # <class 'tuple'>
    print(f"Contenido: {args}")

# Ejemplos:
funcion(1, 2, 3)           # args = (1, 2, 3)
funcion("a", "b")          # args = ('a', 'b')
funcion()                  # args = ()


# **Ejemplo práctico:**

def sumar(*numeros):
    return sum(numeros)

print(sumar(1, 2, 3))      # 6
print(sumar(5, 10, 15, 20)) # 50
print(sumar())             # 0


### **2. `**kwargs` - RECIBIR MÚLTIPLES ARGUMENTOS POR NOMBRE**


def funcion(**kwargs):
    # kwargs es un DICCIONARIO con argumentos clave=valor
    print(f"Tipo: {type(kwargs)}")  # <class 'dict'>
    print(f"Contenido: {kwargs}")

# Ejemplos:
funcion(nombre="Ana", edad=25)    # kwargs = {'nombre': 'Ana', 'edad': 25}
funcion(x=1, y=2, z=3)           # kwargs = {'x': 1, 'y': 2, 'z': 3}
funcion()                        # kwargs = {}


# **Ejemplo práctico:**

def crear_perfil(**datos):
    perfil = {"nombre": "Desconocido", "edad": 0}
    perfil.update(datos)  # Actualiza con los datos proporcionados
    return perfil

print(crear_perfil(nombre="Juan", edad=30, ciudad="Madrid"))
# {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}


### **3. COMBINANDO `*args` Y `**kwargs`**


def funcion_completa(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

funcion_completa(1, 2, 3, 4, 5, x=10, y=20)
# a: 1, b: 2
# args: (3, 4, 5)
# kwargs: {'x': 10, 'y': 20}


## 🔄 **`*` Y `**` PARA LLAMAR FUNCIONES (DESEMPAQUETAR)**

### **4. `*` PARA DESEMPAQUETAR ITERABLES**


def funcion(a, b, c):
    return a + b + c

# Sin desempaquetar
funcion(1, 2, 3)  # 6

# Con desempaquetar
lista = [1, 2, 3]
funcion(*lista)   # 6 - Equivale a funcion(1, 2, 3)

tupla = (4, 5, 6)
funcion(*tupla)   # 15 - Equivale a funcion(4, 5, 6)


### **5. `**` PARA DESEMPAQUETAR DICCIONARIOS**


def funcion(nombre, edad, ciudad):
    return f"{nombre} tiene {edad} años y vive en {ciudad}"

# Sin desempaquetar
funcion("Ana", 25, "Madrid")

# Con desempaquetar
datos = {"nombre": "Juan", "edad": 30, "ciudad": "Barcelona"}
funcion(**datos)  # Equivale a funcion(nombre="Juan", edad=30, ciudad="Barcelona")


## 🎯 **EJEMPLOS PRÁCTICOS AVANZADOS:**

### **A. FUNCIÓN QUE ENVUELVE OTRAS FUNCIONES**

def ejecutar_con_log(funcion, *args, **kwargs):
    print(f"Ejecutando {funcion.__name__}...")
    resultado = funcion(*args, **kwargs)
    print(f"Resultado: {resultado}")
    return resultado

def sumar(a, b):
    return a + b

ejecutar_con_log(sumar, 5, 3)
# Ejecutando sumar...
# Resultado: 8


### **B. CREAR FUNCIONES FLEXIBLES**

def crear_html(tag, *contenido, **atributos):
    # Construir atributos
    attrs = " ".join(f'{k}="{v}"' for k, v in atributos.items())
    if attrs:
        attrs = " " + attrs
    
    # Construir contenido
    inner = "".join(contenido)
    
    return f"<{tag}{attrs}>{inner}</{tag}>"

print(crear_html("div", "Hola Mundo", class_="container", id="main"))
# <div class="container" id="main">Hola Mundo</div>

print(crear_html("p", "Texto", " más texto", style="color: red"))
# <p style="color: red">Texto más texto</p>


### **C. EN NUESTRO EJEMPLO ANTERIOR:**

def aplicar_operaciones(datos, *operaciones):
    # operaciones es una tupla de funciones lambda
    resultados = []
    for operacion in operaciones:
        resultados.append(operacion(datos))
    return resultados

# operaciones recibe: (lambda1, lambda2, lambda3)


## ⚠️ **REGLAS IMPORTANTES:**

### **ORDEN EN PARÁMETROS:**

def funcion(a, b, *args, c=10, **kwargs):
    # 1. Parámetros normales (a, b)
    # 2. *args (argumentos posicionales extra)
    # 3. Parámetros con valor por defecto (c=10)
    # 4. **kwargs (argumentos nombrados extra)
    pass


### **NO PERMITIDO:**

# ❌ Esto NO funciona
def funcion(*args, a, b):  # Error!
    pass

# ✅ Esto SÍ funciona  
def funcion(a, b, *args):  # Correcto
    pass


## 💡 **RESUMEN:**

# - **`*args`**: Recibe múltiples argumentos posicionales como tupla
# - **`**kwargs`**: Recibe múltiples argumentos nombrados como diccionario  
# - **`*lista`**: Desempaqueta iterables en argumentos posicionales
# - **`**dict`**: Desempaqueta diccionarios en argumentos nombrados

# **¿Quieres que practiquemos con ejemplos específicos?** 😊
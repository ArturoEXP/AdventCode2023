numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

linea = "3fiveone"
resultado = ""

# Procesar cada palabra en la línea
palabras = linea.split()
print(palabras)
for palabra in palabras:
    # Si la palabra está en el diccionario, agregar su valor al resultado
    if palabra.lower() in numbers:
        resultado += str(numbers[palabra.lower()])
        print("if",resultado)
    else:
        # Si no está en el diccionario, agregar la palabra sin cambios al resultado
        resultado += palabra
        print("else",resultado)

print(resultado)
nombre = input("¿Cuál es tu nombre?:")
nombre=nombre.capitalize()
nombre=nombre.strip()
nombre = nombre.replace("e", "o")
print(nombre)
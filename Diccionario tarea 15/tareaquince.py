# Tarea: Trabajando con Diccionarios en Python

# Diccionario
print("=== DICCIONARIO ===")

# Creamos un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Benjamin",
    "Apellido": "López",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero de Software"
}

# Muestra el diccionario original
print("Diccionario original:", informacion_personal)

# Accedemos y modificamos el valor de la clave de la ciudad
informacion_personal["ciudad"] = "Guayaquil"  # Se actualiza la ciudad
print("Después de modificar la ciudad:", informacion_personal)

# Agregar una nueva clave-valor para la profesión
informacion_personal["profesion"] = "Ingeniero Civil"  # Se cambia la profesión de Ingeniero de Software a Ingeniero Civil
print("Después de modificar la profesión:", informacion_personal)

# Verificamos si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "098-765-4321"  # Número de teléfono ficticio agregado
    print("Se ha agregado el teléfono:", informacion_personal)
else:
    print("El teléfono ya está presente en el diccionario:", informacion_personal)

# Eliminar la clave "edad" del diccionario porque no es necesaria
del informacion_personal["edad"]  # Elimina la edad
print("Después de eliminar 'edad':", informacion_personal)

# Borrar todo el diccionario
informacion_personal.clear()
print("Después de limpiar el diccionario:", informacion_personal)



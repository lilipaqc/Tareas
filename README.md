# Tarea: Trabajando con Diccionarios en Python

def crear_informacion_personal():
    # Crear un diccionario con información personal ficticia
    informacion_personal = {
        "nombre": "Benjamin", 
        "Apellido": "López",  
        "edad": 30,
        "ciudad": "Quito",
        "profesion": "Ingeniero de Software"
    }

    # Acceder y modificar el valor de la clave "ciudad"
    informacion_personal["ciudad"] = "Guayaquil"  # Se actualiza la ciudad

    # Agregar una nueva clave-valor para la "profesion" (ya está incluida, pero la modificamos por ejemplo)
    informacion_personal["profesion"] = "Desarrollador Web"  # Actualizamos la profesión

    # Verificar si la clave "telefono" existe en el diccionario
    if "telefono" not in informacion_personal:
        informacion

# Tarea de trabajo con archivos de texto en python

# Primero hacemos la escritura del archivo
# Se crea el archivo my_notes.txt en modo escritura ('w')
file = open('my_notes.txt', 'w')

# Escribo 3 líneas de notas personales
file.write("Agradecida con mis docentes por todo lo que me han enseñado.\n")
file.write("En este semestre he aprendido sobre las bases de la programación.\n")
file.write("Gracias a la Universidad Estatal Amazónica por darme la oportunidad de estudiar.\n")

# Es importante que cerremos el archivo
file.close()

# Para la lectura del archivo
# Se abre el archivo en modo lectura ('r')
file = open('my_notes.txt', 'r')

# Para leer el contenido del archivo línea por línea usamos readlines()
lines = file.readlines()

# Imprimimos cada línea
print("Contenido del archivo my_notes.txt:")
for line in lines:
    print(line, end='')  # usamos end para que no se añada una nueva línea

# Importante que cerramos el archivo después de leer
file.close()





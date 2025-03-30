def temperatura_promedio(ciudades_temperaturas):
    temperaturas_promedio = {}
    for ciudad, semanas in ciudades_temperaturas.items():
        promedios_semanales = []
        for semana in semanas:
            suma_temperaturas = sum([dia["temp"] for dia in semana])
            promedio = suma_temperaturas / len(semana)
            promedios_semanales.append(promedio)
        temperaturas_promedio[ciudad] = promedios_semanales
    return temperaturas_promedio

# Datos de temperaturas para cada ciudad y semana
ciudades_temperaturas = {
    "Quito": [
        [{"day": "Lunes", "temp": 8}, {"day": "Martes", "temp": 9}, {"day": "Miércoles", "temp": 10}, {"day": "Jueves", "temp": 12}, {"day": "Viernes", "temp": 15}, {"day": "Sábado", "temp": 17}, {"day": "Domingo", "temp": 19}],
        [{"day": "Lunes", "temp": 8}, {"day": "Martes", "temp": 9}, {"day": "Miércoles", "temp": 11}, {"day": "Jueves", "temp": 12}, {"day": "Viernes", "temp": 14}, {"day": "Sábado", "temp": 16}, {"day": "Domingo", "temp": 18}],
        [{"day": "Lunes", "temp": 7}, {"day": "Martes", "temp": 8}, {"day": "Miércoles", "temp": 9}, {"day": "Jueves", "temp": 11}, {"day": "Viernes", "temp": 13}, {"day": "Sábado", "temp": 16}, {"day": "Domingo", "temp": 18}],
        [{"day": "Lunes", "temp": 7}, {"day": "Martes", "temp": 8}, {"day": "Miércoles", "temp": 10}, {"day": "Jueves", "temp": 11}, {"day": "Viernes", "temp": 13}, {"day": "Sábado", "temp": 15}, {"day": "Domingo", "temp": 18}]
    ],
    "Guayaquil": [
        [{"day": "Lunes", "temp": 24}, {"day": "Martes", "temp": 26}, {"day": "Miércoles", "temp": 28}, {"day": "Jueves", "temp": 30}, {"day": "Viernes", "temp": 32}, {"day": "Sábado", "temp": 31}, {"day": "Domingo", "temp": 29}],
        [{"day": "Lunes", "temp": 25}, {"day": "Martes", "temp": 27}, {"day": "Miércoles", "temp": 29}, {"day": "Jueves", "temp": 31}, {"day": "Viernes", "temp": 32}, {"day": "Sábado", "temp": 30}, {"day": "Domingo", "temp": 28}],
        [{"day": "Lunes", "temp": 24}, {"day": "Martes", "temp": 26}, {"day": "Miércoles", "temp": 28}, {"day": "Jueves", "temp": 30}, {"day": "Viernes", "temp": 31}, {"day": "Sábado", "temp": 29}, {"day": "Domingo", "temp": 27}],
        [{"day": "Lunes", "temp": 25}, {"day": "Martes", "temp": 27}, {"day": "Miércoles", "temp": 29}, {"day": "Jueves", "temp": 30}, {"day": "Viernes", "temp": 32}, {"day": "Sábado", "temp": 30}, {"day": "Domingo", "temp": 28}]
    ],
    "Manta": [
        [{"day": "Lunes", "temp": 22}, {"day": "Martes", "temp": 24}, {"day": "Miércoles", "temp": 26}, {"day": "Jueves", "temp": 28}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 29}, {"day": "Domingo", "temp": 28}],
        [{"day": "Lunes", "temp": 23}, {"day": "Martes", "temp": 25}, {"day": "Miércoles", "temp": 27}, {"day": "Jueves", "temp": 29}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 28}, {"day": "Domingo", "temp": 27}],
        [{"day": "Lunes", "temp": 22}, {"day": "Martes", "temp": 24}, {"day": "Miércoles", "temp": 26}, {"day": "Jueves", "temp": 28}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 29}, {"day": "Domingo", "temp": 27}],
        [{"day": "Lunes", "temp": 23}, {"day": "Martes", "temp": 25}, {"day": "Miércoles", "temp": 27}, {"day": "Jueves", "temp": 29}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 28}, {"day": "Domingo", "temp": 26}]
    ]
}

# Llamadamos a la función para calcular los promedios
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

#Para imprimir los promedios por ciudad y semana 
print("Temperaturas Promedio por Ciudad "
"(Semana 1, Semana 2, Semana 3, Semana 4):")

# Nombres de las semanas
print(f"{'Ciudad':<12} {'Semana 1':<10} {'Semana 2':<10} {'Semana 3':<10} {'Semana 4':<10}")
for ciudad, promedios in temperaturas_promedio.items():
    print(f"{ciudad:<12} {promedios[0]:<10.2f} {promedios[1]:<10.2f} {promedios[2]:<10.2f} {promedios[3]:<10.2f}")


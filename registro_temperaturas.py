#Matriz 3D para almacenar datos de temperaturas de 3 ciudades de Ecuador
# Primera dimensión: Ciudades (Quito, Guayaquil, Manta)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)

temperaturas = [
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 8},
            {"day": "Martes", "temp": 9},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 8},
            {"day": "Martes", "temp": 9},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 7},
            {"day": "Martes", "temp": 8},
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 18}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 7},
            {"day": "Martes", "temp": 8},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 18}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 28}
        ]
    ],
    [   # Manta
        [   # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 26}
        ]
    ]
]

# Calculamos el promedio de temperaturas para cada ciudad y semana
ciudades = ["Quito", "Guayaquil", "Manta"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")

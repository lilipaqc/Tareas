# Definición de la función con parámetros
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calculamos el descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    # Devolver el monto del descuento calculado
    return descuento

# Llamadamos a la función del monto total
monto_total = 8000  # Ejemplo de monto total
descuento = calcular_descuento(monto_total)  #Llamada con el descuento predeterminado
monto_final = monto_total - descuento
print(f"Monto Total: ${monto_total}")
print(f"Descuento: ${descuento}")
print(f"Monto Final a cancelar: ${monto_final}")

# Llamadamos a la función con monto y el descuento personalizado
monto_total2 = 5000
descuento2 = calcular_descuento(monto_total2, 20)  #Con el 20% de descuento
monto_final2 = monto_total2 - descuento2
print(f"\nMonto Total: ${monto_total2}")
print(f"Descuento: ${descuento2}")
print(f"Monto Final a Pagar: ${monto_final2}")
  


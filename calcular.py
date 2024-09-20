# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Función principal
def main():
    # Primera llamada a la función: usando solo el monto total (descuento predeterminado del 10%)
    monto_total_1 = 500.00  # Ejemplo de monto total
    descuento_1 = calcular_descuento(monto_total_1)
    monto_final_1 = monto_total_1 - descuento_1
    print(f"Monto total: ${monto_total_1:.2f}")
    print(f"Descuento aplicado: ${descuento_1:.2f}")
    print(f"Monto final a pagar: ${monto_final_1:.2f}")

    # Segunda llamada a la función: proporcionando tanto el monto total como el porcentaje de descuento
    monto_total_2 = 200.00  # Otro ejemplo de monto total
    porcentaje_descuento_2 = 15  # Descuento del 15%
    descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
    monto_final_2 = monto_total_2 - descuento_2
    print(f"\nMonto total: ${monto_total_2:.2f}")
    print(f"Descuento aplicado ({porcentaje_descuento_2}%): ${descuento_2:.2f}")
    print(f"Monto final a pagar: ${monto_final_2:.2f}")


# Ejecutar la función principal
if __name__ == "__main__":
    main()

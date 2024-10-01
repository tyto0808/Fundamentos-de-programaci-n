# Abrimos el archivo en modo escritura (creando uno nuevo si no existe)
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas
    file.write("Primera nota: Recuerdame comprar pan.\n")
    file.write("Segunda nota: Recuerdame comprar leche.\n")
    file.write("Tercera nota: Recuerdame hacer los deberes.\n")

# Abrimos el archivo en modo lectura
with open('my_notes.txt', 'r') as file:
    # Leemos el archivo línea por línea
    for line in file:
        # Imprimimos cada línea en la consola
        print(line.strip())
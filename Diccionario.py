# Crear un diccionario ficticio llamado "informacion_personal"
informacion_personal = {
    "nombre": "Joseph Mendoza",  # Nombre de la persona
    "edad": 20,                  # Edad de la persona
    "ciudad": "Pedernales",          # Ciudad actual de la persona
    "profesion": "Biologia"  # Profesión inicial de la persona
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Santo Domingo"  # Cambiamos "Santo Domingo" por "Pedernales"

# Modificar la profesión de la persona
informacion_personal["profesion"] = "Biologo"  # Cambiamos la profesión a "Biologo"

# Verificar si la clave "telefono" existe; si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "3219876543"  # Agregamos un número de teléfono ficticio

# Eliminar la clave "edad" ya que no es necesaria
del informacion_personal["edad"]

# Imprimir el diccionario resultante después de las modificaciones
print(informacion_personal)

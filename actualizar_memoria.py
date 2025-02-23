import json

# Leer comandos.txt
with open("comandos.txt", "r") as f:
    lineas = f.readlines()

# Extraer el último comando válido
for linea in reversed(lineas):
    if linea.startswith("ACTUALIZAR_MEMORIA"):
        _, json_data = linea.split(" ", 1)
        nuevo_evento = json.loads(json_data)
        break
else:
    raise ValueError("No se encontró un comando válido en comandos.txt")

# Leer memoria.json
with open("memoria.json", "r") as f:
    memoria = json.load(f)

# Agregar el nuevo evento
memoria["historia"].append(nuevo_evento)

# Guardar los cambios en memoria.json
with open("memoria.json", "w") as f:
    json.dump(memoria, f, indent=4, ensure_ascii=False)

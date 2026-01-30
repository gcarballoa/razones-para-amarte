import json
import random

# 1. Base de datos de frases manuales (Las que ya tenemos)
# Nota: Aquí deberías pegar la lista de las 70 que ya redactamos arriba
mensajes_base = [
    {"id": i+1, "categoria": "manual", "texto": f"Razón manual {i+1}"} 
    for i in range(70) 
]

# 2. Componentes para el "Motor de Sentimientos"
estructuras = [
    "Me encanta cuando {accion} porque {resultado}.",
    "Gracias por {verbo_ing} {complemento}, me haces sentir {emocion}.",
    "Admiro profundamente tu capacidad de {habilidad}, es algo que {efecto}.",
    "Eres mi persona favorita porque {razon_directa}.",
    "Qué suerte la mía de {infinitivo} a alguien que {detalle_unico}."
]

acciones = [
    {"accion": "te ríes sin control", "resultado": "tu alegría ilumina todo mi entorno"},
    {"accion": "me hablas de tus sueños", "resultado": "me contagias tus ganas de comerte el mundo"},
    {"accion": "te concentras en lo que haces", "resultado": "admiro la pasión que le pones a la vida"},
    {"accion": "me buscas en silencio", "resultado": "siento una conexión que no necesita palabras"}
]

agradecimientos = [
    {"verbo": "estar", "complemento": "presente en mis peores días", "emocion": "totalmente sostenido/a"},
    {"verbo": "creer", "complemento": "en nosotros sin dudar", "emocion": "con una seguridad inmensa"},
    {"verbo": "cuidar", "complemento": "nuestros pequeños rituales", "emocion": "la persona más especial"}
]

detalles = [
    "siempre sabe cómo hacerme sonreír",
    "tiene la palabra justa en el momento indicado",
    "no tiene miedo de mostrarse tal cual es",
    "hace que lo difícil parezca sencillo a su lado"
]

def generar_razon(id_actual):
    tipo = random.randint(1, 5)
    
    if tipo == 1:
        item = random.choice(acciones)
        texto = estructuras[0].format(**item)
    elif tipo == 2:
        item = random.choice(agradecimientos)
        texto = estructuras[1].format(verbo_ing=item["verbo"], complemento=item["complemento"], emocion=item["emocion"])
    elif tipo == 3:
        habilidades = ["escuchar con el corazón", "encontrar belleza en lo simple", "mantener la calma en el caos"]
        efectos = ["me inspira cada día", "atesoro profundamente", "hace que te admire más"]
        texto = estructuras[2].format(habilidad=random.choice(habilidades), efecto=random.choice(efectos))
    elif tipo == 4:
        razones = ["haces que mi hogar sea una persona y no un lugar", "contigo el futuro no da miedo", "tu bondad no tiene límites"]
        texto = estructuras[3].format(razon_directa=random.choice(razones))
    else:
        infinitivos = ["haber conocido", "compartir mi vida", "caminar"]
        texto = estructuras[4].format(infinitivo=random.choice(infinitivos), detalle_unico=random.choice(detalles))
        
    return {"id": id_actual, "categoria": "generada_pro", "texto": texto}

# 3. Generación final
total_objetivo = 365
while len(mensajes_base) < total_objetivo:
    nueva_razon = generar_razon(len(mensajes_base) + 1)
    # Evitar duplicados exactos en la misma corrida
    if nueva_razon["texto"] not in [m["texto"] for m in mensajes_base]:
        mensajes_base.append(nueva_razon)

# 4. Exportar
with open('razones_365.json', 'w', encoding='utf-8') as f:
    json.dump({"total": 365, "mensajes": mensajes_base}, f, ensure_ascii=False, indent=2)

print("Archivo razones_365.json generado con éxito.")
import json
import urllib.request
import os

CIUDADES = [
    {
        "nombre": "Hermosillo",
        "lat": 29.0729,
        "lon": -110.9559,
    },
    {
        "nombre": "Guadalajara",
        "lat": 20.6597,
        "lon": -103.3496,
    },
]

resultado = []

for ciudad in CIUDADES:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={ciudad['lat']}&longitude={ciudad['lon']}"
        "&current=temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m"
        "&daily=sunrise,sunset"
        "&timezone=auto"
    )

    with urllib.request.urlopen(url) as response:
        data = json.load(response)

    current = data["current"]
    daily = data["daily"]

    resultado.append({
        "nombre": ciudad["nombre"],
        "temperatura": current["temperature_2m"],
        "sensacion": current["apparent_temperature"],
        "humedad": current["relative_humidity_2m"],
        "viento": current["wind_speed_10m"],
        "actualizado": current["time"],
        "amanecer": daily["sunrise"][0],
        "atardecer": daily["sunset"][0],
    })

output = {"ciudades": resultado}

ruta_data = os.path.join(os.path.dirname(__file__), "..", "data.json")
with open(ruta_data, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("Listo, data.json creado con estos datos:")
print(output)
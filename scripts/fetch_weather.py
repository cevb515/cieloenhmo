import json
import urllib.request

LATITUDE = 29.0729
LONGITUDE = -110.9559

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={LATITUDE}&longitude={LONGITUDE}"
    "&current=temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m"
    "&timezone=America/Hermosillo"
)

with urllib.request.urlopen(url) as response:
    data = json.load(response)

current = data["current"]

output = {
    "temperatura": current["temperature_2m"],
    "sensacion": current["apparent_temperature"],
    "humedad": current["relative_humidity_2m"],
    "viento": current["wind_speed_10m"],
    "actualizado": current["time"],
}

import os
ruta_data = os.path.join(os.path.dirname(__file__), "..", "data.json")
with open(ruta_data, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("Listo, data.json creado con estos datos:")
print(output)
import yaml
import json
from pathlib import Path

current_dir = Path(__file__).parent

# --- 1) YAML -> JSON ---

# Elimizde bir YAML config'i olduğunu varsayalım (Docker Compose / K8s tarzı).
# Gerçek bir dosya yerine string üzerinden örnekliyoruz, ama yaml.safe_load()
# hem string hem de dosya nesnesiyle (f.read() ya da direkt f ile) çalışır.
yaml_text = """
service: weather-api
port: 8080
env:
  - name: WEATHER_API_KEY
    required: true
replicas: 3
"""

# yaml.safe_load() -> YAML metnini Python dict/list yapısına çevirir.
# "safe" olanı kullanıyoruz çünkü yaml.load() güvensiz nesneleri de
# deserialize edebilir (kötü niyetli bir YAML dosyası kod çalıştırabilir).
config = yaml.safe_load(yaml_text)
print("YAML'dan okunan dict:")
print(config)

# dict elimize geçtikten sonra json.dump ile diske JSON olarak yazabiliriz.
json_output_path = current_dir / "config_from_yaml.json"
with open(json_output_path, "w") as f:
    json.dump(config, f, indent=2)
print(f"\nJSON dosyası yazıldı: {json_output_path.name}")

# --- 2) JSON -> YAML ---

# Şimdi tersini yapalım: bir JSON verisini (mesela bir API'den gelen dict)
# YAML formatına çevirelim.
data = {
    "city": "Kayseri",
    "temperature": 28.5,
    "status": "acik",
    "coordinates": {"lat": 37.966461, "lon": 34.662479},
}

yaml_output_path = current_dir / "data_from_json.yaml"
with open(yaml_output_path, "w") as f:
    # allow_unicode=True olmazsa Türkçe karakterler \uXXXX kaçış kodu olarak yazılır.
    # default_flow_style=False -> iç içe {} yerine okunaklı girintili YAML üretir.
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False)
print(f"YAML dosyası yazıldı: {yaml_output_path.name}")

with open(yaml_output_path) as f:
    print("\nYazılan YAML dosyasının içeriği:")
    print(f.read())

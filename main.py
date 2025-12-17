import os
import json
import requests

# Variables d'environnement
endpoint = os.getenv("VISION_ENDPOINT")
subscription_key = os.getenv("VISION_KEY")


if not endpoint or not subscription_key:
    raise RuntimeError("Missing VISION_ENDPOINT or VISION_KEY")

# URL Computer Vision
vision_url = f"{endpoint}/vision/v3.2/analyze"

# Image à analyser
image_url = (
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1hEuGfRL7DJLZYWDSbgmubhGSbpvDQzIdsA&s"
)

headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/json"
}

params = {
    "visualFeatures": "Tags,Objects,Description"
}

response = requests.post(
    vision_url,
    headers=headers,
    params=params,
    json={"url": image_url}
)

response.raise_for_status()

# Résultat
result = response.json()
print(json.dumps(result, indent=2))

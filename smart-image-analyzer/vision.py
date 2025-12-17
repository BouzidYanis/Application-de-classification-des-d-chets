import requests
import os

endpoint = os.getenv("VISION_ENDPOINT")
key = os.getenv("VISION_KEY")

analyze_url = f"{endpoint}/vision/v3.2/analyze"

headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Content-Type": "application/octet-stream"
}

params = {
    "visualFeatures": "Tags,Objects,Description"
}

def analyze_image(image_bytes):
    response = requests.post(
        analyze_url,
        headers=headers,
        params=params,
        data=image_bytes
    )
    if not response.ok:
        # Remonte une erreur lisible pour le frontend
        raise RuntimeError(f"Vision API error ({response.status_code}): {response.text}")
    response.raise_for_status()
    return response.json()

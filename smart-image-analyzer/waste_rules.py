def classify_waste(tags):
    tags = [tag.lower() for tag in tags]

    if any(t in tags for t in ["plastic", "bottle"]):
        return "Plastique", "Recycle dans le bac jaune ♻️"

    if any(t in tags for t in ["paper", "cardboard", "box"]):
        return "Papier / Carton", "Recycle dans le bac bleu 📦"

    if any(t in tags for t in ["can", "metal", "aluminum"]):
        return "Métal", "Recycle avec les métaux 🔩"

    if any(t in tags for t in ["food", "banana", "apple"]):
        return "Déchet organique", "Compost 🌱"

    return "Déchet inconnu", "Vérifie les règles locales"

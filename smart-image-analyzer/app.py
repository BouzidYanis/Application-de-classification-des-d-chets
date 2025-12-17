import os
from flask import Flask, render_template, request, flash
from dotenv import load_dotenv
from vision import analyze_image
from waste_rules import classify_waste

load_dotenv()

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image = request.files.get("image")
        if not image:
            flash("Aucune image fournie.", "error")
            return render_template("index.html")
        try:
            analysis = analyze_image(image.read())
            tags = [t["name"] for t in analysis.get("tags", [])]
            waste_type, advice = classify_waste(tags)
            return render_template("result.html", tags=tags, waste_type=waste_type, advice=advice)
        except Exception as e:
            flash(f"Erreur d’analyse: {e}", "error")
            return render_template("index.html")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

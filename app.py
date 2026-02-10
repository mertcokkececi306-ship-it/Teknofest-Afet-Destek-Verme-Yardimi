from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sonuc = None

    if request.method == "POST":
        try:
            nufus = int(request.form["nufus"])
            hasar = int(request.form["hasar"])
            saglik = int(request.form["saglik"])

            # Skor hesaplama (ağırlıklı)
            skor = (hasar * 5) + (saglik * 4) + (nufus * 0.5)

            if skor >= 60:
                seviye = "ACİL"
            elif skor >= 30:
                seviye = "ORTA"
            else:
                seviye = "DÜŞÜK"

            sonuc = {
                "skor": int(skor),
                "seviye": seviye
            }

        except Exception as e:
            sonuc = {
                "skor": 0,
                "seviye": "HATA"
            }

    return render_template("index.html", sonuc=sonuc)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

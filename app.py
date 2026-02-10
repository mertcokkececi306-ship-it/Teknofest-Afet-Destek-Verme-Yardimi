from flask import Flask, render_template, request

app = Flask(__name__)

def normalize(deger, max_deger):
    return deger / max_deger

def oncelik_hesapla(nufus, hasar, saglik):
    n = normalize(nufus, 10000)
    h = normalize(hasar, 10)
    s = normalize(saglik, 10)

    skor = (s * 0.4) + (h * 0.35) + (n * 0.25)
    return round(skor, 3)

def seviye_belirle(skor):
    if skor >= 0.7:
        return "ACİL", "red"
    elif skor >= 0.4:
        return "ORTA", "orange"
    else:
        return "DÜŞÜK", "green"

@app.route("/", methods=["GET", "POST"])
def index():
    sonuc = None

    if request.method == "POST":
        nufus = int(request.form["nufus"])
        hasar = int(request.form["hasar"])
        saglik = int(request.form["saglik"])

        skor = oncelik_hesapla(nufus, hasar, saglik)
        seviye, renk = seviye_belirle(skor)

        sonuc = {
            "skor": skor,
            "seviye": seviye,
            "renk": renk
        }

    return render_template("index.html", sonuc=sonuc)

if __name__ == "__main__":
    app.run(debug=True)

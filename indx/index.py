from flask import Flask, render_template

app = Flask(__name__)


@app.route("/b")
def inicio():
    numero = 3 + 2
    return render_template("index.html", calculo=numero)


@app.route("/")
def contacto():
    return render_template("ornitorrinco.html")


@app.route("/nosotros")
def nosotros():
    return ""
 

@app.route("/calculadora/<nacimiento>")
def calculadora(nacimiento=None):
    anio_actual = 2020
    edad = anio_actual - int(nacimiento)
    return render_template(
        "calculadora.html", edad=edad, anio_actual=anio_actual, nacimiento=nacimiento
    )


app.run(debug=True)
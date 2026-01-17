from flask import Flask, render_template, request

app = Flask(__name__)

# --------------------
# MENÚ PRINCIPAL
# --------------------
@app.route("/")
def index():
    return render_template("index.html")


# --------------------
# EJERCICIO 1
# PROMEDIO Y ASISTENCIA
# --------------------
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None

    if request.method == "POST":
        try:
            n1 = float(request.form["n1"])
            n2 = float(request.form["n2"])
            n3 = float(request.form["n3"])
            asistencia = int(request.form["asistencia"])

            promedio = (n1 + n2 + n3) / 3

            if promedio >= 4 and asistencia >= 75:
                resultado = f"Aprobado (Promedio: {promedio:.1f})"
            else:
                resultado = f"Reprobado (Promedio: {promedio:.1f})"

        except:
            resultado = "Error en los datos ingresados"

    return render_template("ejercicio1.html", resultado=resultado)


# --------------------
# EJERCICIO 2
# NOMBRE CON MÁS CARACTERES
# --------------------
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    nombre_mayor = None
    cantidad = None

    if request.method == "POST":
        nombre1 = request.form["nombre1"].strip()
        nombre2 = request.form["nombre2"].strip()
        nombre3 = request.form["nombre3"].strip()

        nombres = [nombre1, nombre2, nombre3]

        nombre_mayor = max(nombres, key=len)
        cantidad = len(nombre_mayor)

    return render_template(
        "ejercicio2.html",
        nombre_mayor=nombre_mayor,
        cantidad=cantidad
    )


# --------------------
# EJECUCIÓN
# --------------------
if __name__ == "__main__":
    app.run(debug=True)

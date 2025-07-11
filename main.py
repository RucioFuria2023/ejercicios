from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            promedio = (nota1 + nota2 + nota3) / 3
            estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

            resultado = {
                'promedio': round(promedio, 2),
                'estado': estado
            }
        except ValueError:
            resultado = {
                'error': "Por favor, ingresa valores numéricos válidos."
            }
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        nombres = [
            request.form['nombre1'],
            request.form['nombre2'],
            request.form['nombre3']
        ]
        nombre_mas_largo = max(nombres, key=len)
        resultado = {
            'nombre': nombre_mas_largo,
            'longitud': len(nombre_mas_largo)
        }

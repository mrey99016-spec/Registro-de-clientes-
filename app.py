from flask import Flask, render_template, request

app = Flask(__name__)

clientes = []
pedidos = []

@app.route('/')
def index():
    return render_template('index.html', clientes=clientes, pedidos=pedidos)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        telefono = request.form.get('telefono')
        correo = request.form.get('correo')
        if not nombre or not telefono or not correo:
            return render_template('index.html', error1='Todos los campos son obligatorios', clientes=clientes, pedidos=pedidos)
        clientes.append({'nombre': nombre, 'telefono': telefono, 'correo': correo})
        return render_template('index.html', exito1='Cliente registrado!', clientes=clientes, pedidos=pedidos)
    return render_template('index.html', clientes=clientes, pedidos=pedidos)

@app.route('/pedido', methods=['GET', 'POST'])
def pedido():
    if request.method == 'POST':
        cliente = request.form.get('cliente')
        comida = request.form.get('comida')
        cantidad = request.form.get('cantidad')
        if not cliente or not comida or not cantidad:
            return render_template('index.html', error2='Todos los campos son obligatorios', clientes=clientes, pedidos=pedidos)
        pedidos.append({'cliente': cliente, 'comida': comida, 'cantidad': cantidad})
        return render_template('index.html', exito2='Pedido guardado!', clientes=clientes, pedidos=pedidos)
    return render_template('index.html', clientes=clientes, pedidos=pedidos)

if __name__ == '__main__':
    app.run(debug=True)

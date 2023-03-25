from flask import Flask, render_template, url_for, request, redirect
import requests

app = Flask(__name__)

pedidosInfo = requests.get('http://4.216.88.64:1880/transporte/pedidosDis')
pedidosInfo = pedidosInfo.json()


@app.route('/home', methods=['GET'])
def index():
    if request.method == 'POST':
        try:
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        return render_template('index.html')
    
@app.route('/listar', methods=['GET'])
def index():
    content = content = pedidosInfo
    if request.method == 'POST':
        try:
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        return render_template('index.html', content = content)

@app.route('/actualizar/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'GET':
        return render_template('crear.html')
    else:
        try:
            info = request.get_json()
            checkTransporte = requests.get('http://4.216.88.64:1880/transporte/check?pedido='+ id)
            if(checkTransporte == '400'):
                backResponse = requests.post('http://4.216.88.64:1880/transporte?pedido='+ info)
            return redirect('/')
        except:
            return backResponse

@app.route('/crear/<int:id>', methods=['GET', 'POST'])
def crear(id):
    if request.method == 'GET':
        content = pedidosInfo
        return render_template('crear.html', content=content)
    else:
        try:
            info = request.get_json()
            checkTransporte = requests.get('http://4.216.88.64:1880/transporte/check?pedido='+ id)
            if(checkTransporte == '400'):
                backResponse = requests.post('http://4.216.88.64:1880/transporte?pedido='+ info)
            return redirect('/')
        except:
            return backResponse

        
    
if __name__ == "__main__":
    app.run(debug=True)

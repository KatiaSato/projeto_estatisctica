from scipy.stats import poisson
from flask import Flask, render_template, request, jsonify

#criar uma instância para a classe FastAPI
app = Flask(__name__) 

#Definir um decorador de rota, que será responsável por tratar as requisições que vão para a rota “ / ” usando o operador get
@app.route('/')

#iremos definir a função da rota
def index():
    
#e retornar o conteúdo,
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])    
def calcular():
    tipo = request.form.get('tipo')
    lambd = float(request.form.get('lambda'))
    k = int(request.form.get('k'))
    
    if tipo == 'pontual':
        resultado = poisson.pmf(k, lambd) 
    elif tipo == 'cumulativa':       
        resultado = poisson.cdf(k, lambd)
    else:
        return jsonify({'erro': 'Tipo inválido'})
    return jsonify({'resultado': round(resultado, 6)})

if __name__ == '__main__':
    app.run(debug=True)
        

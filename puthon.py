from flask import Flask, request,jsonify
app = Flask(__name__)


@app.route('/',methods=['GET'])
def home():
    return{'message':'Bem vindo a minha API'}

@app.route('/users',methods=['POST','GET'])
def create_user():
    data = request.get_json()
    return {'message':'Usuário criado com sucesso'}

if __name__ == '__main__':
    app.run(debug='True')
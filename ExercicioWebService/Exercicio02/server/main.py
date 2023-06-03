from flask import Flask, request
from BancoDados import *
import Users

app = Flask(__name__)

@app.route("/user/", methods=["POST"])
def AddUser():

    banco = MockBancoDados()
    jsonRequest = request.get_json()

    nickname = jsonRequest["nickname"]
    password = jsonRequest["password"]
    plan = jsonRequest["plan"]

    user = Users.User(nickname, password, plan)

    isValid = banco.VerifyUser(user.nickname)
    retorno = banco.FindUser(user.nickname)

    if(retorno != None or not(isValid)):
        return {
            'status':200, 
            'message':'Usuário inválido', 
            'data':[]
        }

    banco.AddUser(user)

    return {
        'status':200, 
        'message': 'Usuário adicionado com sucesso!', 
        'data':[{
            'nickName': user.nickname
        }]
    }

@app.route('/user/delete/', methods=["POST"])
def RemoveUser():
    jsonRequest = request.get_json()

    nickname = jsonRequest["nickname"]
    password = jsonRequest["password"]

    banco = MockBancoDados()

    user = Users.User(nickname, password, 0)

    res = banco.RemoveUser(user)

    if(res):
        return {
                'status':200,
                'message':'Usuário removido com sucesso',
                'data':[]
        }
    
    return {
        'status':200,
        'message':'Usuário ou senha incorreta',
        'data':[]
    }
    



app.run()
from flask import Flask, request
from source.BancoDados import *
import source.Users as Users
from services.Clock import Hour
from services.Advice import Advice

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

@app.route("/user/<nickname>", methods=["GET"])
def FindUser(nickname):
    banco = MockBancoDados()
    res = banco.FindUser(nickname=nickname)
    if(res != None):
        return {
            "status" : 200,
            "message" : "",
            "data" : [{
                "nickname" : res["nickname"],
                "plan" : res["plan"]
            }]        
        }

    return {
        "status" : 200,
        "message" : "Usuário não encontrado",
        "data" : []        
    }

@app.route("/hour", methods=["POST"])
def returnHour():
    ID_UFNCAO_HOUR = 1445
    jsonRequest = request.get_json()
    nickname = jsonRequest["nickname"]
    password = jsonRequest["password"]

    banco = MockBancoDados()
    res = banco.validateUser(nickname, password)
    if(banco.CanDoThat(res["data"], ID_UFNCAO_HOUR)):
        return {
            "status" : 200,
            "message" : "",
            "data" : [Hour.now()]
        }
    return {
        "status" : 200,
        "message" : "Usuário não possui permissão para utilizar essa função. Faça um upgrade de plano.",
        "data" : []
    }


@app.route("/advice/", methods=["POST"])
def get_advice():
    ID_FUNCAO_ADVICE = 2445

    jsonRequest = request.get_json()
    nickname = jsonRequest["nickname"]
    password = jsonRequest["password"]

    de = request.args.get("autor")

    banco = MockBancoDados()
    res = banco.validateUser(nickname, password)
    if(banco.CanDoThat(res["data"], ID_FUNCAO_ADVICE)):
        return {
            "status" : 200,
            "message" : "",
            "data" : Advice.request_api_advice(de)["frases"]
        }
    return {
        "status" : 200,
        "message" : "Usuário não possui permissão para utilizar essa função. Faça um upgrade de plano.",
        "data" : []
    }

@app.route("/country/<IdentificadorPais>", methods=["POST"])
def get_info_country(IdentificadorPais):
    ID_FUNCAO_COUNTRY = 3445
    return {
        "status" : 200,
        "message" : "",
        "data" : [] 
    }





app.run()
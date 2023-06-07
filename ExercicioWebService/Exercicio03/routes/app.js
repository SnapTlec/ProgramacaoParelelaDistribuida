var CriptCarteira = require("../source/CriptoCarteira")
var User = require("../source/User")
var Banco = require("../source/BancoDados")
var Token = require("../source/token")

var express = require('express'); 
var router = express.Router();

//Criar uma CriptoCarteira
router.post('/wallet', function (req, res, next) {
    var tk = req.headers.token
    console.log(tk)
    var user = new Token().validarToken(tk)
    console.log(user)
    

    if(!user.tokenValid){
        return res.send({
            status : 200,
            message : user,
            data : []
        })
    }

    var money= req.body.money
    const user_found = Banco.FindUser(user.data.nome)
    if(!user_found){
        return res.send( {
            status : 200,
            message : "Nome ou senha incorreto",
            data : []
        })
    }

    const carteira = new CriptCarteira(user.data)
    var res_aporte = carteira.depositar(money)
    if(!res_aporte){
        return res.send({
            status:200,
            message : "O valor mínimo de depósito é R$: 50,00.",
            data: []
        })
    }
    Banco.AddWallet(carteira)
    return res.send({
        status : 200,
        message: "Carteira criada com sucesso!",
        data : {
            ID: carteira.ID,
            titular : carteira.owner.nome,
            money : carteira.saldo
        }
    })

});

//Criar um usuário
router.post("/user", function(req, res, next){
    var nome = req.body.name
    var password= req.body.password

    const user =  new User(nome,password)
    var found_user = Banco.FindUser(user)
    
    if(found_user){
        res.send( {
            status : 200,
            message : "Nome inválido ou já está sendo usuado por outro usuário!",
            data : []
        })
    }
    Banco.AddUser(user)

    res.send({
        status : 200,
        message : "Usuário Criado com sucesso!",
        data : {
            nome : user.nome
        }
    })

});

//Recuperar usuários cadastrados
router.get("/user", function(req, res, next){
    res.send({
        status: 200,
        message: "",
        data : Banco.users
    })
})

//Recuperar carteiras criadas
router.get("/wallet", function(req, res, next){
    res.send({
        status: 200,
        message : "",
        data : Banco.wallets
    })
})

// Deletar uma carteira cadastrada
router.post("/wallet/delete", function(req, res, next){
    var nome = req.params.ID
    var password = req.data

    const user = new User(nome, password)
    console.log(user)
    const found = Banco.authUser(user)
    console.log(found)
    if(found){
        if(Banco.RemoveWallet(user))
        res.send({
            status : 200,
            message : "",
            data : []
        })
    }
    res.send({
        status : 200,
        message : "Não foi possível remover a carteira",
        data : []
    })
})

//Realizar login no sistema e opter um token de validacao
//Tempo de valdade é 5min
router.post("/login", function(req, res, next){
    var nome = req.body.name
    var password = req.body.password
    const user = new User(nome, password)
    console.log(user)
    
    if(!Banco.authUser(user)){
        return res.send({
            status : 200,
            message : "Usuário ou senha inválida!",
            data : []
        })
    }
    var token = new Token().gerarToken(user)
    return res.send({
        status: 200,
        message: "",
        data: {
            token : token
        }
    })
})

//Realizar deposito na carteira
router.post("/wallet/deposito", function(req, res, next){
    return res.send(200)
})

router.get("/wallet/sacar", function(req, res, next){
    return res.send(req.params.token)
})

module.exports = router;
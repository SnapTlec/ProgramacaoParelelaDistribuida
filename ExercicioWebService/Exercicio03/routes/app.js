var CriptCarteira = require("../source/CriptoCarteira")
var express = require('express'); 
var router = express.Router();

router.post('/wallet', function (req, res, next) {
    const VALOR_MINIMO_APORTE = 50.00
    nome = req.body.name
    password = req.body.password
    money = req.body.money

    if(nome || password){
        return {
            status : 200,
            message : "Nome ou senha incorreto",
            data : []
        }
    }
    if(money < VALOR_MINIMO_APORTE){
        return {
            status : 200,
            message : "O valor de aporte não pode ser menor do que R$:50,00",
            data : []
        }
    }

    const owner =  {
        nome : nome,
        password : password
    }

    const carteira = CriptCarteira(owner, money)

});

module.exports = router;
var crypto = require('node:crypto');
class CriptCarteira{
    constructor(){
        this.ID = crypto.randomBytes(20).toString('hex');
        this.saldo = 0
    }
    atribuir_owner(user){
        if(!user.nome || !user.password){
            return false
        }
        this.owner = user
        return true
    }
    depositar(valor) {
        const VALOR_MINIMO_APORTE = 50.00
        if(valor < VALOR_MINIMO_APORTE){
            return false
        }
        this.saldo += valor
        return true

    }
    sacar(valor){
        var saldoAtual = this.saldo
        if(saldoAtual < valor){
            return false
        }
        novoSaldo = saldoAtual - valor
        var deuCerto = this.atualizarValorSaldo(novoSaldo)
        if(deuCerto){
            return true
        }
        return false
    }
    atualizarValorSaldo(valor){
        if(valor < 0){
            return false
        }
        this.saldo = valor
        return true
    }
}

module.exports = CriptCarteira
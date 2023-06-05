export default class CriptCarteira{
    constructor(owner, aporte){
        this.saldo = aporte
        this.owner = owner
    }
    depositar(valor) {
        if(valor > 0){
            this.saldo += valor
            return true
        }
        return false
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
var { Buffer }  = require ('node:buffer')
const User = require('./User');
const Banco = require('./BancoDados')


class Token{
    constructor(){
        this.SECRET = "N4_n01t3_ma1s_s0mbr14"
        this.TIMEOUT_SESSION=300000
    }

    gerarToken(user){
        if(!user){
            return false
        }
        var auth_string = user.nome + "." + user.password
        var secret = this.SECRET
        var time = new Date().getTime().toString()

        var auth_cifrado = Buffer.from(auth_string).toString('base64');
        var secret_cifrado = Buffer.from(secret).toString('base64');
        var time_cifrado = Buffer.from(time).toString('base64')

        var token_criptografia = secret_cifrado + "." +  time_cifrado + "." + auth_cifrado

        return token_criptografia
    }

    validarToken(token){
        if(!token){
            return false
        }
        var token_cifrado_split = token.split(".")
        var token_split = []
        token_cifrado_split.forEach(part_cifra => {
            const buff = Buffer.from(part_cifra, 'base64').toString('ascii')
            token_split.push(buff)
        })
        var secret = token_split[0]

        if(secret != ""){
            return {
                tokenValid : false,
                message : "Token Inválido"
            }
        }
        var time_now = new Date().getTime().toString()
        var time_init_login = parseInt(token_split[1])
        var tempo_sessao = time_now - time_init_login
        
        if(tempo_sessao >= this.TIMEOUT_SESSION){
            return {
                tokenValid : true,
                message : "Sua sessão expirou. Timeout!"
            }
        }
        var auth_string = token_split[2]
        var auth_string_split = auth_string.split(".")

        var nome = auth_string_split[0]
        var password = auth_string_split[1]

        const user = new User(nome, password)
        if(Banco.authUser(user)){
            return {
                tokenValid : true,
                message: ""
            }
        }

        return {
            tokenValid : false,
            message : "Erro não tratado!"
        };
    }
}

module.exports = Token
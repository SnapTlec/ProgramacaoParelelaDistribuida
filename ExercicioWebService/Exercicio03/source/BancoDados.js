class BancoDados{
    static wallets = []
    static users = []

    static AddWallet(wallet){
        this.wallets.push(wallet)
    }
    static AddUser(user){
        if(!user){
            return false
        }
        var res = this.FindUser(user.nome)
        if(res){
            return false
        }
        this.users.push(user)
        return true
    }
    static RemoveWallet(user){
        const WALLET_NOT_FOUND = -1
        const wallet = this.wallets.find(element => element.owner.nome == user.nome)
        const index = this.wallets.indexOf(wallet)
        if(index == WALLET_NOT_FOUND){
            return false
        }
        const x = this.wallets.splice(index, 1)
        return true
    }
    static RemoveUser(_user){
        const USER_NOT_FOUND = -1
        if(!_user){
            return false
        }
        const user = this.users.find(element => element.nome == _user.nome)
        const index = this.users.indexOf(user)
        if(index == USER_NOT_FOUND){
            return false
        }
        const x = this.users.splice(index, 1)
        return true
    }
    static FindWallet(ownerName){
        const found = this.wallets.find(element => element.owner.nome == ownerName)
        return found
    }
    static FindUser(UserName){
        if(!UserName){
            return false
        }
        var found = this.users.find(element => element.nome == UserName)
        return found
    }
    static authUser(user){
        if(!user){
            return false
        }
        const found = this.users.find(element => element.nome == user.nome && element.password == user.password)
        console.log(found)
        if(found){
            return true
        }
        return false

    }
}

module.exports = BancoDados
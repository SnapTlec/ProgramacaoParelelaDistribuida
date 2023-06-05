export default class BancoDados{
    static wallets = []
    static users = []

    static AddWallet(wallet){
        this.wallets.push(wallet)
    }
    static AddUser(user){
        this.users.push(user)
    }
    static RemoveWallet(wallet){
        const index = this.wallets.indexOf(wallet)
        if(index){
            return false
        }
        const x = this.wallets.splice(index, 1)
        return true
    }
    static RemoveUser(user){
        const index = this.users.indexOf(user)
        if(index){
            return false
        }
        const x = this.users.splice(index, 1)
        return true
    }
    static FindWallet(ownerName){
        const found = this.wallets.find(element => element.name == ownerName)
        return found
    }
    static FindUser(UserName){
        const found = this.wallets.find(element => element.name == UserName)
        return found
    }
}
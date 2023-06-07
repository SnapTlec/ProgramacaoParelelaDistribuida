const axios = require('axios');

var url = "http://localhost:3000/wallet"


body = {
    name : "leonardo.brito",
    password : "123456789",
    money : 100.00
}

axios.post(url, body,{
    headers : {
        token : "TjRfbjAxdDNfbWExc19zMG1icjE0.MTY4NjA5NjY5NTA0Mw==.bGVvbmFyZG8uYnJpdG8uMTIzNDU2Nzg5"
    }
}).then(function (response){

    console.log("Retorno criação carteira: ", response.data)
})
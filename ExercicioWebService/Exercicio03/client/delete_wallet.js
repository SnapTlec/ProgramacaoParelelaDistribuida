const axios = require('axios');

var url = "http://localhost:3000/wallet"

body = {
    name : "leonardo.brito",
    password : "123456789",
}

axios.delete(url, {data : {body : body}}).then(function (response){

    console.log(response.data)
})
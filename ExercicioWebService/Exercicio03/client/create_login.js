const axios = require('axios');

var url = "http://localhost:3000/login"

body = {
    name : "leonardo.brito",
    password : "123456789",
}

axios.post(url, body).then(function (response){

    console.log("Retorno login: ", response.data)
})
const axios = require('axios');

var url = "http://localhost:3000/wallet"


axios.get(url).then(function (response){
    console.log(response.data)
})
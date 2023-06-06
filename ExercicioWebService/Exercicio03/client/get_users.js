const axios = require('axios');

var url = "http://localhost:3000/user"


axios.get(url).then(function (response){
    console.log(response.data)
})
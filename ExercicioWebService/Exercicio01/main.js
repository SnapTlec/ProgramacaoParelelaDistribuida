require('dotenv').config();
const axios = require('axios');

var apiKey = process.env.API_KEY;
var urlBase = process.env.URL_BASE;
var moeda = 'USD';
var url = urlBase+apiKey+'/latest/'+moeda;



axios.get(url).then(function (response){

    var jsonRetorno = response.data;
    const tabela = {
        Real : jsonRetorno.conversion_rates.BRL,
        Euro : jsonRetorno.conversion_rates.EUR,
        Iene : jsonRetorno.conversion_rates.JPY
    }

    console.log('Tabela de conversão do dólar em relação a:')
    console.table(tabela)
})

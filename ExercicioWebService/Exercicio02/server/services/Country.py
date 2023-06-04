import requests
class Country:
    @staticmethod
    def get_info_country(name:str=None):
        URL_BASE = f"https://restcountries.com/v3.1/name/"

        if(name == None):
            COUNTRY_DEFAULT = "Brazil"
            url = URL_BASE + COUNTRY_DEFAULT
            res = requests.get(url)
            return res.json()
        url = URL_BASE + name
        res = requests.get(url)

        return res.json()
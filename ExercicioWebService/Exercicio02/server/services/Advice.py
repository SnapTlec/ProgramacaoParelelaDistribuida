import requests

class Advice:
    
    @staticmethod
    def request_api_advice(de:str=None):
        MAX_DEFAULT = 1
        TERM_DEFAULT = "Jesus%20Cristo"
        URL_BASE = "https://pensador-api.vercel.app/"
        
        if(de==None):
            url = f"{URL_BASE}?term={TERM_DEFAULT}&max={MAX_DEFAULT}"
            res = requests.get(url)
            return res.json()
        url = f"{URL_BASE}?term={de}&max={MAX_DEFAULT}"
        res = requests.get(url)

        return res.json
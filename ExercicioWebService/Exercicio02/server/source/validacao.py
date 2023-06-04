import hmac
import hashlib
import base64
import json 
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class Validacao:

    @staticmethod
    def create_jwt(nickname:str):

        session_time = int(os.getenv('SESSION_TIME'))

        payload = json.dumps({
            'userId': nickname,
            'exp' : (datetime.datetime.now() + datetime.timedelta(minutes=session_time)).timestamp()
        }).encode()

        header = json.dumps({
            'typ': os.getenv('HEADER_TYPER'),
            'alg': os.getenv('HEADER_ALGORITMO')
        }).encode()

        b64_header = base64.urlsafe_b64encode(header).decode()
        b64_payload = base64.urlsafe_b64encode(payload).decode()

        secret_key = os.getenv('SECRET_KEY')

        signature = hmac.new(
            key=secret_key.encode(),
            msg=f'{b64_header}.{b64_payload}'.encode(),
            digestmod=hashlib.sha256
        ).digest()

        jwt = f'{b64_header}.{b64_payload}.{base64.urlsafe_b64encode(signature).decode()}'

        return jwt

    @staticmethod
    def verify_and_decode_jwt(jwt):

        secret_key = os.getenv('SECRET_KEY')

        b64_header, b64_payload, b64_signature = jwt.split('.')

        b64_signature_checker = base64.urlsafe_b64encode(
            hmac.new(
                key=secret_key.encode(),
                msg=f'{b64_header}.{b64_payload}'.encode(),
                digestmod=hashlib.sha256
            ).digest()
        ).decode()

        # payload extraido antes para checar o campo 'exp'
        payload = json.loads(base64.urlsafe_b64decode(b64_payload))
        unix_time_now = datetime.datetime.now().timestamp()

        print(unix_time_now)
        print(payload['exp'])

        if payload.get('exp') and payload['exp'] < unix_time_now:
            raise Exception('Token expirado')
        
        if b64_signature_checker != b64_signature:
            raise Exception('Assinatura inválida')
        
        return payload    

if __name__ == '__main__':
    auth = {
        nickname: 'leonardo.brito',
        passWord : ''
    }
    jwt_created = Validacao().create_jwt(auth)
    print(jwt_created)

    time.sleep(2)

    decoded_jwt = Validacao().verify_and_decode_jwt(jwt_created)
    print(decoded_jwt)
from enum import Enum

class Plan(Enum):
    STANDARD = 0
    MEDDIUM = 1
    PREMIUM = 2

class MockBancoDados:
    users = [{'nome':'leo', 'plan': 1}, {'nome':'camila', 'plan':2}]

    def VerifyUser(self, nickname:str) -> bool:
        nick = nickname.split('.')
        if(len(nick) != 2 or nick[0] == '' or nick[1] == ''):
            return False
        return True
    
    def AddUser(self, nickname, plan:Plan):
        isValid = self.VerifyUser(nickname)
        retorno = self.FindUser(nickname)
        if(retorno != None or not(isValid)):
            return {
                'status':200, 
                'message':'Usuário inválido', 
                'data':[]
            }

        self.users.append({'nome':nickname, 'plano':plan.value})

        return {
            'status':200, 
            'message': 'Usuário adicionado com sucesso!', 
            'data':[{
                'nickName': nickname
            }]
        }
    
    def RemoveUser(self, nickname):
        res = next((user for user in self.users if user['nome'] == nickname), None)
        if(res == None):
            return {
                'status':200,
                'message':'Usuário não encontrado',
                'data':[]
            }
        self.users.remove(res)
        return {
                'status':200,
                'message':'Usuário removido com sucesso',
                'data':[]
            }

    def FindUser(self, nickname:str) -> dict | None:
        if(nickname == None):
            return None
        
        res = next((user for user in self.users if user['nome'] == nickname), None)

        return res


if __name__ == '__main__':
    banco = MockBancoDados()
    print(banco.AddUser('gustavo.lima', Plan.MEDDIUM))
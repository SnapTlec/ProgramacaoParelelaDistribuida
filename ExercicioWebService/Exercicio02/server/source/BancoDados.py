from enum import Enum


class Plan(Enum):
    STANDARD = {"functionAllow" : [1445] }
    MEDDIUM = {"functionAllow" : [1445, 2445]}
    PREMIUM = {"functionAllow" : [1445, 2445, 3445]}

class MockBancoDados:
    users = [{'nickname':'leo.brito', 'password' : '32154', 'plan': [1445]}, {'nickname':'camila.silva', "password":"124587" ,'plan':[1445, 2445]}]

    def VerifyUser(self, nickname:str) -> bool:
        nick = nickname.split('.')
        if(len(nick) != 2 or nick[0] == '' or nick[1] == ''):
            return False
        return True
    
    def AddUser(self, user):
        self.users.append({'nickname':user.nickname, 'password' : user.password, 'plan':user.plan.value["functionAllow"]})
    
    def RemoveUser(self, user):    

        res = next((_user for _user in self.users if _user['nickname'] == user.nickname and _user['password'] == user.password), None)

        if(res == None):
            return False
        
        self.users.remove(res)
        
        return True

    def FindUser(self, nickname:str):
        if(nickname == None):
            return None
        
        res = next((user for user in self.users if user['nickname'] == nickname), None)

        return res

    def CanDoThat(self, user, idFuncao) -> bool:
        ID_FUNCAO = idFuncao
        if (user == None):
            return False
        for funcao in user["plan"]:
            if funcao == ID_FUNCAO:
                return True
        return False 
    
    def validateUser(self, nickname, password):

        res = next((_user for _user in self.users if _user['nickname'] == nickname and _user['password'] == password), None)

        if(res == None):
            return {
                "response_bool" : False,
                "data" : None 
            }
        
        return {
            "response_bool" : True,
            "data" : res 
        }
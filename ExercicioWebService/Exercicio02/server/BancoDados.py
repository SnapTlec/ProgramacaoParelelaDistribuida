from enum import Enum


class Plan(Enum):
    STANDARD = 0
    MEDDIUM = 1
    PREMIUM = 2

class MockBancoDados:
    users = [{'nickname':'leo.brito', 'password' : '32154', 'plan': 1}, {'nickname':'camila.silva', "password":"124587" ,'plan':2}]

    def VerifyUser(self, nickname:str) -> bool:
        nick = nickname.split('.')
        if(len(nick) != 2 or nick[0] == '' or nick[1] == ''):
            return False
        return True
    
    def AddUser(self, user):
        self.users.append({'nickname':user.nickname, 'password' : user.password, 'plan':user.plan.value})
    
    def RemoveUser(self, user):    

        res = next((_user for _user in self.users if _user['nickname'] == user.nickname and _user['password'] == user.password), None)

        if(res == None):
            return False
        
        self.users.remove(res)
        
        return True

    def FindUser(self, nickname:str) -> dict or None:
        if(nickname == None):
            return None
        
        res = next((user for user in self.users if user['nickname'] == nickname), None)

        return res


if __name__ == '__main__':
    banco = MockBancoDados()
    print(banco.AddUser('gustavo.lima', Plan.MEDDIUM))
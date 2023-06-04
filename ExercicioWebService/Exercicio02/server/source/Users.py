from source.BancoDados import Plan

class User:
    def __init__(self, name:str, password:str, plan:int):
        self.nickname = name
        self.password = password
        self.plan = self.setPlan(plan)


    def setPlan(self, plan:int) -> Plan:
        if(plan == 0):
            return Plan.STANDARD
        else:
            if(plan == 1):
                return Plan.MEDDIUM
            else:
                if(plan == 2):
                    return Plan.PREMIUM
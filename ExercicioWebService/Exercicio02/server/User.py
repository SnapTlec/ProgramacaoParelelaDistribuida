from BancoDados import Plan
class User:
    def __inti__(self, name:str, password:str, plan:Plan):
        self.nome = name
        self.senha = password
        self.plano = plan


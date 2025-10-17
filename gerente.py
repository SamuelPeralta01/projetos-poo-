from funcionario import Funcionario
class Gerente(Funcionario):
    def __init__(self,nome,cpf,salario,depart, senha, quant_func):
        super().__init__(nome,cpf,salario,depart)
        self.senha = senha
        self.quant_func = quant_func
    def getSenha(self):
        return self.senha
    def getQuant_func(self):
        return self.quant_func
    def autenticar(self,senha):
        if self.senha == senha:  
            return True
        else:
            return False
    def bonificar(self):
        self.salario = self.salario * 1.15
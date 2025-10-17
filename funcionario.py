class Funcionario():
    def __init__(self, nome, cpf, salario, depart):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.depart = depart
    def setSalario(self,salario):
        self.salario = salario
    def bonificar(self):
        self.salario = self.salario * 1.10   
    def getNome(self):
        return self.nome
    def getCpf(self):
        return self.cpf
    def getSalario(self):
        return self.salario
    def getDepart(self):
        return self.depart
from funcionario import Funcionario
class Vendedor(Funcionario):
    def __init__(self,nome,cpf,salario,depart,quant_vend,comissao):
        super().__init__(nome, cpf, salario, depart)
        self.quant_vend = quant_vend
        self.comissao = comissao
    def setQuant_vend(self,quant_vend):
        self.quant_vend = quant_vend
    def getQuant_vend(self):
        return self.quant_vend
    def getComissao(self):
        return self.comissao
    def atualizarQuant(self,quant):
        self.quant_vend = self.quant_vend + quant
    def calcularSalario(self):
        self.salario = self.salario + (self.quant_vend * self.comissao)
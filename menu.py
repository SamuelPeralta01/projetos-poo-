

from funcionario import Funcionario
from gerente import Gerente
from vendedor import Vendedor

        
def menu():
     print(" ----------- MENU ------------")
     print("(1) Cadastrar Funcionário")
     print("(2) Cadastrar Gerente")
     print("(3) Cadastrar Vendedor")
     print("(4) Bonificar Funcionário")
     print("(5) Bonificar Gerente")
     print("(6) Autenticar senha Gerente")
     print("(7) Atualizar quantidade de vendas do vendedor")
     print("(8) Calcular Salário do Vendedor")
     print("(9) Listar Funcionários")
     print("(10) Listar Gerentes")
     print("(11) Listar Vendedores")
     print("(12) Sair ")

funcionarios = []
gerentes = []
vendedor = []
while True:
    menu()
    opcao = 0
    try:
        opcao = int(input("Escolha a opção que deseja realizar: "))
    except ValueError:
        print("Opção inválida, selecione uma das opções ")
    
    match opcao:
        
        case 1:
            nome = input("Informe o nome do funcionário: ").lower()
            cpf = input("Informe o CPF do funcionário: ")
            salario = float(input("informe o salário do funcionário: "))
            depart = input("Informe o departamento do funcionário: ")
            func = Funcionario(nome,cpf,salario,depart)
            funcionarios.append(func)
            
        case 2:

            nome = input("Informe o nome do gerente: ").lower()
            cpf = input("Informe o CPF do gerente: ")
            salario = float(input("informe o salário do gerente: "))
            depart = input("Informe o departamento do gerente: ")
            senha = input("Informe a senha do gerente: ")
            quant_func = int(input("Informe a quantidade de funcionários do gerente: "))
            ger = Gerente(nome,cpf,salario,depart,senha,quant_func)
            gerentes.append(ger)
            
        case 3:
            nome = input("Informe o nome do vendedor: ").lower()
            cpf = input("Informe o CPF do vendedor: ")
            salario = float(input("informe o salário do vendedor: "))
            depart = input("Informe o departamento do vendedor: ")
            quant_vend = int(input("Informe a quantidade de vendas do vendedor: "))
            comissao = float(input("Informe a comissão do vendedor (qual o valor por venda): "))
            vend = Vendedor(nome,cpf,salario,depart,quant_vend,comissao)
            vendedor.append(vend)

        case 4:
            encontrado = False
            for func in funcionarios:
                print("Funcinários cadastrados ")
                print(func.getNome())
            
            nome_func = input("Informe o nome do funcionário que deseja bonificar: ").lower()
            for func in funcionarios:
                if func.getNome() == nome_func:
                    func.bonificar()
                    print(f"Funcionário {func.getNome()} bonificado com sucesso. Novo salário: {func.getSalario()}")
                    encontrado = True
                    break
            if not encontrado:
                    print("Funcionário não encontrado")
        
        case 5:
            encontrado = False
            print("Gerentes cadastrados ")
            for ger in gerentes:
                print(ger.getNome()) 
            nome_ger = input("Informe o nome do gerente que deseja bonificar: ").lower()
            for ger in gerentes:
                if ger.getNome() == nome_ger:
                    ger.bonificar()
                    print(f"Gerente {ger.getNome()} bonificado com sucesso. Novo salário: {ger.getSalario()}")
                    encontrado = True
                    break
            if not encontrado:
                    print("Gerente não encontrado")

        case 6:
            encontrado = False
            print("Gerentes cadastrados ")
            for ger in gerentes: 
                print(ger.getNome()) 
            nome_gen = input("Selecione o gerente escolhido: ").lower()
            for ger in gerentes:
                if ger.getNome() == nome_gen:
                    encontrado = True
                    senha_e = input("informe a senha que deseja autenticar: ")
                    if ger.autenticar(senha_e):
                        print("A senha é verdadeira ")
                        break
                    else:
                        print("A senha não foi reconhecida ")
                        break
            if not encontrado:
                    print("Gerente não encontrado")

        case 7:
            encontrado = False
            print("Vendedores Cadastrados")
            for vend in vendedor:
                print(vend.getNome())
            vend_s = input("Escolha um dos vendedores cadastrados: ").lower()
            for vend in vendedor:
                if vend.getNome() == vend_s:
                    encontrado = True
                    quant_v = int(input("Digite quantas vendas deseja adicionar: "))
                    vend.atualizarQuant(quant_v)
                    print("Vendas adicionadas com sucesso: ")
                    break
            if not encontrado:
                    print("Vendedor não encontrado")
        case 8:
            encontrado = False  
            print("Vendedores Cadastrados")
            for vend in vendedor:
                print(vend.getNome())
            vend_s = input("Escolha um dos vendedores cadastrados: ").lower()
            for vend in vendedor:
                if vend.getNome() == vend_s:
                    encontrado = True
                    vend.calcularSalario()
                    print(f"Salário do vendedor {vend.getNome()} atualizado com sucesso. Novo salário: {vend.getSalario()}")
                    break
            if not encontrado:
                    print("Vendedor não encontrado")
        case 9:
            
            for func in funcionarios:
                print(f"Nome: {func.getNome()}, CPF: {func.getCpf()}, Salario {func.getSalario()}, Departamento {func.getDepart()}")
            if not funcionarios:
                print("Nenhum funcionário cadastrado.")
        case 10:
            for ger in gerentes:
                print(f"Nome: {ger.getNome()}, CPF: {ger.getCpf()}, Salario {ger.getSalario()}, Departamento {ger.getDepart()}, Quantidade de Funcionários {ger.getQuant_func()}, Senha {ger.getSenha()}, ")
            if not gerentes:
                print("Nenhum gerente cadastrado.")
        case 11:
            for vend in vendedor:
                print(f"Nome: {vend.getNome()}, CPF: {vend.getCpf()}, Salario {vend.getSalario()}, Departamento {vend.getDepart()}, Quantidade de Vendas {vend.getQuant_vend()}, Comissão por venda {vend.getComissao()}")
            if not vendedor:
                print("Nenhum vendedor cadastrado.")
        case 12:
            print("Saindo do sistema ")
            break
            
# 🧠 Sistema de Funcionários

Este projeto foi desenvolvido em Python como exercício de **Programação Orientada a Objetos (POO)**.  
O sistema permite gerenciar **funcionários, gerentes e vendedores**, simulando um pequeno sistema de RH.

---

## 🚀 Funcionalidades

- Cadastro de Funcionários, Gerentes e Vendedores  
- Bonificação de salário por cargo  
- Autenticação de senha para Gerentes  
- Cálculo de comissão e atualização de vendas para Vendedores  
- Listagem de todos os funcionários cadastrados

---

## 🧱 Conceitos de POO aplicados

- **Herança:**  
  As classes `Gerente` e `Vendedor` herdam de `Funcionario`.

- **Encapsulamento:**  
  Atributos com métodos `get` e `set` controlam o acesso aos dados.

  Código dividido em múltiplos arquivos (`funcionario.py`, `gerente.py`, `vendedor.py`, `menu.py`).

---

## 📂 Estrutura do Projeto

```
sistema-funcionarios/
│
├── funcionario.py   # Classe base Funcionario
├── gerente.py       # Classe Gerente (herda de Funcionario)
├── vendedor.py      # Classe Vendedor (herda de Funcionario)
├── menu.py          # Menu principal do sistema
└── README.md        # Este arquivo
```



---
## Execute o programa:

- python menu.py

# 📚 Aprendizados

 - Durante o desenvolvimento, foram praticados:

 - Criação e relacionamento entre classes;

 - Reutilização de código com herança;

 - Modularização em múltiplos arquivos Python;

 - Organização de código e boas práticas de POO.

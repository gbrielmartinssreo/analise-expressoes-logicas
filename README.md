doekdoksodkeok
# Analise de Expressões Lógicas
![Status do Projeto](https://img.shields.io/badge/Status-Andamento-orange)

## 📖 Descrição
Este projeto implementa um avaliador de expressões booleanas, permitindo a geração de tabelas-verdade e a avaliação de expressões com valores específicos. Ele foi criado com a intenção de ajudar os alunos que cursarão a disciplina de matemática discreta.

Este projeto foi desenvolvido utilizando **Python**.

---

## 📋 Índice
1. [Instalação](#-instalação)
2. [Funcionalidades](#-funcionalidades)
3. [Tecnologias](#-tecnologias)
4. [Exemplos](#-exemplos)
5. [Sobre o Autor](#-sobre-o-autor)

---

## 🛠 Instalação e execução

1. Clone o repositório:
    ```bash
    git clone https://github.com/gbrielmartinssreo/analise-expressoes-logicas.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd analise-expressoes-logicas
    ```
3. Certifique-se de ter o python instalado:
    ```python
    python --version
    ```

4. Rode o programa:
	```python
    python main.py
	```


---

## ⚙️ Funcionalidades

* **Geração de Tabelas-Verdade:** Gera tabelas-verdade para expressões booleanas arbitrárias, visualizando os resultados para todas as combinações possíveis de valores das variáveis.

* **Avaliação de Expressões:** Avalia expressões booleanas fornecendo valores específicos para as variáveis.  O avaliador retorna o resultado (Verdadeiro ou Falso).

* **Operadores Suportados:**  O avaliador suporta os seguintes operadores lógicos:
    * `^`: E (AND)
    * `v`: OU (OR)
    * `~`: NÃO (NOT)
    * `>`: Implicação
    * `-`: Bicondicional (equivalência)
    * `(` e `)`: Parênteses para controlar a precedência.


## 💻 Tecnologias

Boa parte deste projeto foi desenvolvido utilizando o algoritmo Shunting Yard:
-  O algoritmo Shunting Yard é implementado para processar expressões lógicas de entrada e transformá-las em uma notação que facilita a avaliação.
-   Ele permite que expressões lógicas complexas, como aquelas que utilizam conjunções (`^`), disjunções (`v`), negações (`~`), condicionais (`>`), e bicondicionais (`-`), sejam avaliadas sem a necessidade de manipular a precedência dos operadores manualmente.
-   A expressão é analisada e convertida para uma forma pós-fixa, o que torna o processo de avaliação mais simples e eficiente.


---
## 👨🏻‍⚖️ Exemplos

**Geração de Tabela-Verdade:**
```
Bem-vindo ao Solucionador de Lógica Proposicional!
Escolha uma das opções abaixo:
1. Gerar tabela verdade
2. Resolver expressão lógica com valores específicos
3. Resolver demonstrações com regras de inferência
4. Sair
Digite o número da opção desejada: 1
Quantas letras tem a expressao: 3
Digite a expressao: (A^B)vC
Digite a 1º letra: A
Digite a 2º letra: B
Digite a 3º letra: C
-------------------------------------
   A    |    B    |    C    | (A^B)vC
-------------------------------------
 False  |  False  |  False  |  False 
-------------------------------------
 False  |  False  |   True  |   True 
-------------------------------------
 False  |   True  |  False  |  False 
-------------------------------------
 False  |   True  |   True  |   True 
-------------------------------------
  True  |  False  |  False  |  False 
-------------------------------------
  True  |  False  |   True  |   True 
-------------------------------------
  True  |   True  |  False  |   True 
-------------------------------------
  True  |   True  |   True  |   True 
-------------------------------------

```    

**Resolvendo Expressão:**
```
Bem-vindo ao Solucionador de Lógica Proposicional!
Escolha uma das opções abaixo:
1. Gerar tabela verdade
2. Resolver expressão lógica com valores específicos
3. Resolver demonstrações com regras de inferência
4. Sair
Digite o número da opção desejada: 2
Quantas letras tem a expressao: 2
Digite a expressao: ~AvB
Digite a 1º letra: A
Digite o valor (V/F): F
Digite a 2º letra: B
Digite o valor (V/F): V
True

```

---

## 👤 Sobre o Autor

Este projeto foi criado por [Gabriel Martins de Morais](https://github.com/gbrielmartinssreo).

---

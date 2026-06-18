# Sobre o Projeto

## Sistema de Gestão para Casa da Pizza

Projeto desenvolvido para o **PIM II (Projeto Integrado Multidisciplinar)** do curso de **Análise e Desenvolvimento de Sistemas**.

O objetivo do trabalho foi analisar a infraestrutura computacional e o ecossistema de Tecnologias da Informação e Comunicação (TIC) de uma empresa, e a escolhida em questão foi uma pequena empresa do setor alimentício, a **Casa da Pizza**, localizada em Uberaba-MG. A partir desse estudo, foi identificada a necessidade de automatizar processos relacionados ao controle de estoque e ao gerenciamento de pedidos.

Como solução, foi desenvolvido um sistema simples em **Python** com interface gráfica utilizando **Tkinter**, permitindo que a empresa organize melhor suas informações e tenha maior controle sobre suas operações diárias.

---

## Funcionalidades

- Cadastro de ingredientes e controle de estoque;
- Registro de pedidos realizados;
- Consulta dos itens disponíveis;
- Armazenamento permanente das informações em arquivos JSON;
- Interface simples e acessível para utilização em pequenos negócios.

---

### Estrutura dos Arquivos

#### `main.py`

Arquivo principal da aplicação.

Responsável pela interface gráfica, gerenciamento de estoque, registro de pedidos e manipulação dos dados armazenados.

#### `estoque.json`

Arquivo utilizado para armazenar os ingredientes cadastrados e suas respectivas quantidades em estoque.

Exemplo:

```json
[
    {
        "nome": "Mussarela",
        "quantidade": 10
    }
]
```

#### `pedidos.json`

Arquivo utilizado para armazenar os pedidos registrados pelo sistema.

Exemplo:

```json
[
    {
        "cliente": "João",
        "produto": "Pizza Calabresa",
        "valor": 45.00
    }
]
```

---

### Tecnologias Utilizadas

- Python 3
- Tkinter
- JSON

---

### Objetivo Acadêmico

Este projeto foi desenvolvido para demonstrar a aplicação prática dos conceitos estudados nas disciplinas relacionadas à:

- Infraestrutura Computacional;
- Tecnologias da Informação e Comunicação (TIC);
- Lógica de Programação;
- Desenvolvimento de Software;
- Pensamento Computacional;

A proposta demonstra como ferramentas simples e de baixo custo podem auxiliar pequenas empresas na organização de processos e na melhoria da gestão operacional.

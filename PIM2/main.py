# Fiz uso do Tkinter apenas para criar uma interface simples que poderia ser manejada por pessoas leigas em programação
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

# Aqui estão os jsons que serão importados
ARQ_ESTOQUE = "estoque.json"
ARQ_PEDIDOS = "pedidos.json"

# Cria os arquivos json caso não existam
def criar_arquivos():
    if not os.path.exists(ARQ_ESTOQUE):
        with open(ARQ_ESTOQUE, "w", encoding="utf-8") as f:
            json.dump([], f)

    if not os.path.exists(ARQ_PEDIDOS):
        with open(ARQ_PEDIDOS, "w", encoding="utf-8") as f:
            json.dump([], f)

# Funções para o estoque
def carregar_estoque():
    with open(ARQ_ESTOQUE, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_estoque(dados):
    with open(ARQ_ESTOQUE, "w", encoding="utf-8") as f:
        json.dump(
            dados,
            f,
            indent=4,
            ensure_ascii=False
        )

def cadastrar_ingrediente():

    nome = entry_nome_ingrediente.get()

    try:
        qtd = int(entry_qtd.get())
        minimo = int(entry_minimo.get())

    except:
        messagebox.showerror(
            "Erro",
            "Digite apenas números."
        )
        return

    estoque = carregar_estoque()

    estoque.append({
        "ingrediente": nome,
        "quantidade": qtd,
        "minimo": minimo
    })

    salvar_estoque(estoque)

    messagebox.showinfo(
        "Sucesso",
        "Ingrediente cadastrado."
    )

    atualizar_lista_estoque()

def atualizar_lista_estoque():

    lista_estoque.delete(
        0,
        tk.END
    )

    estoque = carregar_estoque()

    for item in estoque:

        lista_estoque.insert(
            tk.END,
            f"{item['ingrediente']} - "
            f"{item['quantidade']} unidades"
        )

def verificar_estoque():
    estoque = carregar_estoque()
    alerta = ""
    for item in estoque:

        if item["quantidade"] <= item["minimo"]:

            alerta += (
                f"• {item['ingrediente']}\n"
            )

    if alerta:
        messagebox.showwarning(
            "Estoque Baixo",
            alerta
        )
    else:
        messagebox.showinfo(
            "Estoque",
            "Todos os produtos estão OK."
        )

# Funções para o pedido
def carregar_pedidos():
    with open(
        ARQ_PEDIDOS,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)

def salvar_pedidos(dados):
    with open(
        ARQ_PEDIDOS,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            dados,
            f,
            indent=4,
            ensure_ascii=False
        )
def novo_pedido():
    cliente = entry_cliente.get()
    produto = entry_produto.get()
    try:
        quantidade = int(
            entry_quantidade_pedido.get()
        )
        valor = float(
            entry_valor.get()
        )
    except:
        messagebox.showerror(
            "Erro",
            "Quantidade e valor inválidos."
        )
        return

    pedidos = carregar_pedidos()
    pedidos.append({
        "cliente": cliente,
        "produto": produto,
        "quantidade": quantidade,
        "valor": valor,
        "status": "Recebido"
    })

    salvar_pedidos(pedidos)
    atualizar_lista_pedidos()
    messagebox.showinfo(
        "Pedido",
        "Pedido registrado."
    )

def atualizar_lista_pedidos():
    lista_pedidos.delete(
        0,
        tk.END
    )
    pedidos = carregar_pedidos()
    for pedido in pedidos:
        lista_pedidos.insert(
            tk.END,
            f"{pedido['cliente']} - "
            f"R$ {pedido['valor']:.2f}"
        )

# Geração de relatórios de faturamento
def mostrar_faturamento():
    pedidos = carregar_pedidos()
    total = 0
    for pedido in pedidos:
        total += pedido["valor"]

    messagebox.showinfo(
        "Faturamento",
        f"Total vendido:\nR$ {total:.2f}"
    )

# Início da interface no Tkinter
criar_arquivos()
janela = tk.Tk()
janela.title(
    "Casa da Pizza"
)
janela.geometry(
    "900x650"
)

# Fonte maior para facilitar uso
FONTE = (
    "Arial",
    12
)

TITULO = (
    "Arial",
    14,
    "bold"
)

# Abas no tkinter
abas = ttk.Notebook(
    janela
)

abas.pack(
    fill="both",
    expand=True
)

aba_estoque = tk.Frame(abas)
aba_pedidos = tk.Frame(abas)
aba_relatorios = tk.Frame(abas)

abas.add(
    aba_estoque,
    text="Estoque"
)

abas.add(
    aba_pedidos,
    text="Pedidos"
)

abas.add(
    aba_relatorios,
    text="Relatórios"
)

# Aba do Estoque
tk.Label(
    aba_estoque,
    text="Cadastro de Ingredientes",
    font=TITULO
).pack(
    pady=10
)

tk.Label(
    aba_estoque,
    text="Ingrediente",
    font=FONTE
).pack()

entry_nome_ingrediente = tk.Entry(
    aba_estoque,
    font=FONTE,
    width=30
)

entry_nome_ingrediente.pack()

tk.Label(
    aba_estoque,
    text="Quantidade (em quilos)",
    font=FONTE
).pack()

entry_qtd = tk.Entry(
    aba_estoque,
    font=FONTE,
    width=30
)

entry_qtd.pack()

tk.Label(
    aba_estoque,
    text="Quantidade Mínima (em quilos)",
    font=FONTE
).pack()

entry_minimo = tk.Entry(
    aba_estoque,
    font=FONTE,
    width=30
)

entry_minimo.pack()

tk.Button(
    aba_estoque,
    text="Cadastrar",
    font=FONTE,
    width=20,
    command=cadastrar_ingrediente
).pack(
    pady=10
)

tk.Button(
    aba_estoque,
    text="Verificar Estoque",
    font=FONTE,
    width=20,
    command=verificar_estoque
).pack()

lista_estoque = tk.Listbox(
    aba_estoque,
    font=FONTE,
    width=50,
    height=10
)

lista_estoque.pack(
    pady=10
)

# Aba de pedidos
tk.Label(
    aba_pedidos,
    text="Novo Pedido",
    font=TITULO
).pack(
    pady=10
)

campos = [
    "Cliente",
    "Produto",
    "Quantidade",
    "Valor"
]

entradas = []

for campo in campos:
    tk.Label(
        aba_pedidos,
        text=campo,
        font=FONTE
    ).pack()

    entrada = tk.Entry(
        aba_pedidos,
        font=FONTE,
        width=30
    )
    entrada.pack()
    entradas.append(
        entrada
    )

entry_cliente = entradas[0]
entry_produto = entradas[1]
entry_quantidade_pedido = entradas[2]
entry_valor = entradas[3]

tk.Button(
    aba_pedidos,
    text="Registrar Pedido",
    font=FONTE,
    width=20,
    command=novo_pedido
).pack(
    pady=10
)

lista_pedidos = tk.Listbox(
    aba_pedidos,
    font=FONTE,
    width=50,
    height=10
)

lista_pedidos.pack()

# Aba de relatórios
tk.Label(
    aba_relatorios,
    text="Relatórios",
    font=TITULO
).pack(
    pady=20
)

tk.Button(
    aba_relatorios,
    text="Consultar Faturamento",
    font=FONTE,
    width=25,
    height=2,
    command=mostrar_faturamento
).pack()

# Carregamento
atualizar_lista_estoque()
atualizar_lista_pedidos()

# Execução do arquivo
janela.mainloop()
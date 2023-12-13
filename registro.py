
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import tkinter as tk
import sqlite3
import os


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\gugab\Documents\faculdade\4o Periodo\4ADS\2a try\AV2\Exercicios\register\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

entry_user = None
entry_senha = None
entry_nome = None
entry_ender = None
entry_telef = None
entry_email = None

def criar_tabela():
    with sqlite3.connect('crudcabana.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS pessoa (
            Id_pessoa INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            endereco TEXT,
            telefone INTEGER,
            email TEXT,
            id_login INTEGER,
            FOREIGN KEY (id_login) REFERENCES login(id)
        )""")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS login (
                id_login INTEGER PRIMARY KEY,
                username TEXT,
                senha TEXT,
                permissao INTEGER
            )
        """)


def exec_cadastro():
    global entry_user, entry_senha, entry_nome, entry_ender, entry_telef, entry_email

    username = entry_user.get()
    senha = entry_senha.get()
    nome = entry_nome.get()
    ender = entry_ender.get()
    telef = entry_telef.get()
    email = entry_email.get()
    with sqlite3.connect('crudcabana.db') as conn:
        cursor = conn.cursor()

    try:
        # Inserir dados na tabela login
        cursor.execute("INSERT INTO login VALUES (NULL, ?, ?, 0)", (username, senha))
        id_log = cursor.lastrowid

        # Inserir dados na tabela pessoa
        cursor.execute("INSERT INTO pessoa VALUES (NULL, ?, ?, ?, ?, ?)", (nome, ender, telef, email, id_log))

        # Commit para confirmar as alterações no banco de dados
        conn.commit()

        # Mensagem de sucesso
        messagebox.showinfo("Registro", "Usuário registrado com sucesso!")
        print("Usuário registrado com sucesso. ID do login:", id_log)

    except InterruptedError:
        # Mensagem de erro se o nome de usuário já existe
        messagebox.showerror("Erro", "Nome de usuário já existe. Escolha outro.")
        print("Erro: Nome de usuário já existe.")
    except Exception as e:
        # Outros erros
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
        print("Erro desconhecido:", str(e))

def validar_entrada(char):
    # Verifica se o caractere é um número
    return char.isdigit()

def verificar_entrada(event):
    entrada = entry_telef.get()
    if not entrada.isdigit():
        messagebox.showerror("Erro", "O campo Telefone, só aceita números! Tente novamente")
        # Limpar a entrada inválida
        entry_telef.delete(0, tk.END)
    return True

def pagina():
    global entry_user, entry_senha, entry_nome, entry_ender, entry_telef, entry_email

    window = Tk()
    window.geometry("700x400")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 400,
        width = 700,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        700.0,
        38.0,
        fill="#3379E2",
        outline="")

    canvas.create_text(
        255.0,
        5.0,
        anchor="nw",
        text="Hotel Crudcabana",
        fill="#FFFFFF",
        font=("Inter Medium", 24 * -1)
    )

    canvas.create_rectangle(
        110.0,
        59.0,
        580.0,
        382.0,
        fill="#706D6D",
        outline="")

    canvas.create_text(
        280.0,
        75.0,
        anchor="nw",
        text="Registrar",
        fill="#2E71D5",
        font=("Inter Bold", 24 * -1)
    )

    #user
    canvas.create_text(
        145.0,
        122.0,
        anchor="nw",
        text="Usuário",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )


    entry_user = tk.Entry(window, width=28)
    entry_user.place(x=140, y=141)

    #senha
    canvas.create_text(
        330.0,
        122.0,
        anchor="nw",
        text="Senha",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )

    entry_senha = tk.Entry(window, width=28)
    entry_senha.place(x=335, y=141)

    #nome
    canvas.create_text(
        145.0,
        167.0,
        anchor="nw",
        text="Nome",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )

    entry_nome = tk.Entry(window, width=61)
    entry_nome.place(x=140, y=191)

    #endereco
    canvas.create_text(
        145.0,
        221.0,
        anchor="nw",
        text="Endereço",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )

    entry_ender = tk.Entry(window, width=61)
    entry_ender.place(x=140, y=243)

    #telefone
    canvas.create_text(
        145.0,
        275.0,
        anchor="nw",
        text="Telefone",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )

    entry_telef = tk.Entry(window, width=25, validate='key', validatecommand=validar_entrada)
    entry_telef.place(x=140, y=294)

    entry_telef.bind("<KeyRelease>", verificar_entrada)

    #email
    canvas.create_text(
        315.0,
        275.0,
        anchor="nw",
        text="Email",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )

    entry_email = tk.Entry(window, width=32)
    entry_email.place(x=315, y=294)

    #criando tabelas
    criar_tabela()

    estilo_Cadastro = ("Inter Bold", 12, "bold")

    # btnRegistrar
    btn_Register = tk.Button(window, width=10, text="Cadastrar", font=estilo_Cadastro, command=exec_cadastro)
    btn_Register.place(x=406, y=338)


    window.resizable(False, False)
    window.mainloop()
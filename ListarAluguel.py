
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from tkinter import ttk
import sqlite3


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\gugab\Documents\faculdade\4o Periodo\4ADS\2a try\AV2\Exercicios\Listar\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def ListaAluga():
    window = Tk()
    window.title("Hotel CRUDcabana - Listar Alugueis")

    window.geometry("1080x720")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1080.0,
        83.0,
        fill="#3379E2",
        outline="")

    canvas.create_text(
        390.0,
        27.0,
        anchor="nw",
        text="Hotel Crudcabana",
        fill="#FFFFFF",
        font=("Inter Medium", 24 * -1)
    )

    canvas.create_rectangle(
        68.0,
        133.0,
        1032.0,
        664.0,
        fill="#706D6D",
        outline="")


    canvas.create_text(
        450.0,
        147.0,
        anchor="nw",
        text="Listar Alugueis",
        fill="#2E71D5",
        font=("Inter Bold", 24 * -1)
    )

    #Tabela
    tblAluga = ttk.Treeview(window)
    tblAluga["columns"] = ("id_aluguel", "Id_quarto", "Id_cliente", "Data_entrada" , "Data_saida")
    tblAluga.heading("#0", text="ID")
    tblAluga.heading("id_aluguel", text="ID")
    tblAluga.heading("Id_quarto", text="Id do Cliente")
    tblAluga.heading("Id_cliente", text="Id Do Quarto")
    tblAluga.heading("Data_entrada", text="Data de Entrada")
    tblAluga.heading("Data_saida", text="Data de Saída")

    tblAluga.column("#0", width=50)  # indice
    tblAluga.column("id_aluguel", width=50)
    tblAluga.column("Id_quarto", width=150)
    tblAluga.column("Id_cliente", width=150)
    tblAluga.column("Data_entrada", width=150)
    tblAluga.column("Data_saida", width=150)

    tblAluga.place(x=130, y=236)

    # Limpar dados antigos
    for row in tblAluga.get_children():
        tblAluga.delete(row)

    # Conectar ao banco de dados
    with sqlite3.connect('crudcabana.db') as conn:
        cursor = conn.cursor()

    # Executar uma consulta SELECT
    cursor.execute("SELECT * FROM aluguel")
    dados = cursor.fetchall()

    # Inserir dados na Treeview
    for dado in dados:
        # Adicionando os dados à Treeview
        tblAluga.insert("", "end", values=dado)

    canvas.create_text(
        500.0,
        201.0,
        anchor="nw",
        text="Aluguéis",
        fill="#FFFFFF",
        font=("Inter Bold", 24 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
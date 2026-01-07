import tkinter as tk
from tkinter import ttk, messagebox
from services.aluno_service import listar_alunos, carregar_alunos

def criar_aba_alunos(parent):
    frame = ttk.Frame(parent)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # ==== TABELA ====
    colunas = ("id", "nome", "matricula", "turma", "turno", "status")
    tabela = ttk.Treeview(frame, columns=colunas, show="headings")
    tabela.pack(fill="both", expand=True)

    for col in colunas:
        tabela.heading(col, text=col.capitalize())

    def carregar():
        tabela.delete(*tabela.get_children())
        for aluno in listar_alunos():
            tabela.insert("", "end", values=aluno)

    # ==== BOTÕES ====

    botoes = ttk.Frame(frame)
    botoes.pack(fill="x", pady=10)

    ttk.Button(botoes, text="Novo").pack(side="left", padx=5)
    ttk.Button(botoes, text="Editar").pack(side="left", padx=5)
    ttk.Button(botoes, text="Inativar").pack(side="left", padx=5)

    carregar_alunos(tabela)
import tkinter as tk
from tkinter import ttk, messagebox
from services.aluno_service import listar_alunos, carregar_alunos, buscar_aluno_por_id, inativar_aluno
from telas.alunos_form import abrir_formulario

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
    
    carregar()

    # ==== BOTÕES ====

    botoes = ttk.Frame(frame)
    botoes.pack(fill="x", pady=10)

    def novo():
        abrir_formulario(parent, atualizar_callback=carregar)

    def editar():
        selecionado = tabela.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um aluno")
            return
        
        aluno_id = tabela.item(selecionado)["values"][0]
        aluno = buscar_aluno_por_id(aluno_id)

        abrir_formulario(parent, aluno=aluno, atualizar_callback=carregar)
    
    def inativar():
        selecionado = tabela.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um aluno")
            return
        
        aluno_id = tabela.item(selecionado)["values"][0]

        if messagebox.askyesno("Confirmar", "Inativar aluno selecionado?"):
            inativar_aluno(aluno_id)
            carregar()


    ttk.Button(botoes, text="Novo", command=novo).pack(side="left", padx=5)
    ttk.Button(botoes, text="Editar", command=editar).pack(side="left", padx=5)
    ttk.Button(botoes, text="Inativar", command=inativar).pack(side="left", padx=5)

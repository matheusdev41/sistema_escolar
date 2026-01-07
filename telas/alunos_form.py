import tkinter as tk
from tkinter import ttk, messagebox
from services.aluno_service import cadastrar_aluno, atualizar_aluno

def abrir_formulario(parent, aluno=None, atualizar_callback=None):
    janela = tk.Toplevel(parent)
    janela.title("Aluno")
    janela.geometry("350x300")
    janela.grab_set()

    campos = {}

    def criar_campo(label):
        ttk.Label(janela, text=label).pack(anchor="w", padx=10)
        entry = ttk.Entry(janela)
        entry.pack(fill="x", padx=10, pady=5)
        return entry

    campos["nome"] = criar_campo("Nome")
    campos["matricula"] = criar_campo("Matricula")
    campos["turma"] = criar_campo("Turma")
    campos["turno"] = criar_campo("Turno")

    if aluno:
        _, nome, matricula, turma, turno = aluno
        campos["nome"].insert(0, nome)
        campos["matricula"].insert(0, matricula)
        campos["turma"].insert(0, turma)
        campos["turma"].insert(0, turno)
    
    def salvar():
        dados = {k: v.get() for k, v in campos.items()}

        if not dados["nome"]:
            messagebox.showwarning("Erro", "Nome é obrigatório")
            return

        if aluno:
            atualizar_aluno(aluno[0], **dados)
        else:
            cadastrar_aluno(**dados)
        
        if atualizar_callback:
            atualizar_callback()
        
        janela.destroy()
    
    ttk.Button(janela, text="Salvar", command=salvar).pack(pady=15)

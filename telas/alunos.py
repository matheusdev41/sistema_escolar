import tkinter as tk
from tkinter import messagebox
from services.aluno_service import cadastrar_aluno

def tela_alunos():
    janela = tk.Toplevel()
    janela.title("Cadastrar Alunos")
    janela.geometry("400x300")
    
    tk.Label(janela, text="Nome").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Matrícula").pack()
    entry_matricula = tk.Entry(janela)
    entry_matricula.pack()

    tk.Label(janela, text="Turma").pack()
    entry_turma = tk.Entry(janela)
    entry_turma.pack()

    tk.Label(janela, text="Turno").pack()
    entry_turno = tk.Entry(janela)
    entry_turno.pack()

    def salvar():
        if not entry_nome.get():
            messagebox.showwarning("Erro", "Nome obrigatório")
            return
        
        cadastrar_aluno(
            entry_nome.get(),
            entry_matricula.get(),
            entry_turma.get(),
            entry_turno.get()
        )

        messagebox.showinfo("Sucesso", "Aluno Cadastrado")
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar).pack(pady=10)
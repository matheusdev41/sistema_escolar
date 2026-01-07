import tkinter as tk
from tkinter import ttk
from telas.alunos_tab import criar_aba_alunos

root = tk.Tk()
root.title("Sistema de Coordenação escolar")
root.geometry("1000x500")

# Notebook
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Aba alunos
aba_alunos = ttk.Frame(notebook)
notebook.add(aba_alunos, text="Alunos")

criar_aba_alunos(aba_alunos)

root.mainloop()
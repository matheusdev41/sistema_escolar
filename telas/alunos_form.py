import tkinter as tk
from tkinter import ttk, messagebox
from services.aluno_service import cadastrar_aluno, atualizar_aluno

def abrir_formulario(parent, aluno=None, atualizar_callback=None):
    TURMAS = [
        "Robótica",
        "Informática",
        "Manutenção",
        "Administração",
        "Inglês"
    ]

    janela = tk.Toplevel(parent)
    if aluno:
        janela.title("Editar aluno")
    else:
        janela.title("Novo Aluno")
        janela.geometry("380x420")
        janela.resizable(False, False)
        janela.grab_set()

    # ===== FRAME CAMPOS =====
    frame_campos = ttk.Frame(janela)
    frame_campos.pack(fill="x", padx=15, pady=15)

    campos = {}

    def criar_campo(label):
        ttk.Label(frame_campos, text=label).pack(anchor="w")
        entry = ttk.Entry(frame_campos)
        entry.pack(fill="x", pady=5)
        return entry

    def criar_combo(label, valores):
        ttk.Label(frame_campos, text=label).pack(anchor="w")
        combo = ttk.Combobox(
            frame_campos,
            values=valores,
            state="readonly"
        )
        combo.pack(fill="x", pady=5)
        return combo

    campos["nome"] = criar_campo("Nome")
    campos["nome"].focus()
    campos["matricula"] = criar_campo("Matrícula")
    campos["turma"] = criar_combo("Turma", TURMAS)
    campos["turno"] = criar_campo("Turno")

    if aluno and len(aluno) >= 5:
        id_, nome, matricula, turma, turno = aluno
        campos["nome"].insert(0, nome)
        campos["matricula"].insert(0, matricula)
        campos["turma"].set(turma)
        campos["turno"].insert(0, turno)

    # ===== FRAME BOTÕES (RODAPÉ FIXO) =====
    frame_botoes = ttk.Frame(janela)
    frame_botoes.pack(side="bottom", fill="x", padx=15, pady=10)

    def salvar():
        dados = {k: v.get() for k, v in campos.items()}

        if not dados["nome"]:
            messagebox.showwarning("Erro", "Nome é obrigatório")
            return
        
        if not dados["turma"]:
            messagebox.showwarning("Erro", "Selecione uma turma")
        

        if aluno:
            # garante que aluno_id seja um valor simples
            aluno_id = aluno[0][0] if isinstance(aluno[0], tuple) else aluno[0]

            atualizar_aluno(
                aluno_id,
                dados["nome"],
                dados["matricula"],
                dados["turma"],
                dados["turno"]
            )

        else:
            cadastrar_aluno(**dados)

        if atualizar_callback:
            atualizar_callback()

        janela.destroy()
    ttk.Button(frame_botoes, text="Cancelar", command=janela.destroy). pack(side="right", padx=5)
    ttk.Button(frame_botoes, text="Salvar", command=salvar).pack(
        side="right"
    )

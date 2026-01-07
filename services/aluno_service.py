from db import conectar

def cadastrar_aluno(nome, matricula, turma, turno):
    conn = conectar()
    cursor = conn.cursor()

    sql = """
    INSERT INTO alunos (nome, matricula, turma, turno)
    VALUES(%s, %s, %s, %s)
    """
    cursor.execute(sql, (nome, matricula, turma, turno))

    conn.commit()
    conn.close()

def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, matricula, turma, turno, status
        FROM alunos
        WHERE status = 'Ativo'
        ORDER BY nome
    """)

    dados = cursor.fetchall()
    conn.close()

    return dados

def carregar_alunos(tabela):
    for item in tabela.get_children():
        tabela.delete(item)

    alunos = listar_alunos()
    for aluno in alunos:
        tabela.insert("", "end", value=aluno)

def buscar_aluno_por_id(aluno_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, matricula, turma, turno
        FROM alunos
        WHERE id =  %s
    """, (aluno_id,))

    aluno = cursor.fetchall()
    conn.close()
    return aluno

def atualizar_aluno(aluno_id, nome, matricula, turma, turno):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE alunos
        SET nome=%s, matricula=%s, turma=%s, turno=%s
        WHERE id=%s
    """, (nome, matricula, turma, turno, aluno_id))

    conn.commit()
    conn.close()

def inativar_aluno(aluno_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE alunos
        SET status = 'Inativo'
        WHERE id = %s
    """, (aluno_id,))

    conn.commit()
    conn.close()
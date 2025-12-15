from datetime import datetime
from sqlalchemy.orm import Session
from .tabelas_do_bd import engine, Professor, Turma, Materia, Aluno, Falta

def AtualizarTurma(id_turma, novo_nome_turma):
  with Session(engine) as session:
    turma = session.query(Turma).filter(Turma.id == id_turma).first()
    
    if turma:
      turma.nome_turma = novo_nome_turma
      session.commit()

def AtualizarProfessor(id_professor, novo_nome, novo_email, nova_senha):
  with Session(engine) as session:
    professor = session.query(Professor).filter(Professor.id == id_professor).first()

    if professor:
      professor.nome = novo_nome
      professor.email_institucional = novo_email
      professor.senha = nova_senha
      session.commit()

def AtualizarAluno(id_aluno, novo_nome, novo_id_turma):
  with Session(engine) as session:
    aluno = session.query(Aluno).filter(Aluno.id == id_aluno).first()

    if aluno:
      aluno.nome = novo_nome
      aluno.id_turma = novo_id_turma
      session.commit()

def AtualizarMateria(id_materia, novo_nome_materia, novo_id_professor):
  with Session(engine) as session:
    materia = session.query(Materia).filter(Materia.id == id_materia).first()

    if materia:
      materia.nome_materia = novo_nome_materia
      materia.id_professor = novo_id_professor
      session.commit()

def AtualizarFalta(id_falta, nova_data_str):
  with Session(engine) as session:
    falta = session.query(Falta).filter(Falta.id == id_falta).first()

    if falta:
      data = datetime.strptime(nova_data_str, "%Y-%m-%d").date()
      falta.data_falta = data
      session.commit()
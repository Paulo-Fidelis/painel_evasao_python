from datetime import datetime
from sqlalchemy.orm import Session
from tabelas_do_bd import engine, Professor, Turma, Materia, Aluno, Falta

def DeletarProfessor(email_institucional, senha):
  
  with Session(engine) as session:
    delete = session.query(Professor).filter_by(email_institucional=email_institucional, senha=senha).first()
    session.delete(delete)
    session.commit()

def DeletarAluno(nome):

  with Session(engine) as session:
    delete = session.query(Aluno).filter_by(nome = nome).first()
    session.delete(delete)
    session.commit()


def DeletarFalta(nome_aluno, data_str):

  data = datetime.strptime(data_str, "%Y-%m-%d").date()

  with Session(engine) as session:
    aluno = session.query(Aluno).filter(nome = nome_aluno).first()
    delete = session.query(Falta).filter_by(data_falta = data, id_aluno = aluno.id).first()

    session.delete(delete)
    session.commit()

def DeletarMatéria(nome_materia):
  
  with Session(engine) as session:
    delete = session.query(Materia).filter_by(nome_materia = nome_materia).first()
    session.delete(delete)
    session.commit()

def DeleteTurma(nome_turma):

  with Session(engine) as session:
    delete = session.query(Turma).filter_by(nome_turma = nome_turma).first()
    session.delete(delete)
    session.commit()

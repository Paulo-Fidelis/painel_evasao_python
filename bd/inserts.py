from datetime import datetime
from sqlalchemy.orm import Session

from .tabelas_do_bd import engine, Professor, Turma, Materia, Aluno, Falta

def AdicionarTurma(nome_turma):
  
  with Session(engine) as session:
    
    novaTurma = Turma(
      nome_turma = nome_turma
    ) 
    
    session.add(novaTurma)
    session.commit()


def AdicionarProfessorComMatéria(nome, email_institucional, senha, materia, id_turma):
  with Session(engine) as session:
    
    novaMateria = Materia(
      nome_materia = materia,
      id_turma = id_turma
    )
    
    novoProfessor = Professor(
      nome = nome,
      email_institucional = email_institucional,
      senha = senha,
      materia = novaMateria
    )

    session.add(novoProfessor)

    session.commit()


def AdicionarAlunoComTurma(nome, id_turma):
  with Session(engine) as session:

    novoAluno = Aluno(
      nome = nome,
      id_turma = id_turma
    )

    session.add(novoAluno)
    session.commit()

def AdicionarFalta(data_str, nome_aluno, nome_materia):
  with Session(engine) as session:
    
    aluno = session.query(Aluno).filter(Aluno.nome == nome_aluno).first()
    materia  = session.query(Materia).filter(Materia.nome_materia == nome_materia).first()

    data = datetime.strptime(data_str, "%Y-%m-%d").date()

    novaFalta = Falta(
      data_falta = data,
      id_turma = aluno.id_turma,
      id_aluno = aluno.id,
      id_materia = materia.id
    )
    
    session.add(novaFalta)
    session.commit()

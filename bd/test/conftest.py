from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from ..tabelas_do_bd import  Turma, Aluno, Materia, Professor, Falta, engine
from datetime import datetime
import pytest

Session = sessionmaker(bind=engine)

@pytest.fixture(scope="session")
def db_session():
    """Sessão do banco de dados para cada teste"""
    session = Session()
    yield session
    session.rollback()
    session.close()

# Fixtures para entidades de teste
@pytest.fixture(scope="session")
def Turma_valida(db_session): # posso colocar um parâmetro nome turma, para evitar ter 3 fixtures que fazem a mesma coisa
    """Cria uma turma válida para testes"""
    turma = Turma(nome_turma="teste turma")
    db_session.add(turma)
    db_session.commit()
    return turma

@pytest.fixture(scope="session")
def Turma_A(db_session):
    turma = Turma(nome_turma="Turma A")
    db_session.add(turma)
    db_session.commit()
    return turma

@pytest.fixture(scope="session")
def Turma_B(db_session):
    turma = Turma(nome_turma="Turma B")
    db_session.add(turma)
    db_session.commit()
    return turma 

@pytest.fixture(scope="session")
def Falta_valida(db_session, Aluno_valido, Materia_valida, Turma_valida):
    
    dataValida = datetime.strptime("2025-12-22", "%Y-%m-%d").date()
    
    falta_valida = Falta(
        data_falta = dataValida, 
        id_turma = Turma_valida.id,
        id_aluno = Aluno_valido.id,
        id_materia = Materia_valida.id
    )
    
    db_session.add(falta_valida)
    db_session.commit()
    
    return falta_valida

@pytest.fixture(scope="session")
def Professor_valido(db_session, Turma_valida): # Feito para as defs de update 
    
    materia_valida = Materia(
        nome_materia = "Matemática",
        id_turma = Turma_valida.id
    )
    professor_valido = Professor(
        nome = "Carlos",
        email_institucional = "carlos@professor",
        senha = "123",
        materia = materia_valida
    )
    
    db_session.add(professor_valido)
    db_session.commit()
    
    return professor_valido
  

@pytest.fixture(scope="session")
def Aluno_valido(db_session, Turma_valida):
    
    aluno_valido = Aluno(nome = "Osvaldo", id_turma = Turma_valida.id)
    
    db_session.add(aluno_valido)
    db_session.commit()
    
    return aluno_valido

@pytest.fixture(scope="session")
def Materia_valida(Turma_valida,db_session):
    
    professor_valido = Professor(nome="Lucas",email_institucional="lucas@professor",senha="123")
    db_session.add(professor_valido)
    db_session.commit()
    
    materia_valida = Materia(
        nome_materia = "Português",
        id_turma = Turma_valida.id,
        id_professor = professor_valido.id
    )
    
    db_session.add(materia_valida)
 
    db_session.commit()
    
    return materia_valida
    

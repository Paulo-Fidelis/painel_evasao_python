from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.orm import sessionmaker

from ..tabelas_do_bd import Falta, Aluno, Materia, Turma, Professor, engine
from ..inserts import AdicionarFalta
from ..delete import DeletarFalta
from ..update import AtualizarFalta

from datetime import datetime
import pytest

Session = sessionmaker(bind=engine)

@pytest.fixture(scope="module") 
def db_session(): #  Cria uma sessão temporária do bd para os testes
   
    session = Session()
    
    yield session
    
    session.rollback()
    session.close()
    
@pytest.fixture(scope="module")
def Turma_valida(db_session):
    
    turma_valida = Turma(nome_turma = "9º B")
    
    db_session.add(turma_valida)
    db_session.commit()    
    
    return turma_valida

@pytest.fixture(scope="module")
def Aluno_valido(db_session, Turma_valida):
    
    aluno_valido = Aluno(nome = "Pedro", id_turma = Turma_valida.id)
    
    db_session.add(aluno_valido)
    db_session.commit()
    
    return aluno_valido

@pytest.fixture(scope="module")
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


# Acredito que para Faltas, é né

class TestFalta: 
    
    # Insert tests
    
    def test_insert_Falta_valida(self, db_session, Aluno_valido, Materia_valida):
        
        dataValida = "2025-12-09"
        AdicionarFalta(dataValida, Aluno_valido.nome, Materia_valida.nome_materia)
        
        falta =  db_session.query(Falta).filter(Falta.id_aluno == Aluno_valido.id, Falta.id_materia == Materia_valida.id).first()
        data = datetime.strptime(dataValida, "%Y-%m-%d").date()
        
        assert falta is not None
        assert falta.id_aluno == Aluno_valido.id
        assert falta.id_materia == Materia_valida.id
        assert falta.id_turma == Materia_valida.id_turma
        assert falta.data_falta == data
    
    def test_insert_Falta_multiplas(self, db_session, Aluno_valido, Materia_valida):
        
        dataValida = "2025-12-12"
        
        AdicionarFalta(dataValida, Aluno_valido.nome, Materia_valida.nome_materia)
        AdicionarFalta(dataValida, Aluno_valido.nome, Materia_valida.nome_materia)
        AdicionarFalta(dataValida, Aluno_valido.nome, Materia_valida.nome_materia)
        
        data = datetime.strptime(dataValida, "%Y-%m-%d").date()
        faltas =  db_session.query(Falta).filter(Falta.id_aluno == Aluno_valido.id, Falta.id_materia == Materia_valida.id, Falta.data_falta == data).all()
       
        assert faltas is not None
        assert len(faltas) == 3
        assert faltas[0].id_aluno == Aluno_valido.id
        
    @pytest.mark.xfail(raises=AttributeError, reason="Uma falta precisa de um aluno para existir")
    def test_insert_Falta_sem_aluno(sef, Materia_valida):
        
        dataValida = "2025-12-11"
        try:
            AdicionarFalta(dataValida, None, Materia_valida.nome_materia)
            
        except AttributeError:
            
            raise
    
    @pytest.mark.xfail(raises=AttributeError, reason="Uma falta precisa de uma materia para existir")
    def test_insert_Falta_sem_materia(sef, Aluno_valido):
        
        dataValida = "2025-12-11"
        
        try:
            AdicionarFalta(dataValida, Aluno_valido.nome, None)
            
        except AttributeError:
            
            raise
    
    @pytest.mark.xfail(raises=TypeError, reason="Uma falta precisa de uma data para existir")
    def test_insert_Falta_sem_data(sef, Aluno_valido, Materia_valida):
        
        try:
            
            AdicionarFalta(None, Aluno_valido.nome, Materia_valida.nome_materia)
            
        except TypeError:
            
            raise
        
    # Updates test
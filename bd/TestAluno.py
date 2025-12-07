from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.orm import sessionmaker
from tabelas_do_bd import Aluno, Turma, engine
from inserts import AdicionarAlunoComTurma
from update import AtualizarAluno
from delete import DeletarAluno
import pytest
    
Session = sessionmaker(bind=engine)

@pytest.fixture(scope="module") 
def db_session(): # Cria uma sessão temporária do bd para os testes
   
    session = Session()
    
    yield session
    #session.query(Turma).filter(Turma.nome_turma == "oi").delete()
    session.rollback()
    session.close()
 
# Especialmente criadas para os testes de update    
@pytest.fixture(scope="module")
def Turma_A(db_session):
    turma = Turma(nome_turma="Turma A")
    db_session.add(turma)
    db_session.commit()
    return turma

@pytest.fixture(scope="module")
def Turma_B(db_session):
    turma = Turma(nome_turma="Turma B")
    db_session.add(turma)
    db_session.commit()
    return turma   

@pytest.fixture(scope="module")
def Aluno_valido(db_session, Turma_A):
    
    aluno_valido = Aluno(nome = "Osvaldo", id_turma = Turma_A.id)
    
    db_session.add(aluno_valido)
    db_session.commit()
    
    return aluno_valido
    

class TestAluno:
    
    def test_insert_aluno_valido(self, db_session,Turma_A):
        
        AdicionarAlunoComTurma("Maria", Turma_A.id)
        
        aluno = db_session.query(Aluno).filter(Aluno.nome == "Maria", Aluno.id_turma == Turma_A.id).first()
        assert aluno is not None
        assert aluno.nome == "Maria"
        assert aluno.id_turma == Turma_A.id
    
    @pytest.mark.xfail(raises=IntegrityError, reason="Aluno precisa de turma")        
    def test_insert_aluno_sem_turma(self, db_session):
        try:
            AdicionarAlunoComTurma("Pedro", None)
        except IntegrityError:
            raise
    
    #Update testes
    
    def test_update_aluno_valido(self, db_session, Aluno_valido, Turma_B):
        
        AtualizarAluno(Aluno_valido.id, "Osvaldo Freitas", Turma_B.id)
        
        db_session.expire_all()
        
        aluno = db_session.query(Aluno).filter(Aluno.id == Aluno_valido.id).first()
        
        assert aluno is not None
        assert aluno.nome == "Osvaldo Freitas"
        assert aluno.id_turma == Turma_B.id
    
    def test_update_aluno_turma(self,db_session, Aluno_valido, Turma_B):
       
        AtualizarAluno(Aluno_valido.id, Aluno_valido.nome, Turma_B.id)
        
        db_session.expire_all()
        
        aluno = db_session.query(Aluno).filter(Aluno.id == Aluno_valido.id).first()
        assert aluno is not None
        assert aluno.nome == Aluno_valido.nome
        assert aluno.id == Aluno_valido.id
        assert aluno.id_turma == Turma_B.id
    
    def test_update_aluno_nome(self,db_session, Aluno_valido):
        
        AtualizarAluno(Aluno_valido.id, "Osvaldo Ronaldo", Aluno_valido.id_turma)
        
        db_session.expire_all()
        
        aluno = db_session.query(Aluno).filter(Aluno.id == Aluno_valido.id).first()
        
        assert aluno is not None
        assert aluno.nome == "Osvaldo Ronaldo"
        assert aluno.id == Aluno_valido.id
        assert aluno.id_turma ==  Aluno_valido.id_turma

    @pytest.mark.xfail(raises=IntegrityError, reason="Id da turma é obrigatório")    
    def test_update_aluno_sem_turma(self,db_session, Aluno_valido):
        try:
            AtualizarAluno(Aluno_valido.id, "Osvaldo Freitas", None)
        except IntegrityError:
            raise
    
    @pytest.mark.xfail(raises=IntegrityError, reason="Id do aluno é obrigatório")    
    def test_update_aluno_sem_id(self,db_session, Turma_A):
        try:
            AtualizarAluno(None, "Osvaldo Freitas", Turma_A.id)
        except IntegrityError:
            raise  
        
    #Delete testes
    
    def test_delete_aluno_valido(self,db_session,Aluno_valido):
        DeletarAluno(Aluno_valido.id,Aluno_valido.nome)
        
        aluno = db_session.query(Aluno).filter(Aluno.id == Aluno_valido.id).all()
        
        assert len(aluno) == 0
    
    
    @pytest.mark.xfail(raises=UnmappedInstanceError, reason="Id do aluno é obrigatório")    
    def test_delete_aluno_sem_id(self,db_session,Aluno_valido):
        DeletarAluno(None,Aluno_valido.nome)
        
   
        
  
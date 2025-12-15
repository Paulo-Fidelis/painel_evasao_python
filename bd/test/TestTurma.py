from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.orm import sessionmaker

from ..tabelas_do_bd import Turma, engine
from ..inserts import AdicionarTurma
from ..delete import DeleteTurma
from ..update import AtualizarTurma

import pytest

Session = sessionmaker(bind=engine)

@pytest.fixture(scope="module") 
def db_session(): #  Cria uma sessão temporária do bd para os testes
   
    session = Session()
    
    yield session
    #session.query(Turma).filter(Turma.nome_turma == "oi").delete()
    session.rollback()
    session.close()
    
@pytest.fixture(scope="module")
def Turma_valida(db_session):
    
    turma_valida = Turma(nome_turma = "2º B")
    
    db_session.add(turma_valida)
    db_session.commit()    
    
    return turma_valida

class TestTurma:
    #Inserts testes
    def test_insert_turma_valida(self, db_session):
        
        AdicionarTurma("3º B")
        
        # Use the session to verify
        turmatest = db_session.query(Turma).filter(Turma.nome_turma == "3º B").first()
        assert turmatest is not None
        assert turmatest.nome_turma == "3º B"
        
    @pytest.mark.xfail(raises=IntegrityError, reason="Nome da turma é obrigatório")
    def test_insert_turma_sem_nome(self, db_session):
        
      try:
          
        AdicionarTurma(None)
        
      except IntegrityError:
             
        raise
    
    #Update tests
    
    def test_update_turma_valida(self,db_session, Turma_valida):
        
        AtualizarTurma(Turma_valida.id,"3º Boladão")
        
        db_session.expire_all() 
        
        testurma = db_session.query(Turma).filter(Turma.id==Turma_valida.id).first()
        
        assert testurma is not None
        assert testurma.nome_turma == "3º Boladão"
    
    @pytest.mark.xfail(raises=ValueError, reason="ID é obrigatório")
    def test_update_turma_sem_id(self, db_session, Turma_valida):
        try:
            AtualizarTurma(None, "teste")
        except ValueError: 
            raise
          
    #Delete tests
    
    def test_delete_turma_valida(self, db_session, Turma_valida):
        
        db_session.expire_all() 
        
        DeleteTurma(Turma_valida.id,Turma_valida.nome_turma)
        
        turmatest = db_session.query(Turma).filter(Turma.id == Turma_valida.id).all()
        
        assert len(turmatest) == 0
        
    @pytest.mark.xfail(raises=UnmappedInstanceError, reason="Nome é obrigatório para a função")    
    def test_delete_turma_sem_id(self,db_session):
        try: 
            DeleteTurma(None,"TEste")
        except UnmappedInstanceError:
            raise
        
  
        
        
def verificar_banco():
    """Função para verificar todas as turmas no banco"""
    session = Session()
    try:
        todas_turmas = session.query(Turma).all()
        print("\n=== TURMAS NO BANCO ===")
        for turma in todas_turmas:
            print(f"ID: {turma.id}, Nome: {turma.nome_turma}")
        print("=======================\n")
    finally:
        session.close()

# Chame antes/depois do teste
verificar_banco()
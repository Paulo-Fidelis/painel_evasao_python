from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.orm import sessionmaker

from ..tabelas_do_bd import Turma, engine
from ..inserts import AdicionarTurma
from ..delete import DeleteTurma
from ..update import AtualizarTurma

import pytest


# pytest test/ --html=relatorio.html --self-contained-html
# para rodar todos os testes de um arquivo, e gerar um html para ele

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
        
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from ..tabelas_do_bd import Professor, Materia, Turma, engine
from ..inserts import AdicionarProfessorComMatéria
from ..update import AtualizarProfessor
from ..delete import DeletarProfessor

import pytest
     
class TestProfessor:
    
    def test_insert_professor_valido(self,db_session,Turma_valida):
        
        AdicionarProfessorComMatéria("Carlos","carlos@prof","123","Biologia",Turma_valida.id)
        
        professor = db_session.query(Professor).filter(Professor.nome=="Carlos").first()
        
        assert professor is not None
        assert professor.nome == "Carlos"
     
    @pytest.mark.xfail(raises=IntegrityError, reason="Professor depende de matéria")    
    def test_insert_professor_sem_materia(self, db_session, Turma_valida):
         
        try:
            
            AdicionarProfessorComMatéria("Freitas","freitas@prof","qwer", None, Turma_valida.id)
            
        except IntegrityError:
            
            raise
    
    
    @pytest.mark.xfail(raises=IntegrityError, reason="Email é obrigatório")
    def test_insert_professor_sem_email(self, db_session, Turma_valida):
        
        try:
            
            AdicionarProfessorComMatéria("Carlos",None,"123","Biologia",Turma_valida.id)
            
        except IntegrityError:
            
            raise
    
    #updates testes
    
    def test_update_professor_valido(self,db_session, Professor_valido):
    
        AtualizarProfessor(Professor_valido.id,"Douglas","Douglas@professor","qwer")
        
        db_session.expire_all() # Pra resetar a session, evitando erro no assert, pq direcionaria pro professor criado pela fixture, ainda que tenha o mesmo ad, bizarro.
        
        professor = db_session.query(Professor).filter(Professor.id == Professor_valido.id).first()
        
        assert professor.nome == "Douglas"
        assert professor.email_institucional == "Douglas@professor"
        assert professor.senha == "qwer"
        
        
    def test_update_professor_email(self,db_session, Professor_valido):
        
        AtualizarProfessor(Professor_valido.id,"Carlos","carlos@professor",Professor_valido.senha)
        
        db_session.expire_all() 
        
        professor = db_session.query(Professor).filter(Professor.id == Professor_valido.id).first()
        
        assert professor.nome == "Carlos"
        assert professor.email_institucional == "carlos@professor"
        
    @pytest.mark.xfail(raises=IntegrityError, reason="Id é necessário")
    def test_update_professor_sem_id(self, db_session):
        
        # Nesse caso de teste realmente é só isso, já que não existe professor para ser atualizado
        try:
            AtualizarProfessor(None,"Carlos","carlos@professor","1234")
            
        except IntegrityError:
            
            raise
    
    # Delete tests
    
    def test_delete_professor_valido(self, db_session, Professor_valido):
      
        DeletarProfessor(Professor_valido.id,Professor_valido.email_institucional,Professor_valido.senha)
        
        dele = db_session.query(Professor).filter(Professor.id == Professor_valido.id).all()
        
        assert len(dele) == 0
   
    @pytest.mark.xfail(reason="Id é necessário")
    def test_delete_professor_sem_id(self, db_session, Professor_valido):
          
        try:
            
            DeletarProfessor(None,Professor_valido.email_institucional, Professor_valido.senha)
            
        except:
            
            raise
    
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.orm import sessionmaker
from tabelas_do_bd import Professor, Materia, Turma, engine
from inserts import AdicionarProfessorComMatéria
from update import AtualizarMateria
from delete import DeletarMatéria
import pytest
    
Session = sessionmaker(bind=engine)

@pytest.fixture(scope="module") 
def db_session(): # Cria uma sessão temporária do bd para os testes
   
    session = Session()
    
    yield session
    #session.query(Turma).filter(Turma.nome_turma == "oi").delete()
    session.rollback()
    session.close()
    
@pytest.fixture(scope="module")
def Turma_valida(db_session):
    
    turma_valida = Turma(nome_turma = "12º")
    
    db_session.add(turma_valida)
    db_session.commit()    
    
    return turma_valida

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
    
class TestMateria: # Materia não tem insert próprio, fiz apenas testes para update e delete
    
    #Updates
    
    def test_update_materia_valida(self,db_session,Materia_valida):
        
        professor_novo =  Professor(nome="Rogério", email_institucional="rogerio@professor", senha="123")
        
        db_session.add(professor_novo)
        db_session.commit()
        
        AtualizarMateria(Materia_valida.id,"Calculo 1",professor_novo.id)
         
        db_session.expire_all() 
        
        materia = db_session.query(Materia).filter(Materia.id == Materia_valida.id).first()
        
        assert materia.nome_materia == "Calculo 1"
        assert materia.id_professor == professor_novo.id
        
    def test_update_materia_trocar_professor(self, db_session, Materia_valida):
        
        db_session.expire_all() 
        
        professor_novo =  Professor(nome="Rogério", email_institucional="rogerio@professor", senha="123")
        
        db_session.add(professor_novo)
        db_session.commit()
        
        AtualizarMateria(Materia_valida.id, Materia_valida.nome_materia, professor_novo.id)
        
          
        db_session.expire_all() 
        
        materia = db_session.query(Materia).filter(Materia.id == Materia_valida.id).first()
        
        assert materia.nome_materia == "Português"
        assert materia.id_professor == professor_novo.id
    
    @pytest.mark.xfail(raises=IntegrityError, reason="Id é necessário")
    def test_update_materia_sem_id(self,db_session,Materia_valida):
        try:
            # Neste caso, a matéria, prof e turma são criados, mas a matéria não é atualizada
            AtualizarMateria(None, "Calculo 2", Materia_valida.id_professor)             
            
        except IntegrityError:
            raise
        
    @pytest.mark.xfail(raises=IntegrityError, reason="Professor Id é necessário")        
    def test_update_materia_sem_professor(self,db_session,Materia_valida):
        try:
            
            AtualizarMateria(Materia_valida.id, "Calculo 2", None)
            
        except IntegrityError:
            
            raise
    
    #Delete tests
    
    def test_delete_materia_valida(self,db_session,Materia_valida):
        
        DeletarMatéria(Materia_valida.id,Materia_valida.nome_materia)
        
        materia = db_session.query(Materia).filter(Materia.id == Materia_valida.id).all()
        
        assert len(materia) == 0
        
    @pytest.mark.xfail(raises=UnmappedInstanceError, reason="Id é obrigatório para deletar")
    def test_delete_materia_sem_id(self,db_session,Materia_valida):
        try:
            DeletarMatéria(None,"Português")
        except UnmappedInstanceError:
            raise
        
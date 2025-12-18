from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.orm import sessionmaker

from ..tabelas_do_bd import Falta, Aluno, Materia, Turma, Professor, engine
from ..inserts import AdicionarFalta
from ..delete import DeletarFalta
from ..update import AtualizarFalta

from datetime import datetime
import pytest

# Acredito que para Faltas, é necessário adicionar, na função de insert, uma dependência de qtd de faltas.

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
    
    def test_update_Falta_valida(self, db_session,Falta_valida):
        NovaData = "2025-12-20"
        AtualizarFalta(Falta_valida.id, NovaData)
        
        db_session.expire_all()
        
        falta = db_session.query(Falta).filter(Falta.id == Falta_valida.id).first()
        data = datetime.strptime(NovaData, "%Y-%m-%d").date()
        
        assert falta is not None
        assert falta.id == Falta_valida.id
        assert falta.data_falta == data
        
    @pytest.mark.xfail(reases=ValueError, reason="A data deve está nos limites de um calendário")        
    def test_update_Falta_data_excedida(self, Falta_valida):
        
        dataExcedida = "2025-13-19"
        
        try:
            
            AtualizarFalta(Falta_valida.id, dataExcedida)
            
        except ValueError:
            
            raise
    
    @pytest.mark.xfail(reases=TypeError, reason="Uma falta precisa de uma data")    
    def test_update_Falta_sem_data(self, Falta_valida):
        
        try:
            
            AtualizarFalta(Falta_valida.id, None)
            
        except TypeError:
            
            raise
    
    # delete tests
    
    def test_delete_Falta_valida(self, db_session, Falta_valida, Aluno_valido):
        
        data = Falta_valida.data_falta.strftime("%Y-%m-%d")
        
        DeletarFalta(Aluno_valido.nome, data)
        
        falta = db_session.query(Falta).filter(
            Falta.id == Falta_valida.id,
            Falta.id_aluno == Aluno_valido.id,
            Falta.data_falta == Falta_valida.data_falta
        ).all()
        
        assert len(falta) == 0
        
    @pytest.mark.xfail(reases=TypeError, reason="Uma falta precisa de uma data")
    def test_delete_Falta_sem_data(self,  Aluno_valido, Falta_valida):
        
        data = Falta_valida.data_falta.strftime("%Y-%m-%d") # Para que a falta seja criada
        
        try:
            
            DeletarFalta(Aluno_valido.nome, None)        
            
        except TypeError:
            
            raise
            
            
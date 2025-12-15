from sqlalchemy import Column, Integer, String, Date, ForeignKey, UniqueConstraint, create_engine
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class Professor(Base):
    __tablename__ = 'professores'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email_institucional = Column(String(40), nullable=False)
    senha = Column(String(20), nullable=False)

    materia = relationship("Materia", back_populates="professor", uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Professor(id={self.id}, nome='{self.nome}', email='{self.email_institucional}')>"

class Turma(Base):
    __tablename__ = 'turmas'

    id = Column(Integer, primary_key=True)
    nome_turma = Column(String(50), nullable=False)

    alunos = relationship("Aluno", back_populates="turma", cascade="all, delete-orphan")
    materias = relationship("Materia", back_populates="turma", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Turma(id={self.id}, nome_turma='{self.nome_turma}')>"

class Aluno(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    
    id_turma = Column(Integer, ForeignKey("turmas.id"), nullable=False)
    
    turma = relationship("Turma", back_populates="alunos")
    faltas = relationship("Falta", back_populates="aluno", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Aluno(id={self.id}, nome='{self.nome}', id_turma={self.id_turma})>"

class Materia(Base):
    __tablename__ = 'materias'

    id = Column(Integer, primary_key=True)
    nome_materia = Column(String(30), nullable=False)


    id_turma = Column(Integer, ForeignKey("turmas.id"), nullable=False)
    id_professor = Column(Integer, ForeignKey("professores.id"), unique=True, nullable=False)

    turma = relationship("Turma", back_populates="materias")
    professor = relationship("Professor", back_populates="materia")
    faltas = relationship("Falta", back_populates="materia", cascade="all, delete-orphan")

    __table_args__ = (
        UniqueConstraint('id_professor', 'id_turma', name='uix_professor_turma'),
    )

    def __repr__(self):
        return f"<Materia(id={self.id}, nome_materia='{self.nome_materia}', id_turma={self.id_turma})>"

class Falta(Base): 
    __tablename__ = 'faltas'

    id = Column(Integer, primary_key=True)
    data_falta = Column(Date, nullable=False)

    id_turma = Column(Integer, ForeignKey("turmas.id"), nullable=False)
    id_aluno = Column(Integer, ForeignKey("alunos.id"), nullable=False)
    id_materia = Column(Integer, ForeignKey("materias.id"), nullable=False)

    turma = relationship("Turma")
    aluno = relationship("Aluno", back_populates="faltas")
    materia = relationship("Materia", back_populates="faltas")


    def __repr__(self):
        return f"<Falta(id={self.id}, data='{self.data_falta}', id_aluno={self.id_aluno}, id_materia={self.id_materia})>"
    


engine = create_engine("sqlite:///escola.db")
Base.metadata.create_all(engine)
from typing import Union, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests
from sqlalchemy.orm import Session

# --- configurações e funções importantes
from bd.tabelas_do_bd import engine, Professor, Turma, Materia, Aluno, Falta
from bd.inserts import (
    AdicionarTurma,
    AdicionarAlunoComTurma,
    AdicionarProfessorComMatéria,
    AdicionarFalta,
)
from bd.update import (
    AtualizarAluno,
    AtualizarProfessor,
    AtualizarTurma,
    AtualizarFalta,
    AtualizarMateria,
)

load_dotenv()


ANYTHINGLLM_API_URL = "http://localhost:3001/api/v1"
API_KEY = os.getenv("ANYTHING_LLM_API_KEY")

headers = {"accept": "application/json", "Authorization": f"Bearer {API_KEY}"}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- modelos para busca ---


class ProfessorResponse(BaseModel):
    id: int
    nome: str
    email_institucional: str

    class Config:
        from_attributes = True


class CadastroAluno(BaseModel):
    nome: str
    nome_turma: str


class CadastroUsuario(BaseModel):
    nome: str
    email: str
    senha: str
    nome_materia: str
    nome_turma: str


class Login(BaseModel):
    email: str
    senha: str


class FaltaModel(BaseModel):
    data: str
    nome_aluno: str
    nome_materia: str


# --- rotas ---


@app.post("/adicionarAluno")
def adicionarAluno(user: CadastroAluno):
    with Session(engine) as session:
        turma = (
            session.query(Turma.id).filter(Turma.nome_turma == user.nome_turma).first()
        )

        if not turma:
            return {"mensagem": "essa turma não existe"}

        AdicionarAlunoComTurma(nome=user.nome, id_turma=turma.id)

    return {"mensagem": "Cadastro realizado com sucesso"}


@app.get("/llmResponse/{prompt}")
def llmResponse(prompt: str):
    endpoint = f"{ANYTHINGLLM_API_URL}/workspace/legal/chat"
    dados = {"message": prompt, "mode": "chat"}

    try:
        response = requests.post(endpoint, json=dados, headers=headers)
        response.raise_for_status()
        data = response.json()

        resposta = data.get("textResponse")
        return {"response": resposta}
    except Exception as e:
        print(f"Erro na LLM: {e}")
        raise HTTPException(status_code=500, detail="Erro ao comunicar com a IA")


@app.post("/login")
def login(user: Login):
    with Session(engine) as session:
        professor = (
            session.query(Professor)
            .filter(
                Professor.email_institucional == user.email,
                Professor.senha == user.senha,
            )
            .first()
        )

    if not professor:
        raise HTTPException(status_code=400, detail="Email ou senha incorretos")

    professor_dados = ProfessorResponse.model_validate(professor)

    return {"mensagem": "Login realizado com sucesso", "professor": professor_dados}


@app.post("/cadastro")
def cadastro(cadstro: CadastroUsuario):
    with Session(engine) as session:
        turma = (
            session.query(Turma).filter(Turma.nome_turma == cadstro.nome_turma).first()
        )

        id_turma = None
        if not turma:
            AdicionarTurma(cadstro.nome_turma)
            turma_nova = (
                session.query(Turma)
                .filter(Turma.nome_turma == cadstro.nome_turma)
                .first()
            )
            id_turma = turma_nova.id
        else:
            id_turma = turma.id

        AdicionarProfessorComMatéria(
            nome=cadstro.nome,
            email_institucional=cadstro.email,
            senha=cadstro.senha,
            materia=cadstro.nome_materia,
            id_turma=id_turma,
        )

    return {"mensagem": "Cadastro realizado com sucesso"}


@app.post("/registrar-falta")
def registrar_falta(dados: FaltaModel):
    with Session(engine) as session:
        auth_aluno = session.query(Aluno).filter(Aluno.nome == dados.nome_aluno).first()
        if auth_aluno:
            AdicionarFalta(dados.data, dados.nome_aluno, dados.nome_materia)
        else:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")

    return {"mensagem": "Falta registrada com sucesso"}


@app.get("/minhas-turmas/{id_professor}")
def listar_turmas(id_professor: int):
    with Session(engine) as session:
        resultados = (
            session.query(Turma)
            .join(Materia, Turma.id == Materia.id_turma)
            .filter(Materia.id_professor == id_professor)
            .all()
        )

        lista_turmas = [
            {"id_turma": t.id, "nome_turma": t.nome_turma} for t in resultados
        ]

    return {
        "professor_id": id_professor,
        "total_turmas": len(lista_turmas),
        "turmas": lista_turmas,
    }

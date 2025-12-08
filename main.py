from typing import Union, Optional
from datetime import datetime, timedelta
from fastapi import FastAPI, Cookie, HTTPException, Depends, Response, status
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import jwt
from sqlalchemy.orm import Session
from bd.tabelas_do_bd import engine, Professor 

load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

class Login(BaseModel):
    email: str 
    senha: str


def criar_token_acesso(dados: dict):

    a_codificar = dados.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    a_codificar.update({"exp": expiracao})
    encoded_jwt = jwt.encode(a_codificar, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def get_usuario_atual(token: Optional[str] = Cookie(None)):

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não autenticado",
        )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")



        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return email 
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Erro de validação do token")

@app.post('/login')
def login(user: Login, response: Response):
    
    with Session(engine) as session:
        professor = session.query(Professor).filter(
            Professor.email_institucional == user.email,
            Professor.senha == user.senha
        ).first()
    
    if not professor:
        raise HTTPException(status_code=400, detail="Email ou senha incorretos")

    
    token_jwt = criar_token_acesso(dados={"sub": professor.email_institucional})

    
    response.set_cookie(
        key="access_token", 
        value=token_jwt, 
        httponly=True,   
        max_age=1800,    
        samesite="lax",  
        secure=False     
    )

    return {"mensagem": "Login realizado com sucesso"}

@app.post('/logout')
def logout(response: Response):
    
    response.delete_cookie(key="access_token")
    return {"mensagem": "Logout realizado"}


@app.get('/minhas-turmas')
def listar_turmas(usuario_email: str = Depends(get_usuario_atual)):
    return {"usuario_logado": usuario_email, "dados": "Lista de turmas..."}
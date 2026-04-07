from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Parceiro(BaseModel):
    cnpj: str
    nome: str
    tipo: str
    whatsapp: str
    especialidades: List[str]

banco_parceiros = []

@app.get("/")
def home():
    return {
        "status": "Cerebro v2.0 Ativo",
        "audio": "Ambiente 10s | Motor 10s-20s"
    }

@app.post("/cadastrar_parceiro")
def cadastrar(parceiro: Parceiro):
    if len(parceiro.cnpj) < 14:
        raise HTTPException(status_code=400, detail="CNPJ Invalido")
    banco_parceiros.append(parceiro)
    return {"mensagem": "Sucesso!"}

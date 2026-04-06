from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "Cerebro do Meu Mecanico Ativo",
        "versao": "2026.1",
        "autor": "Helder",
        "sistema": "Operacional"
    }

@app.get("/diagnostico")
def teste():
    return {
        "resultado": "Pronto para receber audio",
        "chave_seguranca": "meu_mecanico_2026_pro",
        "instrucao": "Envie o arquivo .WAV para analise"
    }

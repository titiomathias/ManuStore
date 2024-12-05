from fastapi import FastAPI

app = FastAPI()

app.include_router()

# GET endpoints de consulta
@app.get("/")
def home():
    return "Fala, Guys"

@app.get("/consulta-estoque")
def consulta_estoque():
    return "estoque"

@app.get("/consulta-entrada")
def consulta_entrada():
    return "entrada"

@app.get("/consulta-saida")
def consulta_entrada():
    return "entrada"



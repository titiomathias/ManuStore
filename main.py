from fastapi import FastAPI
from routers import entrada, estoque, saida, report, backup

app = FastAPI()

@app.get("/")
def home():
    return "Bem-vindo a minha API!"

app.include_router(entrada.router, tags=["Entrada"])
app.include_router(estoque.router, tags=["Estoque"])
app.include_router(saida.router, tags=["Saida"])
app.include_router(report.router, tags=["Report"])
app.include_router(backup.router, tags=["Backup"])


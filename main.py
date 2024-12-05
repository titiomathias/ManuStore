from fastapi import FastAPI
from routers import entrada, estoque, saida, report, backup

app = FastAPI()

@app.get("/")
def home():
    return "Bem-vindo a minha API!"

app.include_router(entrada.router, prefix="/entrada", tags=["Entrada"])
app.include_router(estoque.router, prefix="/estoque", tags=["Estoque"])
app.include_router(saida.router, prefix="/saida", tags=["Saida"])
app.include_router(report.router, prefix="/report", tags=["Report"])
app.include_router(backup.router, prefix="/backup", tags=["Backup"])


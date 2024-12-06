from fastapi import APIRouter, HTTPException, Depends


router = APIRouter()

@router.get("/")
def saida():
    return "todas as saídas"

@router.get("/{codigo}")
def saida(codigo: int):
    return f"Saída de codigo: {codigo}"

@router.post("/")
async def add_saida(dados: dict):
    return dados

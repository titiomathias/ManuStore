from fastapi import APIRouter, HTTPException, Depends


router = APIRouter()

@router.get("/")
def entrada():
    return "todas as entradas"

@router.get("/{codigo}")
def entrada(codigo: int):
    return f"Entrada de codigo: {codigo}"

@router.post("/")
def add_entrada(dados: dict):
    return dados
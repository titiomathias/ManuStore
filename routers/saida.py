from fastapi import APIRouter, HTTPException, Depends


router = APIRouter()

@router.get("/saida")
def saida():
    return "todas as saídas"

@router.get("/saida/{codigo}")
def saida(codigo: int):
    return f"Saída de codigo: {codigo}"


from fastapi import APIRouter, HTTPException, Depends


router = APIRouter()

@router.get("/entrada")
def entrada():
    return "todas as entradas"

@router.get("/entrada/{codigo}")
def entrada(codigo: int):
    return f"Entrada de codigo: {codigo}"



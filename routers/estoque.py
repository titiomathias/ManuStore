from fastapi import APIRouter, HTTPException, Depends


router = APIRouter()

@router.get("/")
def estoque():
    return "estoque completo"

@router.get("/{codigo}")
def estoque(codigo: int):
    return f"produto de codigo: {codigo}"

@router.post("/")
async def add_estoque(dados: dict):
    return dados


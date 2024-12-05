from fastapi import APIRouter, HTTPException, Depends


router = APIRouter()

@router.get("/estoque")
def estoque():
    return "estoque completo"

@router.get("/estoque/{codigo}")
def estoque(codigo: int):
    return f"produto de codigo: {codigo}"



from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..dependencies import get_db

router = APIRouter()

@router.get("/estoque")
def estoque():
    return "estoque completo"

@router.get("/estoque/{codigo}")
def estoque(codigo: int):
    return f"produto de codigo: {codigo}"



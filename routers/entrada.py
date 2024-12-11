from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Estoque
from db import get_db

router = APIRouter()

@router.get("/")
def entrada():
    return "todas as entradas"

@router.get("/{codigo}")
def entrada(codigo: int):
    return f"Entrada de codigo: {codigo}"

@router.post("/")
async def add_entrada(dados: dict):
    return dados

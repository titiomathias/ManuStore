from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from .entrada import entrada_all
from .saida import saida, saida_all
from .estoque import estoque, estoque_all

router = APIRouter()

def get_data(db):
    entradas = entrada_all(db)
    saidas = saida_all(db)
    estoque = estoque_all(db)

    print(entradas)
    print(saidas)
    print(estoque)

@router.get("/")
def report(db: Session = Depends(get_db)):
    get_data(db)
    return "Relatório completo"
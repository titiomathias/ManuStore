from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Entrada
from db import get_db

router = APIRouter()

@router.get("/")
def entrada(db: Session = Depends(get_db)):
    entradas = db.query(Entrada).all()
    return entradas

@router.get("/{codigo}")
def entrada(codigo: int, db: Session = Depends(get_db)):
    item = db.query(Entrada).filter(Entrada.id == codigo).first()

    if not item:
        raise HTTPException(status_code=404, detail=f"Entrada com código {codigo} não encontrada nos registros.")

    return item

@router.post("/")
async def add_entrada(id_codigo: int, quantidade: int, valor_peca: float, frete_peca: float, lucro_peca: float, lucro_total: float, db: Session = Depends(get_db)):
    nova_entrada = Entrada(
        id_codigo=id_codigo,
        quantidade=quantidade,
        valor_peca=valor_peca,
        frete_peca=frete_peca,
        lucro_peca=lucro_peca,
        lucro_total=lucro_total
    )
    db.add(nova_entrada)
    db.commit()
    db.refresh(nova_entrada)
    return nova_entrada

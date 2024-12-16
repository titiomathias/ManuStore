from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Estoque
from db import get_db

router = APIRouter()

@router.get("/")
def estoque(db: Session = Depends(get_db)):
    estoque = db.query(Estoque).all()
    return estoque

@router.get("/{codigo}")
def estoque(codigo: str, db: Session = Depends(get_db)):
    item = db.query(Estoque).filter(Estoque.codigo == codigo).first()

    if not item:
        raise HTTPException(status_code=404, detail=f"Produto com código {codigo} não encontrado no estoque.")

    return item

@router.post("/")
async def criar_item_estoque(codigo: str, fornecedor: str, descricao: str, estoque_atual: int, db: Session = Depends(get_db)):
    novo_item = Estoque(
        codigo=codigo,
        fornecedor=fornecedor,
        descricao=descricao,
        estoque_atual=estoque_atual
    )
    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)
    return novo_item

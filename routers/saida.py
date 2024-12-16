from fastapi import APIRouter, HTTPException, Depends
from models import Saida
from sqlalchemy.orm import Session
from db import get_db

router = APIRouter()

@router.get("/")
def saida(db: Session = Depends(get_db)):
    saidas = db.query(Saida).all()
    return saidas

@router.get("/{codigo}")
def saida(codigo: int, db: Session = Depends(get_db)):
    item = db.query(Saida).filter(Saida.id == codigo).first()

    if not item:
        raise HTTPException(status_code=404, detail=f"saída com código {codigo} não encontrada nos registros.")

    return item

@router.post("/")
async def add_saida(id_codigo: int, quantidade: int, valor_venda: float, forma_pagamento: int, lucro_venda: float, db: Session = Depends(get_db)):
    nova_saida = Saida(
        id_codigo=id_codigo,
        quantidade=quantidade,
        valor_venda=valor_venda,
        forma_pagamento=forma_pagamento,
        lucro_venda=lucro_venda
    )
    db.add(nova_saida)
    db.commit()
    db.refresh(nova_saida)
    return nova_saida

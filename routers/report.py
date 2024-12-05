from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@router.get("/report")
def report():
    return "Relatório completo"
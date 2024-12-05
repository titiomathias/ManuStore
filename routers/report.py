from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@router.get("/")
def report():
    return "Relatório completo"
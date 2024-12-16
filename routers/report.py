from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

def get_data():
    return None

@router.get("/")
def report():
    return "Relatório completo"
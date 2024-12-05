from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@router.get("/")
def backup():
    return "Backup realiado na data atual"
from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@router.get("/backup")
def backup():
    return "Backup realiado na data atual"
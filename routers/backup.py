import os
from datetime import datetime
from fastapi import APIRouter, HTTPException

router = APIRouter()

# Configurações do banco de dados (ajuste conforme necessário)
DB_USER = "root"  # Substitua pelo usuário do banco de dados
DB_PASSWORD = ""  # Substitua pela senha do banco
DB_NAME = "manu_db"  # Substitua pelo nome do banco de dados
BACKUP_DIR = "./backups"  # Diretório onde os backups serão salvos

@router.get("/backup")
def realizar_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    backup_file = f"{BACKUP_DIR}/backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"

    command = f'C:\\xampp\\mysql\\bin\\mysqldump.exe -u {DB_USER} {DB_NAME} > "{backup_file}"'

    exit_code = os.system(command)

    if exit_code != 0:
        raise HTTPException(status_code=500, detail="Erro ao realizar o backup do banco de dados.")

    return {"message": "Backup realizado com sucesso.", "backup_file": backup_file}

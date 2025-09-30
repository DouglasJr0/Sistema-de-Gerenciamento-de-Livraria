import shutil
import os
from pathlib import Path
from datetime import datetime
from database import DB_PATH

BACKUP_DIR = Path("backups")
EXPORT_DIR = Path("exports")

def inicializar_diretorios():
    for d in [DB_PATH.parent, BACKUP_DIR, EXPORT_DIR]:
        d.mkdir(parents=True, exist_ok=True)

def fazer_backup():
    if DB_PATH.exists():
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        backup_file = BACKUP_DIR / f"backup_livraria_{timestamp}.db"
        shutil.copy(DB_PATH, backup_file)
        limpar_backups_antigos()

def limpar_backups_antigos(max_backups=5):
    backups = sorted(BACKUP_DIR.glob("backup_livraria_*.db"), key=os.path.getmtime, reverse=True)
    for old in backups[max_backups:]:
        old.unlink()

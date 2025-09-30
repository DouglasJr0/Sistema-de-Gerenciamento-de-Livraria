import shutil
from datetime import datetime
from pathlib import Path
from database import DB_PATH

BASE_DIR = Path(__file__).parent.resolve()
BACKUP_DIR = BASE_DIR / 'backups'
BACKUP_DIR.mkdir(exist_ok=True)

def fazer_backup():
    now = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    backup_path = BACKUP_DIR / f'backup_livraria_{now}.db'
    shutil.copy(DB_PATH, backup_path)
    limpar_backups_antigos()

def limpar_backups_antigos(max_backups=5):
    backups = sorted(BACKUP_DIR.glob("backup_livraria_*.db"), key=lambda x: x.stat().st_mtime, reverse=True)
    for backup in backups[max_backups:]:
        backup.unlink()

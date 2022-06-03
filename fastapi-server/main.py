from app import create_app
from pathlib import Path
import models
import sys

BASE_DIR = Path(__file__).resolve()
sys.path.append(str(BASE_DIR))
models.Base.metadata.create_all(bind=models.engine)

app = create_app()

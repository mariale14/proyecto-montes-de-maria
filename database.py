from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a la base de datos PostgreSQL (usa tu configuración real de Supabase)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres.vfcfbkkkhdaqatmjlxtr:cv9SPb0mpuKHdcrI@aws-0-us-east-1.pooler.supabase.com:6543/postgres"

# Crea una instancia del motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crea una fábrica de sesiones para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para definir modelos de SQLAlchemy
Base = declarative_base()

# Ejemplo de uso
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

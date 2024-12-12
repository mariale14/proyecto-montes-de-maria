from sqlalchemy import Column, Integer, String
from database import Base

# Modelo de SQLAlchemy para la tabla "users"
class User(Base):
    __tablename__ = "users"  # Nombre de la tabla en la base de datos

    # Columnas de la tabla "users"
    id = Column(Integer, primary_key=True, index=True)  # ID único de usuario, clave primaria
    username = Column(String, unique=True, index=True)  # Nombre de usuario único, con índice para búsquedas rápidas
    email = Column(String, unique=True, index=True)  # Correo electrónico único, con índice para búsquedas rápidas
    phone = Column(String, unique=True, index=True)  # Teléfono único, con índice para búsquedas rápidas
    password = Column(String)  # Contraseña del usuario

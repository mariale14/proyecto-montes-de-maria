from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import User
from schemas import UserCreate, UserResponse, LoginRequest

# Crea las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

# Inicializa la aplicación FastAPI
app = FastAPI()

# Configuración de los orígenes permitidos para CORS
origins = ['*']

# Agrega el middleware de CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite solicitudes desde cualquier origen
    allow_credentials=True,  # Permite el envío de cookies y credenciales
    allow_methods=['*'],     # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=['*']      # Permite todos los encabezados
)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    """
    Crea una sesión de base de datos y asegura su cierre al finalizar.
    """
    db = SessionLocal()
    try:
        yield db  # Devuelve la sesión de la base de datos
    finally:
        db.close()  # Cierra la sesión para liberar recursos

# Ruta para registrar un nuevo usuario
@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Registra un nuevo usuario en la base de datos.

    Args:
        user (UserCreate): Esquema con los datos del usuario a registrar.
        db (Session): Sesión de la base de datos.

    Returns:
        UserResponse: Información del usuario registrado.
    """
    # Verifica si el nombre de usuario ya está registrado
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Crea un nuevo usuario con los datos proporcionados
    new_user = User(
        username=user.username, 
        email=user.email, 
        phone=user.phone, 
        password=user.password
    )
    db.add(new_user)  # Agrega el usuario a la sesión de la base de datos
    db.commit()       # Guarda los cambios en la base de datos
    db.refresh(new_user)  # Actualiza el objeto con los datos almacenados

    # Devuelve la información del usuario registrado
    return UserResponse(
        id=new_user.id, 
        username=new_user.username, 
        email=new_user.email, 
        phone=new_user.phone
    )

# Ruta para iniciar sesión
@app.post("/login")
def login(user: LoginRequest, db: Session = Depends(get_db)):
    """
    Permite que un usuario inicie sesión.

    Args:
        user (LoginRequest): Esquema con las credenciales del usuario.
        db (Session): Sesión de la base de datos.

    Returns:
        dict: Mensaje de éxito si las credenciales son válidas.
    """
    # Busca al usuario en la base de datos usando su email y contraseña
    db_user = db.query(User).filter(User.email == user.email, User.password == user.password).first()
    if not db_user:
        # Lanza un error si las credenciales no son válidas
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Devuelve un mensaje de inicio de sesión exitoso
    return {"message": "Login successful"}

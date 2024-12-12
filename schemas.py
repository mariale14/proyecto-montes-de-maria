from pydantic import BaseModel

# Esquema para la creación de un nuevo usuario
class UserCreate(BaseModel):
    username: str  # Nombre de usuario
    email: str  # Correo electrónico
    phone: str  # Número de teléfono
    password: str  # Contraseña

# Esquema para la respuesta al registrar o consultar un usuario
class UserResponse(BaseModel):
    id: int  # ID del usuario
    username: str  # Nombre de usuario
    email: str  # Correo electrónico
    phone: str  # Número de teléfono

    class Config:
        from_attributes = True  # Permite mapear atributos desde un modelo de base de datos

# Esquema para las solicitudes de inicio de sesión
class LoginRequest(BaseModel):
    email: str  # Correo electrónico del usuario
    password: str  # Contraseña del usuario

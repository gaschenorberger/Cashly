from pydantic import BaseModel, EmailStr, Field, field_validator

class RegisterUser(BaseModel):
    nome: str = Field(min_length=2, max_length=120)
    email: EmailStr
    senha: str = Field(min_length=8)

    @field_validator("nome", mode="before")
    @classmethod
    def clean_name(cls, nome):
        return nome.strip() if isinstance(nome, str) else nome

    @field_validator("email", mode="before")
    @classmethod
    def clean_email(cls, email):
        return email.strip().lower() if isinstance(email, str) else email

    @field_validator("senha")
    @classmethod
    def validate_password(cls, senha):
        if len(senha.encode("utf-8")) > 72:
            raise ValueError("A senha deve ter no maximo 72 bytes")
        return senha

class LoginUser(BaseModel):
    email: EmailStr
    senha: str

    @field_validator("email", mode="before")
    @classmethod
    def clean_email(cls, email):
        return email.strip().lower() if isinstance(email, str) else email

    @field_validator("senha")
    @classmethod
    def validate_password(cls, senha):
        if len(senha.encode("utf-8")) > 72:
            raise ValueError("A senha deve ter no maximo 72 bytes")
        return senha
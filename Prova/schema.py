from pydantic import BaseModel, EmailStr
from typing import List, Optional

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    empresa_id: int

class ObrigacaoAcessoriaResponse(ObrigacaoAcessoriaBase):
    id: int
    empresa_id: int

    class Config:
        orm_mode = True

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: Optional[str]
    email: Optional[EmailStr]
    telefone: Optional[str]

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaResponse(EmpresaBase):
    id: int
    obrigacoes: List[ObrigacaoAcessoriaResponse] = []

    class Config:
        orm_mode = True

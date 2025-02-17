from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import modelos, schema
from BD import SessionLocal, engine

modelos.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/empresas/", response_model=schema.EmpresaResponse)
def criar_empresa(empresa: schema.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = modelos.Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

@app.get("/empresas/{empresa_id}", response_model=schema.EmpresaResponse)
def obter_empresa(empresa_id: int, db: Session = Depends(get_db)):
    empresa = db.query(modelos.Empresa).filter(modelos.Empresa.id == empresa_id).first()
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa

@app.post("/obrigacoes/", response_model=schema.ObrigacaoAcessoriaResponse)
def criar_obrigacao(obrigacao: schema.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = modelos.ObrigacaoAcessoria(**obrigacao.dict())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

@app.get("/docs")
def get_docs():
    return {"message": "Acesse a documentação em /docs"}

from fastapi.testclient import TestClient

import modelos
from BD import SessionLocal
from main import app

client = TestClient(app)


def test_obter_empresa():

    empresa = client.post("/empresas/", json={
        "nome": "Empresa Teste",
        "cnpj": "12345678000195",
        "endereco": "Rua A",
        "email": "teste@email.com",
        "telefone": "11999999999"
    }).json()

    empresa_id = empresa["id"]


    response = client.get(f"/empresas/{empresa_id}")
    assert response.status_code == 200

def setup_module():
    with SessionLocal() as db:
        db.query(modelos.Empresa).delete()
        db.commit()
import pytest
import sqlalchemy
from sqlalchemy.sql import text


@pytest.fixture
def conexao_db():
    engine = sqlalchemy.create_engine("sqlite:///:memory:")
    conexao = engine.connect()
    yield conexao
    conexao.close()

def test_conexao_db(conexao_db):
    resultado = conexao_db.execute(text("SELECT 1"))
    assert resultado.fetchone()[0] == 1



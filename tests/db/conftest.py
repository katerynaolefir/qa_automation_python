import pytest

from core.db.pq.db_client import DbClient


@pytest.fixture(scope="module")
def db():
    client = DbClient()
    yield client
    client.close()
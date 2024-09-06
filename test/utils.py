import pytest
from database import Base
from sqlalchemy import StaticPool, create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.testing import db
from fastapi.testclient import TestClient
import pytest
from main import app
from models import Todos, Users
from routers.user import bcrypt_context

SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {'username': 'Srivathsa', 'id': 1, 'user_role': 'admin'}


client = TestClient(app)


@pytest.fixture
def test_todo():
    todo = Todos(
        title='Learn to code',
        description='Need to learn everyday',
        priority=5,
        complete=False,
        owner_id=1,
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()


@pytest.fixture
def test_user():
    user = Users(
        username="Srivathsa",
        email="vathsa@gmail.com",
        first_name="vathsa",
        last_name="acharya",
        hashed_password=bcrypt_context.hash("v123"),
        role="admin"
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()

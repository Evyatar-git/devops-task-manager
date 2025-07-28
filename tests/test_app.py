import pytest
from app import create_app, db
from app.models import Task
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

@pytest.fixture
def app():
    app = create_app(TestConfig)
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'My Tasks' in response.data

def test_add_task(client):
    response = client.post('/add', data={
        'title': 'Test Task',
        'description': 'This is a test task'
    })
    assert response.status_code == 302  # Redirect after successful add
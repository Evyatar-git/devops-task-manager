import pytest
from app import create_app, db
from app.models import Task
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database for testing

@pytest.fixture
def app():
    """Create test app"""
    app = create_app(TestConfig)
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

def test_health_check(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b'healthy' in response.data

def test_index_page(client):
    """Test the main page loads"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'My Tasks' in response.data

def test_add_task(client):
    """Test adding a new task"""
    response = client.post('/add', data={
        'title': 'Test Task',
        'description': 'This is a test task'
    })
    assert response.status_code == 302  # Redirect after successful add
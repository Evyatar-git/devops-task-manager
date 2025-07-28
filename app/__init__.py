from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

# Create database instance (we'll initialize it later)
db = SQLAlchemy()

def create_app(config_class=DevelopmentConfig):
    """
    Application factory pattern - creates and configures the Flask app
    Why this pattern? Makes testing easier and allows multiple app instances
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize database with app
    db.init_app(app)
    
    # Register blueprints (routes)
    from app.routes import main
    app.register_blueprint(main)
    
    return app
from flask import Flask
from config import Config

# Initialize the Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Import routes at the bottom to avoid circular imports
from app import routes

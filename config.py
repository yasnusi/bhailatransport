import os
from dotenv import load_dotenv

# Load environment variables from a .env file (optional but recommended)
load_dotenv()

class Config:
    # Secret key for CSRF protection and sessions
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    
    # Optional: define the base directory
    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    # Optional future settings (database, email, etc.)
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
    #     "sqlite:///" + os.path.join(BASEDIR, "app.db")
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

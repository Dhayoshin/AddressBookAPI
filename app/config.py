import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database URL with fallback to SQLite
DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./addresses.db")
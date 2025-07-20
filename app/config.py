import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
load_dotenv()  

# --- Load env vars once ---
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))
MYSQL_USER = os.getenv('MYSQL_USER', 'root')

MYSQL_PASSWORD_RAW = os.getenv('MYSQL_PASSWORD')
MYSQL_PASSWORD = quote_plus(MYSQL_PASSWORD_RAW)  # encode @ etc.
MYSQL_DB = os.getenv('MYSQL_DB', 'task_manager')

MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class Config:
    # DB
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8mb4"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = MAIL_USERNAME
    MAIL_PASSWORD = MAIL_PASSWORD

    # AI
    OPENAI_API_KEY = OPENAI_API_KEY
    AI_MODEL = 'gpt-3.5-turbo'

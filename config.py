import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # application
    DEBUG = os.getenv('DEBUG', False)
    FLASK_HOST = os.getenv('FLASK_HOST', '127.0.0.1')
    FLASK_PORT = os.getenv('FLASK_PORT', '5000')

    # telegram bot
    TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
    TG_CHAT_ID = os.getenv('TG_CHAT_ID')

    # postgres
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_URL = rf'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

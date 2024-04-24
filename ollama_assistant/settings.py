import os

DEFAULT_API_URL = os.getenv('OLLAMA_API_URL', 'http://localhost:11434/api')
MONGO_URL = os.getenv('MONGO_URL', 'mongodb://localhost:27017')
DB_NAME = os.getenv('OLLAMA_DB_NAME', 'ollama')
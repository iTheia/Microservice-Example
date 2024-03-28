import os
from dotenv import load_dotenv

load_dotenv()

PEM_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'static', 'access-token-public.pem')
PUBLIC_KEY = ""
with open(PEM_FILE_PATH, 'rb') as f:
    PUBLIC_KEY = f.read()

DATABASE_URL = os.environ['DATABASE_URL']
AUTH_SERVICE = os.environ['AUTH_SERVICE']
PORT = os.environ['PORT']
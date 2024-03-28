from flask import Flask
from routes import setup_routes
from providers.database import Database
from providers.service import ServiceManager
from waitress import serve
from config.config import DATABASE_URL, AUTH_SERVICE, PORT
import alembic.config

def run_migrations():
    alembic.config.main(argv=['upgrade', 'head'])

def start_app ():
  app = Flask(__name__)

  database = Database()
  database.start(DATABASE_URL)
  service_manager = ServiceManager()

  service_manager.add_service('AUTH', AUTH_SERVICE)

  run_migrations()

  setup_routes(app)
  app.run(debug=True, host='0.0.0.0', port=PORT)

if __name__ == '__main__':
  start_app()

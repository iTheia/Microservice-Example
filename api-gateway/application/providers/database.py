from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def start(self, db_url):
        try:
            engine = create_engine(db_url)
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as e:
            print("Error occurred while creating session:", e)
            raise

    def get_session(self):
        return self.session


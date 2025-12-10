from sqlalchemy import create_engine

class DBService:
    def __init__(self, uri="sqlite:///zerokey.db"):
        self.engine = create_engine(uri)

    def connect(self):
        return self.engine.connect()

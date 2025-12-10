from zerokey.services.db_service import DBService

class UserService:
    def __init__(self):
        self.db = DBService()

    def create_user(self, username, password):
        conn = self.db.connect()
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.close()
        return {"created": True, "username": username}

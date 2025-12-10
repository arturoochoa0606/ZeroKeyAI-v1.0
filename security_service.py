from zerokey.utils.crypto import Crypto

class SecurityService:
    def __init__(self):
        self.crypto = Crypto()

    def secure_password(self, password):
        return self.crypto.encrypt(password)

    def verify_password(self, token):
        return self.crypto.decrypt(token)

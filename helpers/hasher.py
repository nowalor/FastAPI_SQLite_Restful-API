from passlib.context import CryptContext


class Hasher:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"])

    @staticmethod
    def verify_hash(self, plaintext_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plaintext_password, hashed_password)

    @staticmethod
    def generate_hash(password: str) -> str:
        return self.pwd_context(password)

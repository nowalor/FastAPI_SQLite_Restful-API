from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def verify_hash(plaintext_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plaintext_password, hashed_password)

    @staticmethod
    def generate_hash(password: str) -> str:
        return pwd_context.hash(password)

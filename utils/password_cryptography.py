from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

def decrypt_password(encrypted_password):
    SECRET_KEY = os.getenv("SECRET_KEY")
    cipher_suite = Fernet(SECRET_KEY)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode('utf-8')
    return decrypted_password

def encrypt_password(password):
    SECRET_KEY = os.getenv("SECRET_KEY")
    cipher_suite = Fernet(SECRET_KEY)
    encrypted_password = cipher_suite.encrypt(password.encode('utf-8'))
    return encrypted_password

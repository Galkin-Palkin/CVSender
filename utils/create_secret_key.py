from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Ваш секретный ключ для симметричного шифрования:\n{key}\nСохраните его в .env и никому не показывайте! Не забудьте добавить .env в .gitignore!")

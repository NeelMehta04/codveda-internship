from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("Level 3/secret.key", "wb") as f:
        f.write(key)

def load_key():
    return open("Level 3/secret.key", "rb").read()

def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, 'rb') as f:
        original = f.read()

    encrypted = fernet.encrypt(original)

    with open(f"{file_path}.enc", 'wb') as f:
        f.write(encrypted)
    print("File encrypted successfully.")

def decrypt_file(encrypted_path):
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_path, 'rb') as f:
        encrypted = f.read()

    decrypted = fernet.decrypt(encrypted)

    with open(f"{encrypted_path}.dec", 'wb') as f:
        f.write(decrypted)
    print("File decrypted successfully.")

generate_key()
encrypt_file("Level 3/example.txt")
decrypt_file("Level 3/example.txt.enc")
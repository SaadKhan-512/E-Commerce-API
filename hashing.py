import argon2

def hash_password(password: str):
    return argon2.hash_password(password)
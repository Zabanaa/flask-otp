import pyotp

def generate_secret_key():
    return pyotp.random_base32()

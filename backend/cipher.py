import base64

class Cipher:
    """ Cipher class to handle encryption and decryption of passwords that uses Base64 encoding """
    def encrypt(self, plaintext):
        if not plaintext:
            raise ValueError("Plaintext cannot be empty")
        plaintext_bytes = plaintext.encode("utf-8")
        encrypted_bytes = base64.b64encode(plaintext_bytes)
        return encrypted_bytes.decode("utf-8")

    def decrypt(self, encrypted_text):
        if not encrypted_text:
            raise ValueError("Encrypted text cannot be empty")
        encrypted_bytes = encrypted_text.encode("utf-8")
        plaintext_bytes = base64.b64decode(encrypted_bytes)
        return plaintext_bytes.decode("utf-8")

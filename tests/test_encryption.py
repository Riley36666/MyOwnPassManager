from src.encrypt import encrypt_pass, decryptPass  

def test_encrypt_then_decrypt_returns_original_password():
    original_password = "MyS3cretP@ssw0rd!"

    encrypted = encrypt_pass(original_password)
    decrypted = decryptPass(encrypted)

    assert decrypted == original_password

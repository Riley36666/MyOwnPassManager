
from unittest.mock import patch
from src.store_pass import storepass  


def test_storepass_valid_password_calls_encrypt_and_write():
    website = "example.com"
    password = "MySecret123"
    fake_encrypted = b"encrypted-bytes"

    with patch("src.store_pass.encrypt_pass", return_value=fake_encrypted) as mock_encrypt, \
         patch("src.store_pass.writePasstoFile") as mock_write:

        result = storepass(website, password)

        assert result is True
        mock_encrypt.assert_called_once_with(password)
        mock_write.assert_called_once_with(fake_encrypted, website)

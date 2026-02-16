# tests/test_delete.pypython -m pytest
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.deletingPass import deletePassFromFile

def test_deletePassFromFile_removes_correct_line(tmp_path):
    # Arrange: create temp password file with 3 entries
    test_file = tmp_path / "password.txt"
    content = [
        b"site1.com:encrypted1\n",
        b"site2.com:encrypted2\n",
        b"site3.com:encrypted3\n"
    ]
    test_file.write_bytes(b"".join(content))

    # Act: delete the second entry
    result = deletePassFromFile(2, file_path=str(test_file))

    # Assert
    assert result is True
    remaining_lines = test_file.read_bytes().split(b"\n")
    remaining_lines = [line for line in remaining_lines if line]  # remove empty lines

    assert remaining_lines == [b"site1.com:encrypted1", b"site3.com:encrypted3"]

def test_deletePassFromFile_invalid_index_returns_false(tmp_path):
    # Arrange: create empty file
    test_file = tmp_path / "password.txt"
    test_file.write_bytes(b"")

    # Act & Assert: index out of range
    result = deletePassFromFile(1, file_path=str(test_file))
    assert result is False

from src.file_handler import FileHandler
from src.manager import Manager
from src.text import Text
from unittest import mock


def test_manager_initialization():
    manager = Manager()
    assert isinstance(manager.file_handler, FileHandler)
    assert isinstance(manager.buffer, list)


def test_manager_start_encryption():
    mock_args = ["1", "rot_13", "hello", "test", "no", "0"]
    with mock.patch("builtins.input", side_effect=mock_args):
        manager = Manager()
        manager.start()
    assert len(manager.buffer) == 1
    assert manager.buffer[0].status == "encrypted"


def test_manager_start_decryption():
    mock_args = ["2", "rot_13", "uryyb", "test", "no", "0"]
    with mock.patch("builtins.input", side_effect=mock_args):
        manager = Manager()
        manager.start()
    assert len(manager.buffer) == 1
    assert manager.buffer[0].status == "decrypted"


    def test_manager_start_read_file(self):
        mock_args = ["1", "rot_13", "hello", "test", "yes", "0"]
        with mock.patch("builtins.input", side_effect=mock_args):
            manager = Manager()
            manager.file_handler.read_to_buffer = lambda filename: [
                {"text": "hello", "rot_type": "Rot13", "status": "encrypted"}
            ]
            manager.start()
        assert len(manager.buffer) == 2
        assert isinstance(manager.buffer[1], Text)
        assert manager.buffer[0]["status"] == "encrypted"


    def test_manager_start_write_file(self):
        mock_args = ["1", "rot_13", "hello", "test", "no", "0"]
        with mock.patch("builtins.input", side_effect=mock_args):
            manager = Manager()
            manager.file_handler.read_to_buffer = lambda filename: []
            manager.file_handler.write = lambda filename, data, read: None
            manager.start()
        assert len(manager.buffer) == 1
        assert isinstance(manager.buffer[0], Text)
        assert manager.buffer[0].status == "encrypted"

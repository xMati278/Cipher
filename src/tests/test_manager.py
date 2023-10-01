from app.manager import Manager
from app.text import Text
from unittest import mock
from app.buffer import Buffer


class TestManager:

    def test_manager_start_encryption(self):
        mock_args = ["1", "rot_13", "hello", "0"]
        with mock.patch("builtins.input", side_effect=mock_args):
            manager = Manager()
            manager.start()
        assert len(Buffer.data) == 3
        assert Buffer.data[0].status == "encrypted"

    def test_manager_start_decryption(self):
        mock_args = ["2", "rot_13", "uryyb", "0"]
        with mock.patch("builtins.input", side_effect=mock_args):
            manager = Manager()
            manager.start()
        assert len(Buffer.data) == 4
        assert Buffer.data[1].status == "decrypted"

    def test_manager_start_read_file(self):
        mock_args = ["1", "rot_13", "hello", "0"]
        with mock.patch("builtins.input", side_effect=mock_args):
            manager = Manager()
            manager.file_handler.read_to_buffer = lambda filename: [
                {"text": "hello", "rot_type": "Rot13", "status": "encrypted"}
            ]
            manager.start()
        assert len(Buffer.data) == 5
        assert isinstance(Buffer.data[1], Text)
        assert Buffer.data[2].status == "encrypted"

    def test_manager_start_write_file(self):
        mock_args = ["1", "rot_13", "hello", "0"]
        with mock.patch("builtins.input", side_effect=mock_args):
            manager = Manager()
            manager.file_handler.read_to_buffer = lambda filename: []
            manager.file_handler.write = lambda filename, data, read: None
            manager.start()
        assert len(Buffer.data) == 6
        assert isinstance(Buffer.data[0], Text)
        assert Buffer.data[3].status == "decrypted"

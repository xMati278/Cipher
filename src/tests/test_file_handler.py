import pytest
import json
import os
import tempfile
from src.file_handler import FileHandler


@pytest.mark.parametrize(
    "input_filename, expected_output",
    [
        ("example.json", "example.json"),
        ("example", "example.json"),
        ("example.txt", "example.txt.json"),
    ],
)
def test_validate_file_extension(input_filename, expected_output):
    validated_filename = FileHandler.validate_file_extension(input_filename)
    assert validated_filename == expected_output


@pytest.mark.parametrize(
    "data_to_write, expected_data",
    [
        (
            [
                {
                    "text_before": "abc",
                    "text_after": "def",
                    "rot_type": "Rot13",
                    "status": "encrypted",
                },
                {
                    "text_before": "xyz",
                    "text_after": "uvw",
                    "rot_type": "Rot13",
                    "status": "decrypted",
                },
            ],
            [
                {
                    "text_before": "abc",
                    "text_after": "def",
                    "rot_type": "Rot13",
                    "status": "encrypted",
                },
                {
                    "text_before": "xyz",
                    "text_after": "uvw",
                    "rot_type": "Rot13",
                    "status": "decrypted",
                },
            ],
        ),
    ],
)
def test_write_to_file(data_to_write, expected_data):
    with tempfile.TemporaryDirectory() as temp_dir:
        FileHandler().data_folder = temp_dir

        temp_file = os.path.join(temp_dir, "temp.json")
        FileHandler().write_to_file(temp_file, data_to_write)

        assert os.path.exists(temp_file)

        with open(temp_file, "r") as file:
            read_data = json.load(file)

        assert read_data == expected_data


@pytest.mark.parametrize(
    "data_to_write, read, expected_data",
    [
        (
            [
                {
                    "text_before": "abc",
                    "text_after": "def",
                    "rot_type": "Rot13",
                    "status": "encrypted",
                },
                {
                    "text_before": "xyz",
                    "text_after": "uvw",
                    "rot_type": "Rot13",
                    "status": "decrypted",
                },
            ],
            True,
            [
                {
                    "text_before": "abc",
                    "text_after": "def",
                    "rot_type": "Rot13",
                    "status": "encrypted",
                },
                {
                    "text_before": "xyz",
                    "text_after": "uvw",
                    "rot_type": "Rot13",
                    "status": "decrypted",
                },
            ],
        ),
    ],
)
def test_write(data_to_write, read, expected_data):
    with tempfile.TemporaryDirectory() as temp_dir:
        FileHandler().data_folder = temp_dir

        temp_file = os.path.join(temp_dir, "temp.json")

        os.makedirs(os.path.dirname(temp_file), exist_ok=True)

        if not read:
            FileHandler().write(filename=temp_file, data=data_to_write)
        else:
            FileHandler().write_to_file(filename=temp_file, data=data_to_write)

        with open(temp_file, "r") as file:
            read_data = json.load(file)

        assert read_data == expected_data

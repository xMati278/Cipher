import pytest
import os
from file_handler import FileHandler


@pytest.fixture
def cleanup_files():
    yield
    filenames = [
        "test_existing.json",
        "test_new.json",
        "test_extension.json",
        "test_no_extension.json",
        "nonexistent_file.json",
        "test_invalid_data.json",
    ]
    for filename in filenames:
        if os.path.exists(filename):
            os.remove(filename)


def test_write_and_read_existing_json_file(cleanup_files):
    filename = "test_existing.json"
    data = [{"name": "John", "age": 30}, {"name": "Alice", "age": 25}]
    FileHandler.write(filename, data)
    result = FileHandler.read(filename)
    assert result == data


def test_write_and_read_new_json_file(cleanup_files):
    filename = "test_new.json"
    data = [{"name": "Bob", "age": 35}, {"name": "Eve", "age": 28}]
    FileHandler.write(filename, data)
    result = FileHandler.read(filename)
    assert result == data


def test_write_with_extension(cleanup_files):
    filename = "test_extension.json"
    data = [{"name": "Charlie", "age": 40}]
    FileHandler.write(filename, data)
    assert os.path.exists(filename)


def test_write_without_extension(cleanup_files):
    filename = "test_no_extension"
    data = [{"name": "David", "age": 45}]
    FileHandler.write(filename, data)
    result = FileHandler.read(filename + ".json")
    assert result == data


def test_read_nonexistent_file(cleanup_files):
    filename = "nonexistent_file.json"
    result = FileHandler.read(filename)
    assert result == []


def test_write_with_invalid_data(cleanup_files):
    filename = "test_invalid_data.json"
    data = None
    with pytest.raises(ValueError):
        FileHandler.write(filename, data)

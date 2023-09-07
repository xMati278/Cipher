import os
import pytest
from file_handler import FileHandler
from src.buffer_dict import BufferDict
import json


@pytest.fixture
def test_file():

    filename = "test_file.json"
    with open(filename, "w") as file:
        json.dump([], file)
    yield filename
    os.remove(filename)



def test_write_valid_data(test_file):
    handler = FileHandler()
    data = [BufferDict(text_before="A", text_after="B")]
    handler.write(test_file, data)

    with open(test_file, "r") as file:
        content = json.load(file)

    assert content == BufferDict.to_dict_list(data)


def test_write_empty_data(test_file):
    handler = FileHandler()
    data = []
    handler.write(test_file, data)

    with open(test_file, "r") as file:
        content = json.load(file)

    assert content == []


def test_read_existing_file(test_file):
    handler = FileHandler()
    data = [BufferDict(text_before="X", text_after="Y")]
    with open(test_file, "w") as file:
        json.dump(BufferDict.to_dict_list(data), file)

    result = handler.read(test_file)
    assert result == data


def test_read_nonexistent_file():
    handler = FileHandler()
    filename = "nonexistent_file.json"
    result = handler.read(filename)
    assert result == []


def test_write_invalid_data(test_file):
    handler = FileHandler()
    data = None
    with pytest.raises(ValueError):
        handler.write(test_file, data)

from buffer_dict import BufferDict
import pytest


def test_to_dict():
    obj = BufferDict(text_before="Hello", text_after="World", rot_type="ROT13", status="Encrypted")
    expected_result = {
        'text_before': 'Hello',
        'text_after': 'World',
        'rot_type': 'ROT13',
        'status': 'Encrypted'
    }
    assert obj.to_dict() == expected_result


def test_to_object_list():
    dict_list = [
        {
            'text_before': 'Message 1',
            'text_after': 'Encrypted 1',
            'rot_type': 'ROT13',
            'status': 'Encrypted'
        },
        {
            'text_before': 'Message 2',
            'text_after': 'Encrypted 2',
            'rot_type': 'ROT47',
            'status': 'Encrypted'
        }
    ]
    object_list = BufferDict.to_object_list(dict_list)
    assert len(object_list) == 2
    assert object_list[0].text_before == 'Message 1'
    assert object_list[1].rot_type == 'ROT47'


def test_to_dict_list():
    object_list = [
        BufferDict(text_before="Hello", text_after="World", rot_type="ROT13", status="Encrypted"),
        BufferDict(text_before="Python", text_after="Rcgbaz", rot_type="ROT13", status="Encrypted")
    ]
    dict_list = BufferDict.to_dict_list(object_list)
    assert len(dict_list) == 2
    assert dict_list[1]['status'] == 'Encrypted'
    assert dict_list[0]['rot_type'] == 'ROT13'


def test_to_object_list_invalid_input(): #TODO not working
    invalid_input = [
        {'text_before': 'Message 1'},
        {'text_after': 'Encrypted 2'}
    ]
    with pytest.raises(TypeError) as excinfo:
        BufferDict.to_object_list(invalid_input)

    assert str(excinfo.value) == "Invalid input data for BufferDict"
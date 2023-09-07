from buffer_dict import BufferDict


def test_to_dict():
    buffer = BufferDict("Hello", "Uryyb", "ROT13", "Encoded")
    result = buffer.to_dict()
    assert result == {
        'text_before': "Hello",
        'text_after': "Uryyb",
        'rot_type': "ROT13",
        'status': "Encoded"
    }

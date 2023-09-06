import pytest

from rot import Rot13, Rot47


@pytest.fixture
def rot13_instance():
    return Rot13()


@pytest.fixture
def rot47_instance():
    return Rot47()


def test_rot13_encrypt_empty_message(rot13_instance):
    empty_message = ""
    with pytest.raises(ValueError) as e:
        rot13_instance.encrypt(empty_message)
    assert str(e.value) == "Empty string."


def test_rot47_encrypt_empty_message(rot47_instance):
    empty_message = ""
    with pytest.raises(ValueError) as e:
        rot47_instance.encrypt(empty_message)
    assert str(e.value) == "Empty string."


def test_rot13_decrypt_empty_message(rot13_instance):
    empty_message = ""
    with pytest.raises(ValueError) as e:
        rot13_instance.decrypt(empty_message)
    assert str(e.value) == "Empty string."


def test_rot47_decrypt_empty_message(rot47_instance):
    empty_message = ""
    with pytest.raises(ValueError) as e:
        rot47_instance.decrypt(empty_message)
    assert str(e.value) == "Empty string."


def test_rot13_encrypt_decrypt(rot13_instance):
    message = "Hello, World!"
    encrypted_message = rot13_instance.encrypt(message)
    decrypted_message = rot13_instance.decrypt(encrypted_message)
    assert decrypted_message == message


def test_rot47_encrypt_decrypt(rot47_instance):
    message = "Hello, World!"
    encrypted_message = rot47_instance.encrypt(message)
    decrypted_message = rot47_instance.decrypt(encrypted_message)
    assert decrypted_message == message


def test_rot13_encrypt_rot47_decrypt(rot13_instance, rot47_instance):
    message = "Hello, World!"
    encrypted_message_rot13 = rot13_instance.encrypt(message)
    decrypted_message_rot47 = rot47_instance.decrypt(encrypted_message_rot13)
    assert decrypted_message_rot47 != message


def test_rot47_encrypt_rot13_decrypt(rot13_instance, rot47_instance):
    message = "Hello, World!"
    encrypted_message_rot47 = rot47_instance.encrypt(message)
    decrypted_message_rot13 = rot13_instance.decrypt(encrypted_message_rot47)
    assert decrypted_message_rot13 != message


def test_rot13_invalid_characters(rot13_instance):
    message = "12345"
    encrypted_message = rot13_instance.encrypt(message)
    decrypted_message = rot13_instance.decrypt(encrypted_message)
    assert decrypted_message == message


def test_rot47_invalid_characters(rot47_instance):
    message = "!@#$%^"
    encrypted_message = rot47_instance.encrypt(message)
    decrypted_message = rot47_instance.decrypt(encrypted_message)
    assert decrypted_message == message

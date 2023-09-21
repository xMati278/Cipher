import pytest
from src.rot import Rot13, Rot47

@pytest.fixture
def rot13_instance():
    return Rot13()

@pytest.fixture
def rot47_instance():
    return Rot47()


class TestRot:
    def test_rot13_encrypt(self, rot13_instance):
        assert rot13_instance.encrypt("Hello, World!") == "Uryyb, Jbeyq!"
        assert rot13_instance.encrypt("abc") == "nop"
        assert rot13_instance.encrypt("123") == "123"

    def test_rot13_decrypt(self, rot13_instance):
        assert rot13_instance.decrypt("Uryyb, Jbeyq!") == "Hello, World!"
        assert rot13_instance.decrypt("nop") == "abc"
        assert rot13_instance.decrypt("123") == "123"

    def test_rot47_encrypt(self, rot47_instance):
        assert rot47_instance.encrypt("Hello, World!") == "w6==@[ (@C=5P"
        assert rot47_instance.encrypt("abc") == "234"
        assert rot47_instance.encrypt("123") == "`ab"

    def test_rot47_decrypt(self, rot47_instance):
        assert rot47_instance.decrypt("w6==@[ (@C=5P") == "Hello, World!"
        assert rot47_instance.decrypt("234") == "abc"
        assert rot47_instance.decrypt("`ab") == "123"

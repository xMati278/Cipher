import pytest
from menu import Menu


def test_app_info(capsys):
    menu = Menu()
    menu.app_info()
    captured = capsys.readouterr()
    expected_output = (
        "\nWelcome to Cipher App\n"
        "Available functionalities:\n"
        "1. Encrypt the message.\n"
        "2. Decrypt the message.\n"
        "0. Save and exit.\n"
    )
    assert captured.out == expected_output

@pytest.mark.parametrize("user_input, expected", [
    ("0\n", {'mode': 0}),
    ("1\n13\nHello\noutput.txt\nyes\n", {'mode': 1, 'shift': 13, 'message': 'Hello', 'filename': 'output.txt', 'read_file': True}),
    ("3\n", ValueError("You have entered an invalid value.")),
    ("2\n47\nWorld\ninput.txt\nno\n", {'mode': 2, 'shift': 47, 'message': 'World', 'filename': 'input.txt', 'read_file': False}),
    ("1\n47\n\noutput.txt\nyes\n", ValueError("No message entered.")),
    ("1\n47\nHello\n\nyes\n", ValueError("Filename not entered.")),
    ("invalid\n", ValueError("invalid literal for int() with base 10: 'invalid'")),
])
def test_get_user_choice(monkeypatch, user_input, expected):
    menu = Menu()
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    with pytest.raises(Exception) as excinfo:
        result = menu.get_user_choice()
    assert str(excinfo.value) == str(expected)

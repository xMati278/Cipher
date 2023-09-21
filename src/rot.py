from __future__ import annotations
from abc import ABC, abstractmethod


class Rot(ABC):
    @abstractmethod
    def encrypt(self, msg: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, msg: str):
        raise NotImplementedError

    @staticmethod
    def get_rot(rot_type: str) -> Rot13 | Rot47:
        """
        Selects the encryption/decryption type.

        :param rot_type: encryption/decryption type

        :return: encryption/decryption class of the appropriate type
        """

        if rot_type == 'rot_13':
            return Rot13()

        elif rot_type == 'rot_47':
            return Rot47()


class Rot13(Rot):
    def encrypt(self, msg: str) -> str:
        """
        Encrypts the message with ROT13.

        :param msg: message to be encrypted using ROT13

        :return: message encrypted using ROT13
        """

        if msg == "":
            raise ValueError("Empty string.")

        encrypted_text = ""
        for char in msg:
            if 'a' <= char <= 'z':
                shift = ord(char) - ord('a')
                encrypted_char = chr(((shift + 13) % 26) + ord('a'))
            elif 'A' <= char <= 'Z':
                shift = ord(char) - ord('A')
                encrypted_char = chr(((shift + 13) % 26) + ord('A'))
            else:
                encrypted_char = char
            encrypted_text += encrypted_char

        return encrypted_text

    def decrypt(self, msg: str) -> str:
        """
        Decrypts a message encrypted using ROT13.

        :param msg: ROT13 encrypted message to be decrypted

        :return: decrypted message using ROT13
        """

        if msg == "":
            raise ValueError("Empty string.")

        decrypted_text = ""

        for char in msg:
            if 'a' <= char <= 'z':
                shift = ord(char) - ord('a')
                decrypted_char = chr(((shift - 13) % 26) + ord('a'))

            elif 'A' <= char <= 'Z':
                shift = ord(char) - ord('A')
                decrypted_char = chr(((shift - 13) % 26) + ord('A'))

            else:
                decrypted_char = char

            decrypted_text += decrypted_char

        return decrypted_text


class Rot47(Rot):
    def encrypt(self, msg: str) -> str:
        """
        Encrypts the message with ROT47.

        :param msg: message to be encrypted using ROT47

        :return: message encrypted using ROT47
        """

        if msg == "":
            raise ValueError("Empty string.")

        encrypted_message_rot47 = ""
        for char in msg:
            char_code = ord(char)
            if 33 <= char_code <= 126:
                char_code -= 47
                if char_code < 33:
                    char_code += 94

            encrypted_message_rot47 += chr(char_code)

        return encrypted_message_rot47

    def decrypt(self, msg: str) -> str:
        """
        Decrypts a message encrypted using ROT47.

        :param msg: ROT47 encrypted message to be decrypted
        :return: decrypted message using ROT47
        """

        if msg == "":
            raise ValueError("Empty string.")

        decoded_message = ""

        for char in msg:
            char_code = ord(char)
            if 33 <= char_code <= 126:
                char_code += 47
                if char_code > 126:
                    char_code -= 94

            decoded_message += chr(char_code)

        return decoded_message

import json
import os
import codecs



class Cipher:
    def __init__(self):
        self.buffer = None
        self.filename = None
        self.mode = None
        self.message = None
        self.shift = None

    def start(self):
        """
        Starts the operation of the application based on ROT13 and ROT47 encryption.
        """

        while True:
            print("")
            print("Welcome to Cipher App")
            print("Available functionalities:")
            print("1. Encrypt the message.")
            print("2. Decrypt the message.")
            print("0. Save and exit.")

            try:
                self.mode = int(input("Choose what you want to do (enter a number):"))

                if self.mode == 0:
                    break

                if 0 < self.mode <= 2:
                    self.shift = int(input("Enter 13 if you want to use ROT13 encryption/ decryption or"
                                           " 47 if you want to use ROT47 encryption/ decryption:"))
                    self.message = str(input("Enter message to be encrypted/ decrypted:"))
                    self.filename = str(input("Enter the file name:"))
                    self.buffer = file_handler(mode="read", filename=self.filename)
                    self.menu(self.mode)

                else:
                    raise ValueError("You have entered an invalid value.")

            except ValueError as e:
                print(e)

    def menu(self, mode: int):
        """
        Supports the main menu of the application.

        :param mode: 1: ROT13, 2: ROT47, 3: Save and exit
        """

        try:
            if self.shift in [13, 47]:
                if mode == 1 and not self.message == "":
                    if self.shift == 13:
                        encrypted_message_rot13 = self.encrypt_message_rot13(msg=self.message)
                        buffer_dict = {"text_before": self.message, "text_after": encrypted_message_rot13,
                                       "rot_type": 'ROT13', "status": "encrypted"}

                    else:
                        encrypted_message_rot47 = self.encrypt_message_rot47(msg=self.message)
                        buffer_dict = {"text_before": self.message, "text_after": encrypted_message_rot47,
                                       "rot_type": 'ROT47', "status": "encrypted"}

                elif mode == 2 and not self.message == "":
                    if self.shift == 13:
                        decrypted_message_rot13 = self.decrypt_message_rot13(msg=self.message)
                        buffer_dict = {"text_before": self.message, "text_after": decrypted_message_rot13,
                                       "rot_type": 'ROT47', "status": "decrypted"}

                    else:
                        decrypted_message_rot47 = self.decrypt_message_rot47(msg=self.message)
                        buffer_dict = {"text_before": self.message, "text_after": decrypted_message_rot47,
                                       "rot_type": 'ROT47', "status": "decrypted"}

                else:
                    raise ValueError("You have entered an invalid message.")
                self.buffer.append(buffer_dict)
                file_handler(mode="write", filename=self.filename, data=self.buffer)

            else:
                raise ValueError("You have entered an incorrect value.")

        except ValueError as e:
            if "invalid literal for int()" in str(e):
                print("You have entered a non-integer value for shift.")

            else:
                print(e)

    @staticmethod
    def encrypt_message_rot13(msg: str) -> bytes:
        """
        Encrypts the message with ROT13.

        :param msg: message to be encrypted using ROT13
        :return: message encrypted using ROT13
        """

        return codecs.encode(msg, "rot13")

    @staticmethod
    def encrypt_message_rot47(msg: str) -> str:
        """
        Encrypts the message with ROT47.

        :param msg: message to be encrypted using ROT47
        :return: message encrypted using ROT47
        """

        encrypted_message_rot47 = ""
        for char in msg:
            char_code = ord(char)
            if 33 <= char_code <= 126:
                char_code -= 47
                if char_code < 33:
                    char_code += 94
            encrypted_message_rot47 += chr(char_code)
        return encrypted_message_rot47

    @staticmethod
    def decrypt_message_rot13(msg: bytes) -> str:
        """
        Decrypts a message encrypted using ROT13.

        :param msg: ROT13 encrypted message to be decrypted
        :return: decrypted message using ROT13
        """

        return codecs.decode(msg, "rot13")

    @staticmethod
    def decrypt_message_rot47(msg: str) -> str:
        """
        Decrypts a message encrypted using ROT47.

        :param msg: ROT47 encrypted message to be decrypted
        :return: decrypted message using ROT47
        """

        decoded_message = ""
        for char in msg:
            char_code = ord(char)
            if 33 <= char_code <= 126:
                char_code += 47
                if char_code > 126:
                    char_code -= 94
            decoded_message += chr(char_code)
        return decoded_message


if __name__ == '__main__':
    cipher_app = Cipher()
    cipher_app.start()

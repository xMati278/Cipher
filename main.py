import json
import os


def file_handler(mode: str, filename: str, data: list = None) -> list:
    if mode not in ["read", "write"]:
        raise ValueError("Mode must be 'read' or 'write'")

    if not filename.endswith(".json"):
        filename += ".json"

    try:
        if mode == "read":
            if not os.path.exists(filename):
                with open(filename, "w") as file:
                    json.dump([], file)
                return []

            with open(filename, "r") as file:
                try:
                    cipher_list = json.load(file)

                except json.JSONDecodeError:
                    cipher_list = []

                return cipher_list

        elif mode == "write":
            if data is None:
                raise ValueError("Data must be provided in 'write' mode")

            with open(filename, "w") as file:
                print(data)
                json.dump(data, file, indent=4)

    except Exception as e:
        print(e)

class Cipher:

    def __init__(self):
        self.buffer = None
        self.running = True
        self.filename = None
        self.mode = None
        self.message = None
        self.shift = None

    def start(self):

        while self.running:
            print("")
            print("Welcome to Cipher App")
            print("Available functionalities:")
            print("1. Encrypt the message.")
            print("2. Decrypt the message.")
            print("0. Save and exit.")

            try:
                self.mode = int(input("Choose what you want to do (enter a number):"))

                if 0 <= self.mode <= 2:
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
        if mode == 1 or mode == 2:
            try:
                if self.shift in [13, 47]:
                    if mode == 1 and not self.message == "":
                        self.encrypt_message(msg=self.message, shift=self.shift)

                    elif mode == 2 and not self.message == "":
                        self.decrypt_message(msg=self.message, shift=self.shift)

                    else:
                        raise ValueError("You have entered an invalid message.")
                else:
                    raise ValueError("You have entered an incorrect value.")

            except ValueError as e:
                if "invalid literal for int()" in str(e):
                    print("You have entered a non-integer value for shift.")

                else:
                    print(e)

        else:
            self.running = False

    def encrypt_message(self, msg: str, shift: int):
        encrypted_message = ""

        for char in msg:
            if 33 <= ord(char) <= 126:
                shifted = ord(char) + shift

                if shifted > 126:
                    shifted -= 94

                encrypted_message += chr(shifted)

            else:
                encrypted_message += char

        buffer_dict = {"text_before": msg, "rot_type": f'ROT{shift}',
                       "text_after": encrypted_message, "status": "encrypted"}

        self.buffer.append(buffer_dict)
        file_handler(mode="write", filename=self.filename, data=self.buffer)

    def decrypt_message(self, msg: str, shift: int):
        decrypted_message = ""

        for char in msg:
            if 33 <= ord(char) <= 126:
                shifted = ord(char) - shift
                if shifted < 33:
                    shifted += 94

                decrypted_message += chr(shifted)

            else:
                decrypted_message -= char

        buffer_dict = {"text_before": msg, "rot_type": f'ROT{shift}',
                       "text_after": decrypted_message, "status": "decrypted"}

        self.buffer.append(buffer_dict)
        file_handler(mode="write", filename=self.filename, data=self.buffer)


if __name__ == '__main__':
    cipher_app = Cipher()
    cipher_app.start()

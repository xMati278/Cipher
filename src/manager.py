from src.menu import Menu
from src.buffer import Buffer
from src.text import Text
from src.file_handler import FileHandler
from src.rot import Rot


class Manager:
    def __init__(self):
        self.file_handler = FileHandler()
        self.buffer = []

    def start(self):
        """
        Start Manager method
        """

        while True:
            choice = Menu.get_user_choice()

            if choice["mode"] == 0:
                break

            if choice["mode"] in [1, 2]:
                self.process_choice(choice)

            print(f"Current buffer: {self.buffer}")

    def process_choice(self, choice):
        mode, shift, message, filename, read_file = choice.values()

        rot_version = Rot.get_rot(shift)

        if read_file:
            self.buffer = self.file_handler.read(filename=filename)

        if mode == 1:
            self.encrypt_message(rot_version, message, filename, read_file)
        else:
            self.decrypt_message(rot_version, message, filename, read_file)

    def encrypt_message(self, rot_version, message, filename, read_file):
        status = "encrypted"
        encrypted_msg = rot_version.encrypt(msg=message)
        self.update_buffer_and_write(
            encrypted_msg, rot_version, status, filename, read_file
        )

    def decrypt_message(self, rot_version, message, filename, read_file):
        status = "decrypted"
        decrypted_msg = rot_version.decrypt(msg=message)
        self.update_buffer_and_write(
            decrypted_msg, rot_version, status, filename, read_file
        )

    def update_buffer_and_write(
        self, message, rot_version, status, filename, read_file
    ):
        text = Text(
            text=message, rot_type=rot_version.__class__.__name__, status=status
        )

        self.buffer.append(text)
        data_to_write = Buffer().to_dict_list(self.buffer)
        self.file_handler.write(filename=filename, data=data_to_write, read=read_file)

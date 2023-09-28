from src.menu import Menu
from src.buffer import Buffer
from src.text import Text
from src.file_handler import FileHandler
from src.rot import Rot


class Manager:
    def __init__(self):
        self.file_handler = FileHandler()

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

            if choice["mode"] == 3:
                Buffer.data = self.load_json_file()

            if choice["mode"] == 4:
                self.save_to_json_file()

            print(f"Current buffer: {Buffer.data}")

    def process_choice(self, choice: dict[str, ...]) -> None:
        """
        processes and decides what the application should do

        :param choice: dictionary with choices
        """

        mode, shift, message = choice.values()

        rot_version = Rot.get_rot(shift)

        if mode == 1:
            self.encrypt_message(rot_version, message)
        else:
            self.decrypt_message(rot_version, message)

    def encrypt_message(self, rot_version: Rot, message: str) -> None:
        """
        process encryption functionality

        :param rot_version: Rot object
        :param message: message to be encrypted
        """

        status = "encrypted"
        encrypted_msg = rot_version.encrypt(msg=message)
        new_text_object = self.create_text_object(
            message=encrypted_msg, status=status, rot_version=rot_version
        )
        Buffer.data.append(new_text_object)

    def decrypt_message(self, rot_version: Rot, message: str) -> None:
        """
        process decryption fonctionality

        :param rot_version: Rot object
        :param message: message to be decrypted
        """

        status = "decrypted"
        decrypted_msg = rot_version.decrypt(msg=message)
        new_text_object = self.create_text_object(
            message=decrypted_msg, status=status, rot_version=rot_version
        )
        Buffer.data.append(new_text_object)

    def load_json_file(self) -> list:
        """
        load data from json file

        :return: list of objects to save in buffer from file
        """

        filename = Menu().get_filename()
        data_to_load = self.file_handler.read_to_buffer(filename=filename)
        return data_to_load

    def save_to_json_file(self) -> None:
        """
        save data from buffer to json file
        """

        filename = Menu().get_filename()
        self.file_handler.write(filename=filename, data=Buffer.data)

    @staticmethod
    def create_text_object(message: str, rot_version: Rot, status: str) -> Text:
        """
        create text object

        :param message: message
        :param rot_version: Rot object
        :param status: status (encrypted/ decrypted)

        :return: Text object
        """

        text = Text(
            text=message, rot_type=rot_version.__class__.__name__, status=status
        )
        return text

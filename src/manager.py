from src.menu import Menu
from src.buffer import Buffer
from src.text import Text
from src.file_handler import FileHandler
from src.rot import Rot


class Manager:
    def __init__(self):
        self.menu = Menu()
        self.file_handler = FileHandler()

        self.buffer = []

    def start(self):
        """
        Start Manager method
        """

        while True:
            menu = Menu()
            choice = menu.get_user_choice()

            if choice['mode'] == 0:
                break

            if choice['mode'] in [1, 2]:

                mode = choice['mode']
                shift = choice['shift']
                message = choice['message']
                filename = choice['filename']
                read_file = choice['read_file']

                rot_version = Rot.get_rot(shift)

                if read_file:
                    self.buffer = self.file_handler.read(filename=filename)

                if mode == 1:
                    status = 'encrpyted'
                    msg = rot_version.encrypt(msg=message)

                else:
                    status = 'decrypted'
                    msg = rot_version.decrypt(msg=message)

                msg_dict = Text(text_before=message, text_after=msg,
                                rot_type=rot_version.__class__.__name__, status=status)

                self.buffer.append(msg_dict)
                data_to_write = Buffer().to_dict_list(self.buffer)
                self.file_handler.write(filename=filename, data=data_to_write, read=read_file)

            print(f'Current buffer: {self.buffer}')

from src.menu import Menu
from src.buffer_dict import BufferDict
from src.file_handler import FileHandler
from src.rot import Rot13, Rot47


class Manager:
    def __init__(self):
        self.menu = Menu()
        self.buffer_dict = BufferDict()
        self.file_handler = FileHandler()
        self.rot13 = Rot13()
        self.rot47 = Rot47()

        self.buffer = []

        self.mode = None
        self.shift = None
        self.message = None
        self.filename = None
        self.read_file = None

    def start(self):
        """
        Start Manager method
        """

        while True:
            menu = Menu()
            menu.app_info()
            choice = menu.get_user_choice()

            if choice['mode'] == 0:
                break

            if choice['mode'] in [1, 2]:

                self.mode = choice['mode']
                self.shift = choice['shift']
                self.message = choice['message']
                self.filename = choice['filename']
                self.read_file = choice['read_file']

                if self.read_file:
                    self.buffer = self.file_handler.read(filename=self.filename)

                if self.mode == 1:
                    status = 'encrpyted'
                    if self.shift == 13:
                        rot = "ROT13"
                        msg = self.rot13.encrypt(msg=self.message)
                    else:
                        rot = "ROT47"
                        msg = self.rot47.encrypt(msg=self.message)

                else:
                    status = 'decrypted'
                    if self.shift == 13:
                        rot = "ROT13"
                        msg = self.rot13.decrypt(msg=self.message)
                    else:
                        rot = "ROT47"
                        msg = self.rot47.decrypt(msg=self.message)

                msg_dict = BufferDict(text_before=self.message, text_after=msg, rot_type=rot, status=status)
                self.buffer.append(msg_dict)
                self.file_handler.write(filename=self.filename, data=self.buffer)

            print(f'Current buffer: {self.buffer}')


if __name__ == '__main__':
    manager = Manager()
    manager.start()

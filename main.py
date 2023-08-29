import time

class Cipher:

    def __init__(self):
        self.buffer = {}
        self.running = True
        self.sleep_time = 5

    def start(self):

        while self.running:
            print("")
            print("Welcome to Cipher App")
            print("Available functionalities:")
            print("1. Encrypt the message.")
            print("2. Decrypt the message.")
            print("0. Save and exit.")

            try:
                mode = int(input("Choose what you want to do (enter a number):"))

                if 0 <= mode <= 2:
                    self.menu(mode)
                else:
                    raise ValueError("You have entered an invalid value.")

            except ValueError as e:
                print(e)
                time.sleep(self.sleep_time)

    def menu(self, mode: int):
        if mode == 1 or mode == 2:
            try:
                shift = int(input("Enter 13 if you want to use ROT13 encryption or"
                                  " 47 if you want to use ROT47 encryption:"))
                message = str(input("Enter message to be encrypted/ decrypted:"))
                if shift == 13 or shift == 47:
                    if mode == 1 and not message == "":
                        print(self.encrypt_message(msg=message, shift=shift))

                    elif mode == 2 and not message == "":
                        print(self.decrypt_message(msg=message, shift=shift))
                    else:
                        raise ValueError("You have entered an invalid message.")
                else:
                    raise ValueError("You have entered an incorrect value")
            except ValueError as e:
                if "invalid literal for int()" in str(e):
                    print("You have entered a non-integer value for shift.")
                else:
                    print(e)
                time.sleep(self.sleep_time)

        elif mode == 0:
            self.running = False

    def encrypt_message(self, msg: str, shift: int) -> str:
        encrypted_message = ""
        for char in msg:
            if 33 <= ord(char) <= 126:
                shifted = ord(char) + shift
                if shifted > 126:
                    shifted -= 94
                encrypted_message += chr(shifted)
            else:
                encrypted_message += char
        return encrypted_message


    def decrypt_message(self, msg, shift: int):
        return self.encrypt_message(msg, -shift)


if __name__ == '__main__':
    cipher_app = Cipher()
    cipher_app.start()


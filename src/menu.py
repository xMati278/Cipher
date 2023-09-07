class Menu:
    def __init__(self):
        self.mode = None
        self.shift = None
        self.message = None
        self.filename = None
        self.read_file = True
        self.continue_loop = True

    @staticmethod
    def app_info():
        """
        Print infos about app
        """

        print("")
        print("Welcome to Cipher App")
        print("Available functionalities:")
        print("1. Encrypt the message.")
        print("2. Decrypt the message.")
        print("0. Save and exit.")

    def get_user_choice(self) -> dict[str, ...]:
        """
        Specifies what the user wants.
        """
        try:
            self.mode = int(input("Choose what you want to do (enter a number):"))

            if self.mode == 0:
                return {'mode': self.mode}

            if 0 < self.mode <= 2:
                self.shift = int(input("Enter 13 if you want to use ROT13 encryption/ decryption or"
                                       " 47 if you want to use ROT47 encryption/ decryption:"))
                if self.shift not in [13, 47]:
                    raise ValueError("the application has no such encryption method")

                self.message = str(input("Enter message to be encrypted/ decrypted:"))
                if self.message == "":
                    raise ValueError("No message entered.")

                self.filename = str(input("Enter the file name:"))
                if self.filename == "":
                    raise ValueError("Filename not entered.")

                read_file_choice = str(input("Do you want to read data from file type yes or no? (if exist)"))
                self.read_file = True if read_file_choice == "yes" else False

            else:
                raise ValueError("You have entered an invalid value.")

            return {'mode': self.mode, 'shift': self.shift, 'message': self.message,
                    'filename': self.filename, 'read_file': self.read_file}

        except ValueError as e:
            print(e)

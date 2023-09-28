from logs.logging_config import logger


class Menu:

    @staticmethod
    def get_user_choice() -> dict[str, ...]:
        """
        Specifies what the user wants.
        """

        Menu.main_menu()
        mode = Menu.get_app_mode()

        if mode in [0, 3, 4]:
            return {'mode': mode}

        if 0 < mode <= 2:
            return Menu.get_user_input_for_mode(mode)

    @staticmethod
    def get_user_input_for_mode(mode: int) -> dict[str, ...]:
        shift = Menu.select_rot()
        message = Menu.get_message()

        return {
            'mode': mode,
            'shift': shift,
            'message': message,
        }

    @staticmethod
    def main_menu():
        """
        Print infos about app
        """

        print("")
        print("Welcome to Cipher App")
        print("Available functionalities:")
        print("1. Encrypt the message.")
        print("2. Decrypt the message.")
        print("3. Load data from JSON file.")
        print("4. Save Buffer to JSON file")
        print("0. Save and exit.")

    @staticmethod
    def select_rot() -> str:
        """
        Gets the type of encryption/decryption from the user.

        :return: type of encryption/decryption as string
        """

        try:
            shift = str(input("Enter rot_13 if you want to use ROT13 encryption/ decryption or"
                              " rot_47 if you want to use ROT47 encryption/ decryption:"))

            if shift not in ["rot_13", "rot_47"]:
                raise ValueError("You have entered an invalid value for the ROT encryption/decryption selection.")

            return shift

        except ValueError as e:
            logger.error(f'src.menu.select_rot Error: {e}')

    @staticmethod
    def get_message() -> str:
        """
        Gets the message for encryption/decryption from the user.

        :return: message for encryption/decryption as string
        """

        try:
            message = str(input("Enter message to be encrypted/ decrypted:"))
            if message == "":
                raise ValueError("No message entered.")

            return message

        except ValueError as e:
            logger.error(f'src.menu.get_message Error: {e}')

    @staticmethod
    def get_filename() -> str:
        """
        Gets the file name from the user.

        :return: file name as string
        """

        try:
            filename = str(input("Enter the file name:"))

            if filename == "":
                raise ValueError("Filename not entered.")

            return filename

        except ValueError as e:
            logger.error(f'src.menu.get_filename Error: {e}')

    @staticmethod
    def get_app_mode() -> int:
        """
        Gets the user's choice of application functionality.

        :return: application functionality mode as int
        """

        try:
            mode = int(input("Choose what you want to do (enter a number):"))
            if mode in [0, 1, 2, 3, 4]:
                return mode
            else:
                raise ValueError("You have not selected the correct application functionality.")

        except ValueError as e:
            logger.error(f'src.menu.get_app_mode Error: {e}')

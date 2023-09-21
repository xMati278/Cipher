import json
import os
from src.buffer import Buffer


class FileHandler:
    def __init__(self):
        self.buffer_operation = Buffer()
        self.data_folder = "..//json_files"

    @staticmethod
    def validate_file_extension(filename: str) -> str:
        """
        Validates the filename format.

        :param filename: filename to validate

        :return: filename in the correct format
        """

        if not filename.endswith(".json"):
            filename += ".json"

        return filename

    def write_to_file(self, filename: str, data: list) -> None:
        """
        Writes data to a JSON file.

        :param filename: file name in JSON format
        :param data: data to be written to a file
        """

        file_path = os.path.join(self.data_folder, filename)

        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def write(self, filename: str, data: list, read: bool):
        """
        Checks the correctness of the data to be saved and calls the save function.

        :param filename: file name in JSON format
        :param data: data to be written to a file
        :param read: information whether data was downloaded from the file
        """

        try:
            if data is None:
                raise ValueError("Data should not be None.")
            filename = self.validate_file_extension(filename=filename)

            if not os.path.exists(filename):
                self.write_to_file(filename, [])

            if not read:
                data_to_save = self.read(filename=filename)
                data_to_save = self.buffer_operation.to_dict_list(obj_list=data_to_save)
                data_to_save += data
                self.write_to_file(filename, data_to_save)
            else:
                self.write_to_file(filename, data)

        except (FileNotFoundError, ValueError) as e:
            print(f"src.file_handler.write Error: {e}")

    def read(self, filename: str) -> list:
        """
        The method reads data from the file "filename" and returns it

        :param filename: "example" or "example.JSON" - filename or filename with extension .JSON

        :return: a list of dictionaries based on the given file
        """

        try:
            filename = self.validate_file_extension(filename=filename)
            file_path = os.path.join(self.data_folder, filename)

            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File: {filename} not found.")

            with open(file_path, "r") as file:
                try:
                    cipher_list = json.load(file)

                except json.JSONDecodeError:
                    cipher_list = []
                    return cipher_list

                valid_list = self.buffer_operation.to_object_list(dict_list=cipher_list)
                return valid_list

        except FileNotFoundError as e:
            print(f"src.file_handler.read Error: {e}")

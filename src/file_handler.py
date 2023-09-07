import json
import os
from src.buffer_dict import BufferDict


class FileHandler:

    def write(self, filename: str, data: list) -> list:
        """
        The method writes data from the "data" parameter to a file named "filename"

        :param filename: "example" or "example.JSON" - filename or filename with extension .JSON
        :param data: parameter for saving data
        """

        if data is None:
            raise ValueError

        try:
            if not filename.endswith(".json"):
                filename += ".json"
                data = BufferDict.to_dict_list(data)
                print(data)

            with open(filename, "w") as file:
                json.dump(data, file, indent=4)

            return data

        except Exception as e:
            print(e)

    @staticmethod
    def read(filename: str) -> list:
        """
        The method reads data from the file "filename" and returns it

        :param filename: "example" or "example.JSON" - filename or filename with extension .JSON
        :return: a list of dictionaries based on the given file
        """

        try:
            if not filename.endswith(".json"):
                filename += ".json"

            if not os.path.exists(filename):
                with open(filename, "w") as file:
                    json.dump([], file)
                return []

            with open(filename, "r") as file:
                try:
                    cipher_list = json.load(file)
                    cipher_list = BufferDict.to_object_list(cipher_list)

                except json.JSONDecodeError:
                    cipher_list = []

                return cipher_list
        except Exception as e:
            print(e)

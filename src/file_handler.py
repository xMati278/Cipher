import json
import os


class FileHandler:

    @staticmethod
    def write(filename: str, data: list):
        """
        :param filename: "example" or "example.JSON" - filename or filename with extension .JSON
        :param data: parameter for saving data
        """

        if data is None:
            raise ValueError

        try:
            if not filename.endswith(".json"):
                filename += ".json"

            if data is None:
                raise ValueError

            with open(filename, "w") as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            print(e)

    @staticmethod
    def read(filename: str) -> list:
        """
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

                except json.JSONDecodeError:
                    cipher_list = []

                return cipher_list
        except Exception as e:
            print(e)

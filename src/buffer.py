from typing import Any, List
from dataclasses import asdict
from text import Text


class Buffer:
    def __init__(self):
        self.buffer_list: List[Text] = []

    def to_object_list(self, dict_list: list) -> None:
        """
        Converts a list of dictionaries to a list of objects.

        :param dict_list: list of dictionaries to convert
        """

        object_list = []
        for item in dict_list:
            try:
                obj = Text(**item)
                object_list.append(obj)

            except TypeError as e:
                raise TypeError("Invalid input data for BufferDict") from e

            self.buffer_list.extend(object_list)

    def to_dict_list(self) -> list[dict[str, Any]]:
        """
        converts a list of objects into a list of dictionaries
        """

        return [asdict(obj) for obj in self.buffer_list]


from typing import Any, List
from dataclasses import asdict
from src.text import Text


class Buffer:

    @staticmethod
    def to_object_list(dict_list: list) -> List[dict[str: Any]]:
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

        return object_list

    @staticmethod
    def to_dict_list(obj_list) -> list[dict[str, Any]]:
        """
        converts a list of objects into a list of dictionaries

        :param obj_list: list of objects to convert
        """
        if obj_list is None:
            return []

        dict_list = []
        for obj in obj_list:
            if isinstance(obj, dict):
                dict_list.append(obj)

            elif hasattr(obj, '__dict__'):
                dict_list.append(asdict(obj))

            else:
                raise ValueError(f"Unsupported object type: {type(obj)}")

        return dict_list

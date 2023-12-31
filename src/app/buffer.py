from typing import Any, List, Dict
from dataclasses import asdict

from logs.logging_config import logger
from .text import Text

class Buffer:
    data = []

    @staticmethod
    def add(text: Text) -> None:
        """
        Add Text object to Buffer

        :param text: Text object
        """

        Buffer.data.append(text)

    @staticmethod
    def to_object_list(dict_list: List[Dict[str, Any]]) -> List[Text]:
        """
        Converts a list of dictionaries to a list of objects.

        :param dict_list: list of dictionaries to convert
        """

        try:
            object_list = [Text(**item) for item in dict_list]
        except TypeError as e:
            logger.error(e)
            raise TypeError("Invalid input data for BufferDict") from e

        return object_list

    @staticmethod
    def to_dict_list() -> List[Dict[str, Any]]:
        """
        converts a list of objects into a list of dictionaries

        :return: list od dictionaries
        """

        if Buffer.data is None:
            return []

        dict_list = []
        try:
            for obj in Buffer.data:
                if isinstance(obj, dict):
                    dict_list.append(obj)

                elif hasattr(obj, '__dict__'):
                    dict_list.append(asdict(obj))

                else:
                    raise ValueError(f"Unsupported object type: {type(obj)}")

        except ValueError as e:
            logger.error(f'src.buffer.to_dict_list: {e}')

        return dict_list

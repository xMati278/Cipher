from dataclasses import dataclass


@dataclass
class BufferDict:
    text_before: str = ""
    text_after: str = ""
    rot_type: str = ""
    status: str = ""

    def to_dict(self):
        return {
            'text_before': self.text_before,
            'text_after': self.text_after,
            'rot_type': self.rot_type,
            'status': self.status
        }

    @classmethod
    def to_object_list(cls, dict_list) -> list:
        """
        converts a list of dictionaries to a list of objects
        :param dict_list: list of dictionaries to convert
        :return: list of objects
        """

        object_list = []
        for item in dict_list:
            try:
                obj = cls(**item)
                object_list.append(obj)
            except TypeError as e:
                raise TypeError("Invalid input data for BufferDict") from e
        return object_list

    @classmethod
    def to_dict_list(cls, object_list) -> list:
        """
        converts a list of objects into a list of dictionaries
        :param object_list: list of objects to convert
        :return: list of dictionaries
        """
        dict_list = []
        for obj in object_list:
            dict_list.append(obj.to_dict())
        return dict_list

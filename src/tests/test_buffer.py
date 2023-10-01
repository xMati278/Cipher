from app.buffer import Buffer
from app.text import Text


class TestBuffer:

    def test_to_object_list(self):
        dict_list = [
            {"text": "abc", "rot_type": "Rot13", "status": "encrypted"},
            {"text": "xyz", "rot_type": "Rot13", "status": "decrypted"},
        ]

        obj_list = Buffer.to_object_list(dict_list)

        assert len(obj_list) == 2
        assert obj_list[0].text == "abc"
        assert obj_list[1].text == "xyz"
        assert obj_list[1].rot_type == "Rot13"

    def test_to_dict_list(self):
        obj_list = [
            Text(text="abc", rot_type="Rot13", status="encrypted"),
            Text(text="xyz", rot_type="Rot13", status="decrypted"),
        ]
        for i in obj_list:
            Buffer.add(i)

        dict_list = Buffer.to_dict_list()

        assert len(dict_list) == 2
        assert dict_list[0]["text"] == "abc"
        assert dict_list[1]["status"] == "decrypted"


if __name__ == "__main__":
    pytest.main()

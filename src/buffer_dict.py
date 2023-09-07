from dataclasses import dataclass


@dataclass
class BufferDict:
    text_before: str
    text_after: str
    rot_type: str
    status: str

    def to_dict(self):
        return {
            'text_before': self.text_before,
            'text_after': self.text_after,
            'rot_type': self.rot_type,
            'status': self.status
        }

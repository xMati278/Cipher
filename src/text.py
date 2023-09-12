from dataclasses import dataclass


@dataclass
class Text:
    text_before: str
    text_after: str
    rot_type: str
    status: str

from dataclasses import dataclass


@dataclass
class Note:
    note_id: str
    owner_id: str
    text: str

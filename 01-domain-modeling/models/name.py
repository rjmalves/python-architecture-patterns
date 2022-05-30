from dataclasses import dataclass
from typing import NamedTuple


@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str

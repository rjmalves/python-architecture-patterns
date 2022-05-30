import pytest

from models.name import Name
from models.person import Person


def test_name_equality():
    assert Name("Harry", "Percival") != Name("Barry", "Percival")


def test_barry_is_harry():
    harry = Person(Name("Harry", "Percival"))
    barry = harry

    barry.name = Name("Barry", "Percival")

    assert harry is barry and barry is harry

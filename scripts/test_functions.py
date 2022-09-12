import pytest
from scripts.conftest import person_test_data

from .functions import is_bigger, panic, extract_allergies

# take function, glue yourself on top & do it again & again
@pytest.mark.parametrize("a,b,expected", [(1, 2, False), (4, 3, True), (51, 6, True)])
def test_is_bigger(a, b, expected):
    assert is_bigger(a, b) == expected


def test_no_panic():
    assert panic(False) == None


# how to test for things going wrong
def test_some_panic():
    with pytest.raises(Exception):
        panic(True)


def extract_allergies(extract_allergies2):
    assert len(extract_allergies2(person_test_data)) == 4

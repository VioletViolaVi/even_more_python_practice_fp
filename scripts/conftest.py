import pytest


@pytest.fixture
def person_test_data():
    return {
        "name": "Ronald",
        "fav_colour": "green",
        "diet": {
            "type": "herbivore",
            "allergies": ["potato", "cabbage", "oninion", "beans"]
        }
    }

import pytest
from def_cards import get_data
from settings import DATA_PATH
from def_cards import card_date
def test_get_data(DATA_PATH):
    assert isinstance(get_data(DATA_PATH),list)

def test_card_date(valid_data):
    assert card_date(valid_data) == []
import pytest
from project import height, weight, select_level


def test_select_level():
    assert select_level(1) == 20
    assert select_level(2) == 10


def test_weight_string_input():
    with pytest.raises(TypeError):
        weight('heavy')


def test_height_string_unput():
    with pytest.raises(TypeError):
        height('tall')


def test_weight_correct_inputs():
    assert weight(346) == '34.6kg'
    assert weight(4600) == '460.0kg'


def test_height_correct_inputs():
    assert height(15) == '1.5m'
    assert height(3) == '30cm'

import pytest
import main


@pytest.fixture
def lst():
    return main.List()


def test_add_elem_in_memory_range_1(lst):
    expected = [1, None, None, None, None]

    lst.add(1)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_add_elem_in_memory_range_2(lst):
    expected = [1, 5, 3, None, None]

    lst.add(1), lst.add(5), lst.add(3)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_add_elem_in_memory_range_3(lst):
    expected = [1, 5, 3, -17, 0]

    lst.add(1), lst.add(5), lst.add(3), lst.add(-17), lst.add(0)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_add_elem_more_memory_range_1(lst):
    expected = [1, 5, 3, -17, 0, 13, None]

    lst.add(1), lst.add(5), lst.add(3), lst.add(-17), lst.add(0), lst.add(13)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_add_elem_more_memory_range_2(lst):
    expected = [1, 5, 3, -17, 0, 13, -1, -5, None, None]

    lst.add(1), lst.add(5), lst.add(3), lst.add(-17)
    lst.add(0), lst.add(13), lst.add(-1), lst.add(-5)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'

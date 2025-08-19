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


def test_add_first_elem_in_memory_range_1(lst):
    expected = [1, None, None, None, None]

    lst.add_first(1)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_add_first_elem_in_memory_range_2(lst):
    expected = [-7, 13, 0, 5, 1]

    lst.add_first(1), lst.add_first(5), lst.add_first(0), lst.add_first(13), lst.add_first(-7)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_add_first_elem_more_memory_range_1(lst):
    expected = [2, -7, 13, 0, 5, 1, None]

    lst.add_first(1), lst.add_first(5), lst.add_first(0)
    lst.add_first(13), lst.add_first(-7), lst.add_first(2)
    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_add_first_elem_more_memory_range_2(lst):
    expected = [0, 2, -7, 13, -6, 0, 5, 1, None, None]

    lst.add_first(1), lst.add_first(5), lst.add_first(0), lst.add_first(-6)
    lst.add_first(13), lst.add_first(-7), lst.add_first(2), lst.add_first(0)
    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'
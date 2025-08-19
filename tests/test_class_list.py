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


def test_remove_memory_empty(lst):
    expected = None

    res = lst.remove(1)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_remove_memory_1(lst):
    expected = [5, 0, 13, -7, None]

    lst.add(1), lst.add(5), lst.add(0), lst.add(13), lst.add(-7)
    lst.remove(1)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_remove_memory_2(lst):
    expected = [1, 5, 13, -7, None]

    lst.add(1), lst.add(5), lst.add(0), lst.add(13), lst.add(-7)
    lst.remove(0)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_remove_memory_3(lst):
    expected = [1, 5, 0, 13, None]

    lst.add(1), lst.add(5), lst.add(0), lst.add(13), lst.add(-7)
    lst.remove(-7)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_pop_memory_empty(lst):
    expected = None

    res = lst.pop(1)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_pop_index_out_range_1(lst):
    expected = None

    lst.add(1), lst.add(5), lst.add(0), lst.add(13), lst.add(-7)

    res = lst.pop(150)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_pop_index_out_range_2(lst):
    expected = None

    lst.add(1), lst.add(5), lst.add(0), lst.add(13), lst.add(-7)

    res = lst.pop(-150)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_pop_index_no_int(lst):
    with pytest.raises(AssertionError):
        lst.pop('2')


def test_pop_index_in_range_1(lst):
    expected = 1

    lst.add(1), lst.add(5), lst.add(0), lst.add(13), lst.add(-7)

    res = lst.pop(0)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_pop_index_in_range_2(lst):
    expected = 0

    lst.add(1), lst.add(5), lst.add(0), lst.add(13), lst.add(-7)

    res = lst.pop(2)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_pop_index_in_range_3(lst):
    expected = -7

    lst.add(1), lst.add(5), lst.add(0), lst.add(13), lst.add(-7)

    res = lst.pop(4)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_insert_index_no_int(lst):
    with pytest.raises(AssertionError):
        lst.insert('2', 5)


def test_insert_index_out_range_in_memory_range_1(lst):
    expected = [3, None, None, None, None]

    lst.insert(14, 3)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_insert_index_out_range_in_memory_range_2(lst):
    expected = [1, 5, 0, 13, 3]

    lst.add(1), lst.add(5), lst.add(0), lst.add(13)
    lst.insert(14, 3)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_insert_index_in_range_in_memory_range_1(lst):
    expected = [3, 1, None, None, None]

    lst.add(1)
    lst.insert(0, 3)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_insert_index_in_range_in_memory_range_2(lst):
    expected = [1, 5, 3, 0, None]

    lst.add(1), lst.add(5), lst.add(0)
    lst.insert(2, 3)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_insert_index_in_range_in_memory_range_3(lst):
    expected = [3, 1, 5, 0, None]

    lst.add(1), lst.add(5), lst.add(0)
    lst.insert(0, 3)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_insert_index_in_range_in_memory_range_4(lst):
    expected = [1, 5, 0, 3, 7]

    lst.add(1), lst.add(5), lst.add(0), lst.add(7)
    lst.insert(3, 3)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_insert_index_in_range_out_memory_range_1(lst):
    expected = [3, 1, 5, 0, 7, 13, None]

    lst.add(1), lst.add(5), lst.add(0), lst.add(7), lst.add(13)
    lst.insert(0, 3)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_insert_index_in_range_out_memory_range_2(lst):
    expected = [1, 5, 3, 0, 7, 13, None]

    lst.add(1), lst.add(5), lst.add(0), lst.add(7), lst.add(13)
    lst.insert(2, 3)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_insert_index_out_range_out_memory_range_1(lst):
    expected = [1, 5, 0, 2, 9, 7, 6, 4, 8, 1, 3, None, None, None, None]

    lst.add(1), lst.add(5), lst.add(0), lst.add(2), lst.add(9)
    lst.add(7), lst.add(6), lst.add(4), lst.add(8), lst.add(1)
    lst.insert(25, 3)

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_find_elem_memory_empty(lst):
    expected = -1

    res = lst.find(1)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_find_elem_memory_no_empty_1(lst):
    expected = -1

    lst.add(1), lst.add(5), lst.add(0), lst.add(2)

    res = lst.find(13)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_find_elem_memory_no_empty_2(lst):
    expected = 2

    lst.add(1), lst.add(5), lst.add(13), lst.add(2)

    res = lst.find(13)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_count_entry_elem_memory_empty(lst):
    expected = 0

    res = lst.count_entry(13)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_count_entry_elem_memory_no_empty_1(lst):
    expected = 0

    lst.add(1), lst.add(5), lst.add(0), lst.add(2)

    res = lst.count_entry(13)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_count_entry_elem_memory_no_empty_2(lst):
    expected = 1

    lst.add(1), lst.add(5), lst.add(0), lst.add(2)

    res = lst.count_entry(2)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_count_entry_elem_memory_no_empty_3(lst):
    expected = 2

    lst.add(13), lst.add(5), lst.add(0), lst.add(13)

    res = lst.count_entry(13)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_count_entry_elem_memory_no_empty_4(lst):
    expected = 5

    lst.add(3), lst.add(3), lst.add(3), lst.add(3), lst.add(3)

    res = lst.count_entry(3)

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_clear_memory_empty(lst):
    expected = [None, None, None, None, None]

    lst.clear()

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_clear_memory_no_empty(lst):
    expected = [None, None, None, None, None]

    lst.add(3), lst.add(3), lst.add(3)
    lst.clear()

    res = lst.memory

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_lenght_memory_empty(lst):
    expected = 0

    res = lst.lenght()

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_lenght_memory_no_empty_1(lst):
    expected = 1

    lst.add(3)
    res = lst.lenght()

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_lenght_memory_no_empty_2(lst):
    expected = 4

    lst.add(1), lst.add(5), lst.add(0), lst.add(2)
    res = lst.lenght()

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_is_empty_memory_empty(lst):
    expected = True

    res = lst.is_empty()

    assert res == expected, f'Ожидали:{expected}, получили:{res}'


def test_is_empty_memory_no_empty(lst):
    expected = False

    lst.add(1), lst.add(5), lst.add(0)
    res = lst.is_empty()

    assert res == expected, f'Ожидали:{expected}, получили:{res}'

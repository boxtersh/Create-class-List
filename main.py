def malloc(N) -> list:
    """
    Функция выделяет память под список из пустых ячеек с количеством N (default)
    :param N: требуемое количество ячеек
    :return: список памяти из пустых ячеек с количеством N
    """
    return [None] * N


def realloc(now_memory, N) -> (list, int):
    """
    Функция расширяет память из пустых ячеек с количеством N (default) // 2
    :param now_memory: память сейчас
    :param N: расширение памяти на N // 2 ячеек
    :return: Картеж (список новой памяти, количество ячеек памяти)
    """
    new_memory = [None] * N + [None] * (N // 2)
    i = 0
    for _ in now_memory:
        new_memory[i] = now_memory[i]
        i += 1

    return new_memory, N + N // 2


class List:

    def __init__(self):
        self.__count = 0
        self.__size = 5
        self.__memory = malloc(self.__size)

    def __check_type(self, elem, type_elem):
        assert isinstance(elem, type_elem), f'Ожидали class:{type(type_elem)}, получили:{type(elem)}'

    def add(self, elem) -> None:
        """
        Функция добавляет элемент в конец списка
        :param elem: добавляемый элемент
        :return: None
        """
        if self.__count == self.__size:
            self.__memory, self.__size = realloc(self.__memory, self.__size)

        self.__memory[self.__count] = elem
        self.__count += 1

    def add_first(self, elem) -> None:
        """
        Функция добавляет элемент в начало списка
        :param elem: добавляемый элемент
        :return: None
        """
        if self.__count == self.__size:
            self.__memory, self.__size = realloc(self.__memory, self.__size)

        for i in range(self.__count):
            self.__memory[self.__count - i] = self.__memory[self.__count - 1 - i]

        self.__memory[0] = elem
        self.__count += 1

    def remove(self, elem) -> None:
        """
        Функция удаляет первый найденный элемент elem
        Если элемент не найден возвращает None
        :param elem: удаляемый элемент
        :return: None
        """
        if self.__count == 0: return

        index = 0

        while index <= self.__count - 1 and self.__memory[index] != elem:
            index += 1

        if self.__memory[index] == elem:
            for i in range(index, self.__count - 1):
                self.__memory[i] = self.__memory[i + 1]

            self.__memory[self.__count - 1] = None
            self.__count -= 1

    def pop(self, index) -> int | float | None:
        """
        Функция удаляет элемент по индексу возвращая его значение,
        если индекс вне диапазона списка возвращает None

        :param index: индекс удаляемого элемента
        :return: значение элемента по index
        """
        self.__check_type(index, int)

        if self.__count == 0:
            return

        elif index < 0 or index >= self.__count:
            return

        return_elem_index = self.__memory[index]
        for i in range(index, self.__count - 1):
            self.__memory[i] = self.__memory[i + 1]

        self.__memory[self.__count - 1] = None
        self.__count -= 1
        return return_elem_index

    def insert(self, index, elem) -> None:
        """
        Функция добавляет элемент elem в список по индексу index.
        Если index вне диапазона, добавляет elem в конец списка
        :param index: Позиция вставки элемента elem
        :param elem: Добавляемый элемент
        :return: None
        """
        self.__check_type(index, int)

        if (index >= self.__count or index < 0) and self.__count < self.__size:
            self.__memory[self.__count] = elem
            self.__count += 1

        elif (index >= self.__count or index < 0) and self.__count == self.__size:
            self.__memory, self.__size = realloc(self.__memory, self.__size)
            self.__memory[self.__count] = elem
            self.__count += 1

        elif index < self.__count and self.__count < self.__size:

            for i in range(self.__count, index, -1):
                self.__memory[i] = self.__memory[i - 1]

            self.__memory[index] = elem
            self.__count += 1

        else:
            self.__memory, self.__size = realloc(self.__memory, self.__size)

            for i in range(self.__count, index, -1):
                self.__memory[i] = self.__memory[i - 1]

            self.__memory[index] = elem
            self.__count += 1

    def find(self, elem) -> int:
        """
        Функция находит элемент в списке, возвращая его позицию (индекс)
        В случае отсутствия элемента возвращает -1
        :param elem:
        :return:
        """

        if self.__count == 0:
            return -1

        index = 0

        while index <= self.__count - 1 and self.__memory[index] != elem:
            index += 1

        if self.__memory[index] == elem:
            return index

        return -1

    def count_entry(self, elem) -> int:
        """
        Функция находит количество вхождений элемента elem
        В случае отсутствия возвращает 0
        :param elem: искомый элемент
        :return: количество вхождений
        """
        count_entries_elem_list = 0

        if self.__count == 0:
            return count_entries_elem_list

        for lis_item in self.__memory:
            if lis_item == elem:
                count_entries_elem_list += 1

        return count_entries_elem_list

    def clear(self) -> None:
        """
        Функция очищает память, устанавливая значения полей класса List по умолчанию
        self.__count = 0
        self.__size = 5
        self.__memory = [None] * 5
        :return: None
        """
        self.__count = 0
        self.__size = 5
        self.__memory = malloc(self.__size)

    def lenght(self) -> None:
        """
        Функция возвращает длину списка
        :return: длина списка
        """
        return self.__count

    def is_empty(self) -> bool:
        """
        Функция возвращает булево значение проверки списка на пустоту
        [1,2,3] -> True
        [] -> False
        :return: булево значение
        """
        if self.__count == 0:
            return True

        return False

    def get_count(self):
        return self.__count

    def get_memory(self):
        return self.__memory

    count = property(get_count)
    memory = property(get_memory)

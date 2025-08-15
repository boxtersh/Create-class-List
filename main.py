def malloc(N):
    return [None] * N


def realloc(now_memory, N):
    new_memory = [None] * N + [None] * (N // 2)

    for i in range(now_memory):
        new_memory[i] = now_memory[i]

    return new_memory


class List:

    def __init__(self):
        self.__count = 0
        self.__size = 5
        self.__memory = malloc(self.__size)

    def add(self, elem):
        if self.__count == self.__size:
            self.__memory = realloc(self.__memory, self.__size)

        self.__memory[self.__count] = elem
        self.__count += 1

    def add_first(self, elem):
        if self.__count == self.__size:
            self.__memory = realloc(self.__memory, self.__size)

        for i in range(self.__count):
            self.__memory[self.__count - i] = self.__memory[self.__count - 1 - i]
        self.__memory[0] = elem
        self.__count += 1
    # remove(elem) - -
    # - pop(index)
    # - insert(index, elem)
    # - find(elem)
    # count(elem)
    # clear()
    # lenght()
    # - is_empty()
    # - get_count()
    def get_count(self):
        return self.__count

    count = property(get_count)

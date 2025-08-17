def malloc(N):
    return [None] * N


def realloc(now_memory, N):
    new_memory = [None] * N + [None] * (N // 2)

    for i in range(now_memory):
        new_memory[i] = now_memory[i]

    return new_memory


def free(now_memory):
    now_memory = None


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

    def remove(self, elem):
        if self.__count == 0: return

        target_position = None
        i = self.__count - 1

        if self.__memory[i] == elem:
            self.__memory[i] = None
            self.__count -= 1
            return

        while i >= 0 or self.__memory[i] != elem:
            i -= 1
            if self.__memory[i] == elem:
                target_position = i

        if target_position != None:
            for i in range(target_position, self.__count - 1):
                self.__memory[i] = self.__memory[i + 1]

            self.__memory[self.__count - 1] = None
            self.__count -= 1

    def pop(self, index):
        if index > self.__count - 1:
            return

        return_elem_index = self.__memory[index]

        for i in range(index, self.__count - 1):
            self.__memory[i] = self.__memory[i + 1]

        self.__memory[self.__count - 1] = None
        self.__count -= 1
        return return_elem_index

    def insert(self, index, elem):
        if index >= self.__count and self.__count + 1 <= self.__memory:
            self.__memory[self.__count] = elem
            self.__count += 1

        elif index >= self.__count and self.__count + 1 > self.__memory:
            self.__memory = realloc(self.__memory, self.__size)
            self.__memory[self.__count] = elem
            self.__count += 1

        elif index < self.__count and self.__count + 1 <= self.__memory:

            for i in range(self.__count, index, -1):
                self.__memory[i] = self.__memory[i - 1]

            self.__memory[index] = elem

        else:
            self.__memory = realloc(self.__memory, self.__size)

            for i in range(self.__count, index, -1):
                self.__memory[i] = self.__memory[i - 1]

            self.__memory[index] = elem

    def find(self, elem):
        if self.__count == 0:
            return

        if self.__memory[0] == elem:
            return 0

        i = 0
        target_position = None
        while i != self.__count - 1 or self.__memory[i] != elem:
            i += 1
            if self.__memory[i] == elem:
                target_position = i

        if target_position != None:
            return target_position

    def count(self, elem):
        count_entries_elem_list = 0

        if self.__count == 0:
            return count_entries_elem_list

        for lis_item in range(self.__memory):
            if lis_item == elem:
                count_entries_elem_list += 1

        return count_entries_elem_list

    def clear(self):
        free(self.__memory)
        self.__memory = malloc(5)

    def lenght(self):
        return self.__count

    def is_empty(self):
        if self.__count == 0:
            return True

        return False

    # - get_count()
    def get_count(self):
        return self.__count

    count = property(get_count)

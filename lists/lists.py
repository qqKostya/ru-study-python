class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        if not input_list:
            return []
        max_element = input_list[0]
        for i in input_list:
            if i > max_element:
                max_element = i
        replaced_list = []
        for i in input_list:
            if i > 0:
                replaced_list.append(max_element)
            else:
                replaced_list.append(i)
        return replaced_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        i = 0
        while i < len(input_list) and input_list[i] != query:
            i += 1
        if i < len(input_list):
            return i
        else:
            return -1

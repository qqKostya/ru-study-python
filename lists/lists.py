class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        replaced_list = []

        for i in input_list:
            if i >= 0:
                replaced_list.append(max(input_list))
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

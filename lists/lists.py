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
        for element in input_list:
            if element > max_element:
                max_element = element
        replaced_list = []
        for element in input_list:
            if element > 0:
                replaced_list.append(max_element)
            else:
                replaced_list.append(element)
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
        left = 0
        right = len(input_list) - 1

        while left <= right:
            mid = (left + right) // 2

            if input_list[mid] == query:
                return mid

            if input_list[mid] < query:
                left = mid + 1
            else:
                right = mid - 1

        return -1

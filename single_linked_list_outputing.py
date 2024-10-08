# Заводим класс для односвязного списка.
# Для примера аннотируем значения элементов как целые числа.
class single_linked():
    """Класс для односвязных списков."""
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


# Для выполнения задачи вывода значений элементов списка в один проход
# сделаем рекурсивную функцию, которая будет формировать стек вызовов до того,
# как встретим базовый случай. После будем "снимать" функции со стека, печатая
# значения элементов через print().
def rec(el: single_linked) -> None:
    """Функция, которая выводит элементы односвязного списка задом наперёд."""

    if el.next is not None:  # Формируем стек вызовов до того, как не встретим значение None.
        rec(el.next)
    print(el.val, end=' ')  # Выводить будем в одну строку через пробел.


def filling(lst: list[int]) -> single_linked:
    """Функция для формирования односвязного списка из обычного списка Python (list)"""

    root = single_linked(lst[0])  # Сохраняем первый элемент как корневой (для возврата).
    cur_el = root

    # Формируем одностороннюю связь между элементами.
    for el in lst[1:]:
        cur_el.next = single_linked(el)
        cur_el = cur_el.next

    return root


if __name__ == '__main__':
    test_list = [0, 5, 8, 10, 1, -5, -9, 2]  # Список значений для элементов односвязного списка.

    # Формируем односвязный список, первый элемент сохраняя в переменную root.
    root = filling(test_list)

    # Выводим односвязный список задом наперёд.
    rec(root)

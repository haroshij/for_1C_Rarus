# Импортируем stdin для более быстрой обработки ввода данных.
from sys import stdin


def is_correct_bracket_sequence(expr: str) -> bool:
    """Функция, определяющая корректность расстановки
    круглых скобок в выражении"""

    # Вспомогательный список, куда будем добавлять открывающие скобки,
    # и удалять их, когда будем встречать закрывающие скобки.
    temp = list()

    # Последовательно перебираем все символы, игнорируя всё кроме круглых скобок.
    for symb in expr:
        if symb == '(':
            temp.append(symb)
        elif symb == ')':
            try:
                temp.pop()
            # Если встретили лишнюю закрывающую скобку, то обработаем ошибку.
            except IndexError:
                return False

    # Если остались лишние круглые скобки, то вернём False. Иначе скобки расставлены верно.
    return not bool(temp)


if __name__ == '__main__':
    print('Введите выражение:')
    expression = stdin.readline()
    if is_correct_bracket_sequence(expression):
        print('Скобки расставлены корректно')
    else:
        print('Скобки расставлены ошибочно')

def who_is_ruined(A: list[str], Na: int, B: list[str], Nb: int) -> list[str]:
    """Функция, которая возвращает перечень учащихся, которые в прошлом году были отличниками,
    а в текущем году не попали в этот список."""

    # Для линейной сложности удобнее работать со множеством,
    # поэтому список отличников прошлого года поместим во множество.
    ruined_set = set(A)

    # Пройдём по списку отличников текущего года и уберём каждого из множества
    # отличников прошлого года, если он там имеется.
    for student in B:
        if student in ruined_set:
            ruined_set.remove(student)

    # Возврашаем список "скатившихся" студентов.
    return list(ruined_set)


if __name__ == '__main__':
    # A - отличники прошлого года;
    A = ['Иванов', 'Петров', 'Сидоров', 'Предыбайло', 'Распутин', 'Перевертайло']
    # Nа - количество элементов в массиве A;
    Na = len(A)
    # B - отличники текущего года;
    B = ['Иванов', 'Петров', 'Путин', 'Перевертайло']
    # Nb - количество элементов в массиве B.
    Nb = len(B)
    ruined = who_is_ruined(A, Na, B, Nb)

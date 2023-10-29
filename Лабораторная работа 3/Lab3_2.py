# TODO Напишите функцию find_common_participants
def find_common_participants(a, b, delimiter=','):
    # Разбиваем строки на списки участников, используя указанный разделитель
    participants_first_group = a.split(delimiter)
    participants_second_group = b.split(delimiter)

    # Преобразуем списки участников в множества для выполнения операции пересечения
    set_first_group = set(participants_first_group)
    set_second_group = set(participants_second_group)

    # Находим общих участников
    common_participants = set_first_group.intersection(set_second_group)

    # Сортируем результат и возвращаем в виде списка
    return sorted(list(common_participants))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

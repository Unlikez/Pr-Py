# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, spl=","):
    group_1 = set(group1.split(spl))
    group_2 = set(group2.split(spl))
    group = list(group_1.intersection(group_2))
    group.sort()
    return group


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
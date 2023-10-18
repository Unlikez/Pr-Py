list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
quantity_players = len(list_players)
first_team = list_players[:(quantity_players // 2)]
second_team = list_players[quantity_players // 2:]  # TODO Разделите участников на две команды

print(first_team)
print(second_team)

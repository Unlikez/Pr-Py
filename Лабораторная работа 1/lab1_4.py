users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
register = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
quant = len(users)
uniq_users = set(users)
uniq_quant = len(uniq_users)

register["Общее количество"] = quant
register["Уникальные посещения"] = uniq_quant
print(register)

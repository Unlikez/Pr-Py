money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
while money_capital > 0:  # TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
    money_capital = money_capital - spend * ((increase + 1) ** month) + salary
    month += 1
    if money_capital < 0:
        month -= 1
print("Количество месяцев, которое можно протянуть без долгов:", month)

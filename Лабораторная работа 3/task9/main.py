salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев
total = 0
for i in range(1, 11):
        total = spend - salary
        spend *= 1.03
        need_money += total
print(round(need_money))

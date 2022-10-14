money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 1  # количество месяцев, которое можно прожить
total = money_capital+salary - spend
# TODO Оформить решение
while total >= 0:
    total -= spend
    month += 1
    spend = spend*(1+increase)
print(month)

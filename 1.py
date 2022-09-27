# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # Пример:
# # 	6782 -> 23
# # 	0,56 -> 11

value_polz = input('Введите число: ')
value_polz = value_polz.replace(",", "")
value_polz = value_polz.replace(".", "")
value_polz = int(value_polz)
sum = 0
while (value_polz > 9):
    count = value_polz % 10
    sum = sum + count
    value_polz = value_polz // 10

sum = sum + value_polz
print(sum)

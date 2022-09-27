# Задайте список из n чисел последовательности 〖(1+1/n)〗^n  и выведите на экран их сумму.

N = int (input ('Введите число N: '))
list = []
sum = 0

for i in range(1, N+1):
        list.append((1+1/i)**i)
        
for i in list:
    sum = sum + i

print (list)
print(round(sum, 2))
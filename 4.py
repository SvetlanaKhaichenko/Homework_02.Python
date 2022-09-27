# Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# # Пример:
# # Файл:
# # 4
# # 5
# # 2
# # N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# # Результат: 1*2*(-1) = -2


from random import randint
N = int(input('Введите число N: '))
list = []
list_position = []
result = 1
if N > 0:
    for i in range(-N, N+1):
        list.append(i)
elif N==0:
    print('Список нулевой, произведение элементов нулевое')
else:
    N *= -1
    for i in range(-N, N+1):
        list.append(i)

file_position = open ("PositionList.txt", "w+")
for item in range(N):
    file_position.write("%s\n" % randint(0, (N*2+1)))
file_position.close()
file_position = open ("PositionList.txt", "r+")
position = [line.strip() for line in file_position]
for i in position:
    i = int(i)
    result *= list[i]
file_position.close()

print(list)
print(position)
print (result)
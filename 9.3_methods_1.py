# Нижний регистр
# На вход программе подается строка. Напишите программу, которая
# подсчитывает количество буквенных символов в нижнем регистре.

# Формат входных данных
# На вход программе подается строка.

# Формат выходных данных

# ВАРИАНТ1
s = input()

counter = 0
for c in s:
    if c.islower() != False:
        counter += 1
print(counter)


# ВАРИАНТ2
s = input()

counter = 0
for c in s:
    if c != c.title():
        counter += 1
print(counter)

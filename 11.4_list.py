
# Значение функции
# На вход программе подается натуральное число nn, а затем n целых чисел. Напишите программу, которая для каждого введенного числа xx выводит значение функции f(x) = x ^ 2 + 2x + 1f(x) = x
# 2+2x+1, каждое на отдельной строке.
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn целых чисел, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести сначала введенные числа, затем пустую строку, а затем соответствующие значения функции
n = int(input())
L_1 = []
L_2 = []
for i in range(n):
    x = int(input())
    L_1.append(x)
    f = (x + 1)**2
    L_2.append(f)
print(*L_1, sep='\n')
print()
print(*L_2, sep='\n')


# Remove outliers
# При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение.
# На вход программе подается натуральное число nn, а затем nn различных натуральных чисел. Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.
# Формат входных данных
# На вход программе подаются натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

n = int(input())
L = []
for i in range(n):
    s = input()
    L.append(s)
s_search = input()
for j in range(len(L)):
    if s_search.lower() in L[j].lower():
        print(L[j])


# Google search - 2 🌶️🌶️
# На вход программе подается натуральное число nn, затем nn строк, затем число kk — количество поисковых запросов, затем kk строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.
# Формат входных данных
# На вход программе подаются натуральное число nn — количество строк, затем сами строки в указанном количестве, затем число kk, затем сами поисковые запросы.
# Формат выходных данных
# Программа должна вывести все введенные строки, в которых встречаются все поисковые запросы.
# Примечание. Поиск не должен быть чувствителен к регистру символов.

n = int(input())
L = []
for i in range(n):
    s = input()
    L.append(s)
n_search = int(input())
L_1 = []
for j in range(n_search):
    k_search = input()
    L_1.append(k_search)
List = []
counter = 0
for i_1 in L:
    for j_1 in L_1:
        if j_1.lower() in i_1.lower():
            counter += 1
    if counter == len(L_1):
        List.append(i_1)
    counter = 0
print(*List, sep='\n')

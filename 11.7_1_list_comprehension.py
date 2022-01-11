
# ПУЗЫРЬКОВАЯ СОРТИРОВКА
# Алгоритм сортировки пузырьком состоит из повторяющихся
# проходов по сортируемому списку. За каждый проход элементы
# последовательно сравниваются попарно и, если порядок в паре
# неверный, выполняется обмен элементов. Проходы по списку
# повторяются n-1n−1 раз, где nn – длина списка. При каждом
# проходе алгоритма по внутреннему циклу, очередной наибольший
# элемент списка ставится на свое место в конце списка рядом
# с предыдущим «наибольшим элементом».

a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)
# реализация алгоритма пузырьковой сортировки
for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)


# СОРТИРОВКА ВЫБОРОМ
# Сортировка выбором улучшает пузырьковую сортировку, совершая
# всего один обмен за каждый проход по списку. Для этого
# алгоритм ищет максимальный элемент и помещает его на
# соответствующую позицию. Как и для пузырьковой сортировки,
# после первого прохода самый большой элемент находится на
# правильном месте. После второго прохода на своё место
# становится следующий максимальный элемент. Проходы по
# списку повторяются n-1n−1 раз, где nn – длина списка,
# поскольку последний из них автоматически оказывается на
# своем месте.
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)
# реализация алгоритма сортировки выбором
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)

# СОРТИРОВКА ПРОСТЫМИ ВСТАВКАМИ
# Алгоритм сортировки простыми вставками делит список на 2 части
# — отсортированную и неотсортированную. Из неотсортированной
# части извлекается очередной элемент и вставляется на нужную
# позицию, в результате чего отсортированная часть списка
# увеличивается, а неотсортированная уменьшается. Так происходит,
# пока не исчерпан набор входных данных  и не отсортированы
# все элементы.

# Следующий программный код реализует алгоритм сортировки
# простыми вставками:

a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)

for i in range(1, n):
    elem = a[i]  # первый элемент из неотсортированной части списка
    j = i
    while j >= 1 and a[j - 1] > elem:
        a[j] = a[j - 1]
        j -= 1
    a[j] = elem


print('Отсортированный список:', a)

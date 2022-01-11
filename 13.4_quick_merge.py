# Быстрое слияние двух отсортированных списков в один
# Пусть мы имеем два уже отсортированных по возрастанию списка list1 и list2.

# Алгоритм быстрого слияния следующий:

# Создаем численные указатели p1 = 0 и p2 = 0 на начала обоих списков list1 и list2
# соответственно
# На каждом шаге берем меньший из двух элементов list1[p1] и list2[p2]
# Записываем его в результирующий список
# Увеличиваем указатель на первый элемент списка(p1 или p2) из которого был взят
# элемент на 11
# Когда один из начальных списков закончился, добавляем все оставшиеся элементы
# второго списка в результирующий список.


def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


# Следующий программный код:

list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = quick_merge(list1, list2)
print(list3)

"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""
import hashlib


def uniq_count(string):

    string = str(string).lower()

    length = len(string)

    hash_set = set()

    for i in range(length + 1):
        for j in range(i + 1, length + 1):
            h = hashlib.sha256(string[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)

    return len(hash_set)


my_string = 'algorythm'

print(f'Количество различных подстрок в строке {my_string}: {uniq_count(my_string)}')

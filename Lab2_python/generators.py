# ----------------TASK------------------------------------
# Напишите функцию, которая принимает на вход канал состоящий
# из последовательности чисел, первое из которых является количеством
# последующих элементов, которые нужно поместить в массив,
# а за ней следуют элементы этого массива, и возвращающая отдельные массивы.
# Например 3, 4, 0, 2, 1, 2, 2, 4, 5 будет превращено в [4, 0, 2], [2], [4, 5]
from data import lst


# генераторы
def get_indexies(channel):
    i = 0
    first = 0
    last = 0
    ind = []
    while i < len(channel):
        first = i + 1
        last = i + channel[i]
        i += channel[i] + 1
        ind.append((first, last))
    return ind


def get_lsts(ind, c):
    yield [c[i] for i in range(ind[0], ind[1] + 1)]


res = []
for i in range(len(get_indexies(lst))):
    gen = get_lsts(get_indexies(lst)[i], lst)
    res.append(gen)

for i in res:
    for j in i:
        print(j)

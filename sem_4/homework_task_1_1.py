# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения
# вычислений.


import numpy as np
import threading
import time
from  random import randint


all_sum = []


def fill_list():
    numbers: list[int]  = []
    for _ in range(1000001):
        numbers.append(randint(1, 100))
    lst1, lst2, lst3, lst4 =  np.array_split(numbers, 4)
    big_list = [lst1, lst2, lst3, lst4]
    return big_list


def big_sum(numbers: list):
    all_sum.append(sum(numbers))
    
    print('Sum of list: {}'.format(sum(numbers)))
    

threads = []

start_time = time.time()


for lst in fill_list():
    thread = threading.Thread(target=big_sum, args=(lst,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


print(f'All sum =  {sum(all_sum)}')
print('Completed summing in {:.2f} seconds'.format(time.time() - start_time))  
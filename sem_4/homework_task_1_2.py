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

import multiprocessing
import time
from  random import randint

all_sum = []

def fill_list():
    numbers: list[int]  = []
    for _ in range(1000000):
        numbers.append(randint(1, 100))
    lst1, lst2, lst3, lst4 =  np.array_split(numbers, 4)
    big_list = [lst1, lst2, lst3, lst4]
    return big_list


def big_sum(numbers: list):
    print('Sum of list: {}'.format(sum(numbers)))
    
    
processes = []


if __name__ == '__main__':
    start_time = time.time()
    for lst in fill_list():
        process = multiprocessing.Process(target=big_sum, args=(lst,))
        all_sum.append(sum(lst))
        processes.append(process)
        process.start()
            
    for process in processes:
        process.join()
        
    
    print(f'All sum =  {sum(all_sum)}')
    print('Completed download in {:.2f} seconds'.format(time.time() - start_time))  
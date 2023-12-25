# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.


import os
from pathlib import Path
import multiprocessing
import requests
import time


BASE_DIR = Path(__file__).resolve().parent


def get_words_count(el: str):
    if os.path.isfile(os.path.join(BASE_DIR, el)):
        with open(os.path.join(BASE_DIR, el), encoding='utf-8') as file:
            words = 0
            for line in file:
                words += len(line.strip().split(' '))
            print(f'File {el} has {words} words')
    

if __name__ == '__main__':
    processes = []
    
    start_time = time.time()
    
    for el in os.listdir(BASE_DIR):
        process = multiprocessing.Process(target=get_words_count, args=(el,))
        processes.append(process)
        process.start()
            
    for process in processes:
        process.join()
        
    print('Completed download in {:.2f} seconds'.format(time.time() - start_time))  
    
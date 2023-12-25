# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.
# Используйте потоки.


import os
from pathlib import Path
import threading
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
                
                
threads: list[threading.Thread] = []


start_time = time.time()

for el in os.listdir(BASE_DIR):
    thread = threading.Thread(target=get_words_count, args=[el])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


print('Completed word in {:.4f} seconds'.format(time.time() - start_time))  
"""
Написать программу, которая считывает список из 10 URL-адресов и одновременно
 загружает данные с каждого адреса. 
После загрузки данных нужно записать их в отдельные файлы.
Используя многопроцессорность.
"""

import os
from pathlib import Path
import multiprocessing
import requests
import time


BASE_DIR = Path(__file__).resolve().parent
saves_dir = os.path.join(BASE_DIR,'saves')

if not os.path.exists(saves_dir):
    os.makedirs(saves_dir)

urls = [
    'http://yahoo.com',
    'http://www.google.com',
    'http://ya.ru',
    'http://gb.ru',
    'http://ru.wikipedia.org',
    'http://www.vk.com',
    'http://www.reddit.com',
    'http://www.tumblr.com',
    'http://www.python.org',
]


def download(url: str):
    response = requests.get(url, stream=True)
    filename = url.replace('http://', '').replace('https://', '').replace('www.', '').replace('/', '-').replace('www.', '') + '.html'  
    with open(os.path.join(saves_dir, filename), 'w', encoding='utf-8') as file:
        file.write(response.text)
        

if __name__ == '__main__':
    start_time = time.time()
    
    processes = []
    
    
    for url in urls:
        process = multiprocessing.Process(target=download, args=(url,))
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join()
        
    print('Completed download in {:.2f} seconds'.format(time.time() - start_time))  
    
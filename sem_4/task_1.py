"""
Написать программу, которая считывает список из 10 URL-адресов и одновременно
 загружает данные с каждого адреса. 
После загрузки данных нужно записать их в отдельные файлы.
Используйте потоки.
"""


import os
from pathlib import Path
import threading
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

threads = []

start_time = time.time()


for url in urls:
    thread = threading.Thread(target=download, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('Completed download in {:.2f} seconds'.format(time.time() - start_time))  
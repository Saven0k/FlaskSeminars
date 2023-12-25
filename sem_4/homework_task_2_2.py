# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, 
# название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.


import sys
import os
from pathlib import Path
import multiprocessing
import requests
import time


BASE_DIR = Path(__file__).resolve().parent
saves_dir = os.path.join(BASE_DIR,'hw_t_2_2_saves')


if not os.path.exists(saves_dir):
    os.makedirs(saves_dir)


def console():
    urls = sys.argv[1:]

    if not urls:
        print("Использование: python script.py url1 url2 url3")
        urls_default = [
            'https://img.freepik.com/premium-photo/best-birds-animal-4k-resolution-image_911151-10.jpg',
            'https://img.freepik.com/premium-photo/luxury-4k-highly-resolution-animals-wallpaper-background_649024-7898.jpg',
            'https://i.pinimg.com/736x/f4/db/ab/f4dbabbca7ca6bbd102c6ceaee6f108c.jpg',
            'https://img.freepik.com/premium-photo/national-animal-of-costa-rica-high-quality-4k-ul_670382-77652.jpg',
        ]
        return urls_default
    
    return urls


def download(url: str):
    response = requests.get(url, stream=True)
    filename = str(url.split('/')[-1:]).replace('[', '').replace(']', '').replace(' ', '').replace("'", '')
    with open(os.path.join(saves_dir, filename), 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    processes = []
    
    start_big_time = time.time()
    for url in console():
        # start_small_time = time.time()
        process = multiprocessing.Process(target=download, args=(url,))
        processes.append(process)
        process.start()
        # print(f'Download  photo in {time.time() - start_small_time:.10f}')
        
        
    for process in processes:
        start_small_time = time.time()
        process.join()
        print(f'Download  photo in {time.time() - start_small_time:.10f}') #Если ли разница, где считывать время выполнения программы?
        
        
    print('Completed all download in {:.2f} seconds'.format(time.time() - start_big_time))   
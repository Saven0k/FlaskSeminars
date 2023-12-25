# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и выводить результаты в консоль.


import aiofiles
import os
from pathlib import Path
import asyncio
import time


BASE_DIR = Path(__file__).resolve().parent


async def get_words_count(filename: str):
    file_path = os.path.join(BASE_DIR, filename)
    
    async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
        words = 0
        
        for line in await file.readlines():
            words += len(line.strip().split(' '))
        
        print(f'File {filename} has {words} words')
              

async def main():
    tasks = []

    for el in os.listdir(BASE_DIR):
        task = asyncio.ensure_future(get_words_count(el))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print('Completed download in {:.2f} seconds'.format(time.time() - start_time))      
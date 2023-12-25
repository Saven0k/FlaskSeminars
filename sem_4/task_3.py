"""
Написать программу, которая считывает список из 10 URL-адресов и одновременно
 загружает данные с каждого адреса. 
После загрузки данных нужно записать их в отдельные файлы.
Используя асинхронность.
"""

import os
from pathlib import Path
import aiohttp
import asyncio
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
]


async def download_content(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = url.replace('http://', '').replace('https://', '').replace('www.', '').replace('/', '-').replace('www.', '') + '_async.html'  
            content = await response.text()
            with open(os.path.join(saves_dir, filename), 'w', encoding='utf-8') as file:
                file.write(content)                    
                
                
async def main():
    tasks = []
    
    for url in urls:
        task = asyncio.ensure_future(download_content(url))
        tasks.append(task)
        
    await asyncio.gather(*tasks)
    

    
if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
    print('Completed download in {:.2f} seconds'.format(time.time() - start_time))      
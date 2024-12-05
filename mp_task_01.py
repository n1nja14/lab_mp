import asyncio
import threading
import time
import multiprocessing
import math
import requests

# список url
urls = ['https://www.example.com'] * 10


def fetch_url(url):
    response = requests.get(url)
    return response.text


def sequence():
    start_time = time.time()
    for url in urls:
        fetch_url(url)
    # выполнение функции fetch_url для каждого url из urls
    end_time = time.time()
    print(f'sequence time: {end_time - start_time: 0.2f} \n')

def threads():
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f'threads time: {end_time - start_time: 0.2f} \n')

def processes():
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(fetch_url, urls)
    end_time = time.time()
    print(f'processes time: {end_time - start_time: 0.2f} \n')


async def fetch_url_async(url):
    return requests.get(url).text


async def async_():
    start_time = time.time()
    tasks = [asyncio.create_task(fetch_url_async(url)) for url in urls]
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f'async_ time: {end_time - start_time: 0.2f} \n')


if __name__ == '__main__':
    sequence()
    threads()
    processes()
    asyncio.run(async_())
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        sequence time:  5.65 
        threads time:  0.58
        processes time:  1.99
    """

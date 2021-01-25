import time
from concurrent.futures.thread import ThreadPoolExecutor

import requests
import json
from urllib import request
import multiprocessing
import aiohttp
import nest_asyncio
import asyncio

#Synchronicznie

def download_images():
    response = requests.get("https://picsum.photos/v2/list")
    if response.status_code != 200:
        raise AttributeError('GET /tasks/ {}'.format(response.status_code))
    data = json.loads(response.text)
    pictures=[]
    for s in data:
        pictures.append(s['download_url']+".jpg")
    return pictures

def saveImages(link):
    filename = link.split('/')[6].split('.')[0]
    fileformat = link.split('/')[6].split('.')[1]
    request.urlretrieve(link, "images/{}.{}".format(filename, fileformat))

def main():
    images = download_images()
    for image in images:
        saveImages(image)

start_time = time.time()
main()
duration_synch = time.time() - start_time
print(f"Synchronicznie: {duration_synch}s")


#Asynchronicznie - multithreading

def process_images_threading():
    images = download_images()
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(saveImages, images)

start_time = time.time()
process_images_threading()
duration_multithreading = time.time() - start_time
print(f"Asynchronicznie - multithreading: {duration_multithreading}s")


#Asynchronicznie - multiprocessing
def process_images_processing():
    images = download_images()
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.map(saveImages, images)

start_time = time.time()
process_images_processing()
duration_multiprocessing = time.time() - start_time
print(f"Asynchronicznie - multiprocessing: {duration_multiprocessing}s")

#Asynchronicznie - biblioteka Asyncio

async def download_images_asyncio(link, session):
    filename = link.split('/')[6].split('.')[0]
    fileformat = link.split('/')[6].split('.')[1]
    async with session.get(link) as response:
        with open("images/{}.{}".format(filename, fileformat), 'wb') as fd:
            async for data in response.content.iter_chunked(1024):
                fd.write(data)

async def main_asyncio():
    images = download_images()

    async with aiohttp.ClientSession() as session:
        tasks=[download_images_asyncio(image,session)for image in images]
        return await asyncio.gather(*tasks)

start_time = time.time()
nest_asyncio.apply()
asyncio.run(main_asyncio())
duration_asyncio = time.time() - start_time
print(f"Asynchronicznie - biblioteka Asyncio: {duration_asyncio}s")
import requests
import time
import concurrent.futures
import threading

import asyncio
import aiohttp

import multiprocessing

print("I/O")

# Wersja synchroniczna
def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            session.get(url)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Wersja synchroniczna(jeden po drugim) -  {len(sites)} stron w przeciągu {duration} sekund")


# Program z użyciem pięciu wątków
thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        session.get(url)

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Wersja asynchroniczna(na pięciu wątkach) -  {len(sites)} stron w przeciągu {duration} sekund")


# Z biblioteką Asyncio oraz słowami kluczowymi await oraz async
async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(session.get(url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Wersja asynchroniczna(z użyciem biblioteki Asyncio oraz słów kluczowych await oraz async) - {len(sites)} stron w przeciągu {duration} sekund")


# Wersja z wykorzystaniem wielu procesorów
session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        session.get(url)

def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Wersja asynchroniczna(z wykorzystaniem procesorów komputera) -  {len(sites)} stron w przeciągu {duration} sekund")
    print("Wersja z wykorzystaniem procesorów może nie jest najszybsza co spowodowane jest koniecznością tworzenia oddzielnego interpretera dla każdego procesu, lecz jest najprostsza w implementacji oraz wymaga niewiele dodatkowego kodu.")

print("CPU-Bound")


# Wersja synchroniczna - CPU Bound
def cpu_bound(number):
    return sum(i * i for i in range(number))

def find_sums(numbers):
    for number in numbers:
        cpu_bound(number)

if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]
    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Wersja synchroniczna - CPU Bound - {duration} sekund")


# Wersja asynchroniczna z wieloma procesorami - CPU Bound

def cpu_bound(number):
    return sum(i * i for i in range(number))

def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)

if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]
    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Wersja asynchroniczna z wieloma procesorami - {duration} sekund")

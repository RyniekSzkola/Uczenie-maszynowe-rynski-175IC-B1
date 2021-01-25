### I/O
```
Wersja synchroniczna(jeden po drugim) -  160 stron w przeciągu 16.705066680908203 sekund
Wersja asynchroniczna(na pięciu wątkach) -  160 stron w przeciągu 5.242202043533325 sekund
Wersja asynchroniczna(z użyciem biblioteki Asyncio oraz słów kluczowych await oraz async) - 160 stron w przeciągu 0.5485837459564209 sekund
Wersja asynchroniczna(z wykorzystaniem procesorów komputera) -  160 stron w przeciągu 8.758083820343018 sekund
```

### CPU-Bound
```
Wersja synchroniczna - CPU Bound - 9.576741695404053 sekund
Wersja asynchroniczna z wykorzystaniem wielu procesorów - 6.002724647521973 sekund
```

### Pobieranie i zapisywanie zdjęć
```
Wersja synchroniczna: 94.4830892086029s
Wersja asynchroniczna - multithreading: 21.02152729034424 sekund
Wersja asynchroniczna - multiprocessing: 24.93849229812622 sekund
Wersja asynchroniczna - biblioteka Asyncio: 9.84400463104248 sekund
```

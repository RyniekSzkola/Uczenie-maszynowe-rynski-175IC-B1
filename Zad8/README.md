### Zad8 - Praca z danymi w formacie JSON i CSV<br/>

### Wykorzystane klasy i funkcje

### <b>JSON</b>
```
json.dump() - Serializuje argument do formatu JSON i zwraca strumień bajtów.
json.dumps() - Serializuje przekazany w parametrze obiekt i zwraca JSON w postaci Stringa
json.load() - Deserializuje zawartosc pliku jsonowego podanego w parametrze jako sciezka do niego i zwraca obiekt Pythonowy
json.loads() - Deserializuje ciąg znaków(String) przekazany jako parametr i zwraca obiekt Pythonowy
sorted() - Sortuje przekazaną listę
len() - Zwraca długość listy
requests.get() - Wysyła zapytanie typu GET pod adres wskazany w parametrze.
klasa Elf - Niestandardowy obiekt Pythonowy używany do próby deserializacji oraz serializacji.
klasa JSONEncoder - Klasa którą możemy odziedziczyć i nadpisać domyślną serializację konkretnego typu
```

### <b>CSV</b>
```
csv.reader() - Przyjmuje jako argument plik z danymi w formacie CSV i zwraca czytelny obiekt Pythonowy
csv.writer() - Zwraca obiekt który odpowiedzialny jest za zapisywania danych do pliku CSV
writerow() - Dopisuje linie do pliku csv. Przyjmuje tablice
writerows() - Dopisuje wiele liń do pliku csv. Przyjmuje liste tablic.
writeheader() - Pisze linie z nazwami poszczególny kolum(o ile zostały one sprecyzowane w konstruktorze obiektu DictWriter)
pd.read_csv() - Funkcja z pakietu Pandas. Wczytuje plik formatu CSV i zwraca obiekt charakterystyczny dla Pandas - DataFrame
```

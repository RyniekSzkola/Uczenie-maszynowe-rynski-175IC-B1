# Uczenie-maszynowe-rynski-175IC-B1
Zad6 - Praca z plikami<br/>

### Otwarcie pliku
```
file = open('rynski.txt')
print(file)
```

### Otwarcie pliku a następnie zamknięcie po wykonaniu instrukcji w bloku try
```
reader = open('rynski.txt')
try:
    reader.read()
finally:
    reader.close()
```

### Alternatywa dla powyższej instrukcji. Otwieramy plik, wykonujemy instrukcje a następnie zamykamy(bez bloku finally)
```
with open('rynski.txt') as reader:
    reader.read()
```

### Typy plików - zwracają obiekt zależnie od trybu w jakim otwieramy plik
```
print(type(open('rynski.txt')))
print(type(open('rynski.txt', 'r')))
print(type(open('rynski.txt', 'rb')))
print(type(open('rynski.txt', 'rb', buffering=0)))
```

#### Czytanie otwartych plików
```
with open('rynski.txt', 'r') as reader:
    print(reader.read())
```
 
### Czytanie 5 bajtów z pierwszej linijki + 5 kolejnych z pierwszej linijki
```
with open('rynski.txt', 'r') as reader:
    print(reader.readline(5))
    print(reader.readline(5))
```

### Zwrócenie tekstu jako lista
```
f = open('rynski.txt')
print(list(f))
```

### Iterowanie po każdej linii w pliku na 3 różne sposoby
### Pętla while - readline()
```
with open('rynski.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
         print(line, end='')
         line = reader.readline()
```

### Pętla for - readlines()
```
with open('rynski.txt', 'r') as reader:
     for line in reader.readlines():
         print(line, end='')
```

### Pętla for - iteracja przez obiekt reader
```
with open('rynski.txt', 'r') as reader:
     for line in reader:
         print(line, end='')
```

### Zapis odwroconego tekstu ze starego pliku do nowego
```
with open('rynski.txt', 'r') as reader:
    read_only_text = reader.readlines()
with open('rynski_new.txt', 'w') as writer:
    for text in reversed(read_only_text):
        writer.write(text)
with open('rynski_new.txt', 'r') as reader:
    print(reader.read())
```

### Wczytanie obrazu w postaci bajtow i wypisanie danych danych
```
with open('test.jpg', 'rb') as byte_reader:
     print(byte_reader.read(1))
     print(byte_reader.read(3))
     print(byte_reader.read(2))
     print(byte_reader.read(1))
     print(byte_reader.read(1))
```

### Dodawanie nowej lini do pliku i wyswietlenie zawartosci
```
with open('rynski.txt', 'a') as a_writer:
    a_writer.write('\nDodana')
with open('rynski.txt', 'r') as reader:
    print(reader.read())
```

### Praca z dwoma plikami jednoczesnie
```
d_path = 'rynski.txt'
d_r_path = 'rynski_new.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    temp = reader.readlines()
    writer.writelines(reversed(temp))
```

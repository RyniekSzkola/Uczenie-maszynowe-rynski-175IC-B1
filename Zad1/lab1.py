import numpy as np

#tablica 10 zer
a1 = np.zeros((10))

#tablica 10 piątek
a2 = np.array([5,5,5,5,5,5,5,5,5,5])

#tablica od 10 do 50
a3 = np.arange(10, 51)

#tablica 3-wymiarowa z liczbami od 0 do 8
a4 = np.zeros((3, 9))
a4 += np.arange(9)

#macierz jednostkowa 3x3
a5 = np.identity(3)

#macierz o wymiarach 5x5 zawierajaca liczby z dystrybucji normalnej(Gaussa)
a6 = np.random.normal(0, 1, size=(5, 5))

#macierz o wymiarach 10x10 zawierającą liczby od 0,01 do 1 z krokiem 0,01
a7 = np.arange(0, 1, 0.01).reshape((10,10))

#utwórz tablicę zawierającą 20 liniowo rozłożonych liczb między 0 a 1 (włącznie z 0 i 1)
a8 = np.linspace(0, 1, 10)

#utwórz tablicę zawierającą losowe liczby z przedziału (1, 25), następnie zamień ją na macierz o wymiarach 5 x 5 z tymi samymi liczbami:
a9 = np.random.randint(25, size=(25))
a9 = a9.reshape((5, 5))
#oblicz sumę wszystkich liczb w ww. macierzy
a9a = a9.sum()
#oblicz średnią wszystkich liczb w ww. macierzy,
a9b = np.average(a9)
#oblicz standardową dewiację dla liczb w ww. macierzy,
a9c = np.std(a9)
#oblicz sumę każdej kolumny ww. macierzy i zapisz ją do tablicy.
a9d = a9.sum(axis=0)

#utwórz macierz o wymiarach 5x5 zawierającą losowe liczby z przedziału (0, 100) i:
a10 = np.random.randint(100, size=(25))
a10 = a9.reshape((5, 5))
#oblicz medianę tych liczb,
print(np.median(a10))
#znajdź najmniejszą liczbę tej macierzy,
print(np.min(a10))
#znajdź największą liczbę tej macierzy.
print(np.max(a10))

#utwórz macierz o wymiarach różnych od siebie i większych od 1, zawierającą losowe liczby z przedziału (0, 100) i dokonaj jej transpozycji,
a11 = np.random.rand(4, 5) * 100 + 1
a11 = np.transpose(a11)

#utwórz dwie macierze o odpowiednich wymiarach (doczytać), większych od 2 i dodaj je do siebie,
a12a = np.random.rand(4, 5) * 100 + 1
a12b = np.random.rand(4, 5) * 100 + 1
a12c = a12a + a12b

#utwórz dwie macierze o odpowiednich wymiarach (doczytać) różnych od siebie i większych od 2, a następnie pomnóż je przez siebie za pomocą dwóch różnych
a13a = np.random.rand(2, 5) + 2  #+2 zeby byly wieksze od dwoch
a13b = np.random.rand(5, 2) + 2
a13c = np.matmul(a13a, a13b)
a13d = np.dot(a13a, a13b)




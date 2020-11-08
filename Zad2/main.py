import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#wczytujemy plik csv
data = pd.read_csv('samochody1tys.csv')

#Tworzymy kopie naszych danych oraz zmieniamy nazwy kolumn
data_copy = data.rename(columns={"id" : "ID", "marka" : "MARKA", "model" : "MODEL", "przebieg" : "PRZEBIEG", "cena" : "CENA", "wojewodztwo" : "WOJEWODZTWO"}).copy()
#print(data_copy)

#Grupujemy nasze dane i zliczamy: najniższy, najwyższy oraz łączny przebieg wszystkich samochodów każdej z marki
data_copy1 = data_copy.groupby('MARKA')['PRZEBIEG'].agg([min, max, sum])
#print(data_copy1)

#Tworzymy wykres slupkowy ktory przedstawia częstotliwość występowania wartości każdej z kolumn w pewnym przedziale. Na przykład kolumna ID zawsze znajduje się w przedziale od 0 do 1000
# więc częstotliwość jej występowania dla pierwszej kolumny jest równa 100, a dla reszty jest równa 0.
ax = data_copy.plot.hist(bins=10, alpha=0.5)
ax.plot()
#plt.show()

#Stworzyliśmy wykres kołowy porównujący łączną sumę cen każdej z marki i w ten sposób możemy na przykład zauważyć, że łączna suma samochodów Mercedes-Benz jest wyższa niż pozostałych
data_copy2 = data_copy.groupby('MARKA')['CENA'].sum().plot(kind='pie')
#plt.show()

#Funkcja z pakietu pandas pobierająca 10 losowych wierszy z naszego zestawu danych a następnie sortująca je rosnąco według ceny
data_copy3 = data_copy.sample(10).sort_values('CENA')
#print(data_copy3)

#Funkcja z pakietu Pandas określająca liczbę unikalnych wartości z danej kolumny. Widzimy, że dla całego tego zestawu danych zostało użytych 6 rodzajów silnika, a także ogłoszenia pochodzą z każdego istniejącego województwa.
data_copy4 = data_copy.nunique()
#print(data_copy4)

#Funkcja zmieniająca wszystkie litery w wybranej kolumnie na wielkie
data_copy5 = data_copy['MARKA'].map(lambda name: name.upper())
#print(data_copy5)

#Tworzymy nową tablice z losowymi liczbami całkowitymi o długości równej liczbie kolumn naszego zestawu danych za pomocą biblioteki numpy
testRow = np.random.randint(10, size=len(data_copy))
#Przekształcamy ją na strukturę danych charakterystyczną dla pakietu Pandas
test_row = pd.DataFrame(testRow)
#Dołączamy ten zestaw danych do istniejącego już zestawu danych. Użyliśmy metody "insert" z pakietu Pandas która umożliwia dodanie nowej kolumny.
data_copy.insert(2,  'Nowa kolumna', test_row)
#print(data_copy)

#Funkcja zmieniająca kolumny na wiersze i wiersze na kolumny
data_copy7 = pd.melt(data_copy)
#print(data_copy7)

#Funkcja usuwająca wybrane kolumny
data_copy8 = data_copy.drop(columns=['Nowa kolumna', 'CENA'])
print(data_copy8)
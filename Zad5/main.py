import spacy
from collections import Counter

# Wczytanie modelu języka polskiego
nlp = spacy.load("pl_core_news_sm")

#Funkcja 1
# Sczytywanie Stringa przez obiekt nlp(instancja modelu języka) i zapisywanie do obiektu Doc charakterystycznego dla Spacy
introduction_text = ('Ten poradnik jest o przetwarzaniu języka naturalnego w Spacy.')
introduction_doc = nlp(introduction_text)
# Sczytywanie pojedyńczych słów
#print([token.text for token in introduction_doc])

#Funkcja 2
# Sczytywanie danych z pliku tekstowego za pomocą Spacy i zapisywanie do obiektu Doc charakterystycznego dla Spacy
file_name = 'test.txt'
introduction_file_text = open(file_name).read()
# Plik Doc typowy dla Spacy
introduction_file_doc = nlp(introduction_file_text)
# Sczytywanie pojedyńczych słów
#print ([token.text for token in introduction_file_doc])

#Funkcja 3
# Detekcja zdań.
# Metoda sents dzieli wprowadzony ciąg tekstowy na zdania które następnie zapisuje do tablicy(tupli ?) którą możemy następnie wylistować
about_text = ('Michał Ryński jest programistą Java obecnie' +
              ' pracującym dla gdańskiej' +
              ' firmy. Obecnie jest on zainteresowany nauką' +
              ' Przetwarzania Naturalnego Języka.')
about_doc = nlp(about_text)
sentences = list(about_doc.sents)
len(sentences)
for sentence in sentences:
    print (sentence)

#Funkcja 4
# Własne ustawianie ograniczników, domyślnie metoda sents dzieli zdania na podstawie kropek na końcu zdań.
# Możemy ustawić własne ustawienia i dodać na przykład jako ogranicznik 3 kropki co widzimy na poniższym przykładzie.
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == '...':
            doc[token.i+1].is_sent_start = True
    return doc

# Stworzyliśmy metode dodającą jako ogranicznik do metody sents trzy kropki
# A następnie stworzyliśmy nowy model języka tym razem dodając własne ustawienia.
# Następnie ponownie wywołaliśmy metodę sents i tym razem widzimy, że nasze zdanie zostało podzielone na podstawie ogranicznika trzech kropek.
ellipsis_text = ('Michał, czy możesz, ... nieważne, Zapomniałem'
                 ' co chciałem powiedzieć... Czyli, nie uważasz że powinniśmy...')
custom_nlp = spacy.load('pl_core_news_sm')
custom_nlp.add_pipe(set_custom_boundaries, before='parser')
custom_ellipsis_doc = custom_nlp(ellipsis_text)
custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)
for sentence in custom_ellipsis_sentences:
    print(sentence)

#Część 5
# Podstawową jednostką wyrażenia w Spacy jest token. Możemy wylistować sobie tokeny(jednostki) z każdego wyrażenia.
# Tokeny posiadają mnóstwo parametrów które pochodzą z klasy Token które możemy wylistować i na ich podstawie wykonywać dalsze operacje
# Parametry takie jak np is_space - czy token jest spacją, is_punct - czy jest znakiem interpunkcyjnym, idx - poczatkowy numer indeksu w tekscie.
for token in about_doc:
    print (token, token.idx, token.text_with_ws,
           token.is_alpha, token.is_punct, token.is_space,
           token.shape_, token.is_stop)

#Część 6
# Tutaj wylistowaliśmy 10 tak zwanych STOP WORDS(Słowa nie posiadające znaczenia same w sobie - mają zazwyczaj sens zestawione z innymi)
spacy_stopwords = spacy.lang.pl.stop_words.STOP_WORDS
len(spacy_stopwords)
for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)
# Możemy na przykład usunąć wszystkie STOP WORDSy z naszego wcześniej wprowadzonego tekstu
for token in about_doc:
    if not token.is_stop:
        print (token)

#Część 7
# Lemmatization - zamiana słów na formę podstawową wyrazu. Wykonuje się to po to, by wyeliminować odmienione formy wyrazu.
# Spacy posiada metodę lemma_ ktora przekształca wyraz na jego formę podstawową(o ile w takiej się już nie znajduję)
# Przykład poniżej listuje z ciągu tekstowego każdy z wyrazów oraz obok wyświetla jego formę podstawową.
conference_help_text = ('Przykładowe zdanie. Nie mam pomysłu co tutaj napisać więc napiszę, '
                        'że na moim biurku stoją właśnie dwa puste kubki i muszę włożyć je do zmywarki bądź umyć.')
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    print (token, token.lemma_)

#Część 8
# Dalsza analiza tekstu - zliczanie najczęściej występujących słów oraz wyświetlenie unikalnych słów
complete_text = ('Stojący, obok wejścia na przebudowany obiekt sportowy, stary pawilon, mieszczący kiedyś kasy i szatnie kąpieliska, dzisiaj wygląda fatalnie. Wręcz psuje efekt nowego stadionu Legii. Rozpadająca się konstrukcja, bohomazy i hasła wypisane na ścianach, '
                 'robią bardzo złe wrażenie. Dopiero na przełomie marca i kwietnia zdecydowano o rozbiórce. Tak, jakby nikt wcześniej tego starego budynku nie dostrzegał. Potem była niezbędna inwentaryzacja, '
                 'a teraz nie ma środków na wykonanie rozbiórki. Nikt nie zaplanował tej pozycji w budżecie.7 sierpnia na stadionie Legii odbędzie się otwarcie obiektu i prestiżowy mecz Legii z Arsenalem Londyn.'
                 ' We wrześniu zagoszczą uczestnicy Europejskich letnich Igrzysk Olimpiad Specjalnych. Czy zobaczą również szpecące pozostałości z dawnych lat.')
complete_doc = nlp(complete_text)
# Usunięcie wszystkich tak zwanych STOP WORDS aby nie brać ich pod uwage przy analizie
words = [token.text for token in complete_doc
         if not token.is_stop and not token.is_punct]
# Wyświetlenie pięciu najczęściej występujących słów w tekście wraz z ilością ich wystąpień
word_freq = Counter(words)
common_words = word_freq.most_common(5)
print (common_words)
# Wyświetlenie wszystkich unikalnych słów w tekście
unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
print (unique_words)

#Część 9
# Części mowy
# Spacy umożliwia nam rozróżnienie z tekstu jaką część mowy reprezentuje konkretny wyraz.
# W przykładzie poniżej najpierw listujemy dla każdego słowa jaką część mowy reprezentuje a następnie grupujemy z tekstu wszystkie
# Rzeczowniki oraz przymiotniki po czym je wyświetlamy
for token in about_doc:
    print (token, token.tag_, token.pos_, spacy.explain(token.tag_))

nouns = []
adjectives = []
for token in about_doc:
    if token.pos_ == 'NOUN':
        nouns.append(token)
    if token.pos_ == 'ADJ':
        adjectives.append(token)

print(nouns)
print(adjectives)


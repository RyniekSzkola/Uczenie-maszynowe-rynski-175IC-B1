import spacy
from spacy import displacy

# Wczytanie modelu języka polskiego
nlp = spacy.load("pl_core_news_sm")

# Przykładowy tekst
complete_text = ('Stojący, obok wejścia na przebudowany obiekt sportowy, stary pawilon, mieszczący kiedyś kasy i szatnie kąpieliska, dzisiaj wygląda fatalnie. Wręcz psuje efekt nowego stadionu Legii. Rozpadająca się konstrukcja, bohomazy i hasła wypisane na ścianach, '
                 'robią bardzo złe wrażenie. Dopiero na przełomie marca i kwietnia zdecydowano o rozbiórce. Tak, jakby nikt wcześniej tego starego budynku nie dostrzegał. Potem była niezbędna inwentaryzacja, '
                 'a teraz nie ma środków na wykonanie rozbiórki. Nikt nie zaplanował tej pozycji w budżecie.7 sierpnia na stadionie Legii odbędzie się otwarcie obiektu i prestiżowy mecz Legii z Arsenalem Londyn.'
                 ' We wrześniu zagoszczą uczestnicy Europejskich letnich Igrzysk Olimpiad Specjalnych. Czy zobaczą również szpecące pozostałości z dawnych lat.')
complete_doc = nlp(complete_text)

#Część 10
# Wizualizator zależności - displaCy
# Narzędzie z biblioteki które w sposób graficzny wyświetla zależności pomiędzy słowami
about_interest_text = ('On jest zainteresowany w nauce przetwarzania języka naturalnego.')
about_interest_doc = nlp(about_interest_text)
#displacy.serve(about_interest_doc, style='dep')

#Część 11
# Funkcje preprocesora
# Spacy udostępnia funkcje które mogą wpływać na cały wprowadzony tekst. Możemy między innymi przekonwertować go do małych liter,
# Zamienić słowa na formę podstawową, usuwać znaki interpunkcyjne czy usuwać STOP WORDS. Poniżej kilka funkcji:
# Sprawdzenie czy token jest znakiem stop badz znakiem interpunkcyjnym
def is_token_allowed(token):
    if (not token or not token.string.strip() or
        token.is_stop or token.is_punct):
        return False
    return True

# Konwersja tokenu do małych liter
def preprocess_token(token):
    return token.lemma_.strip().lower()

# Przetwarzenie tekstu wejściowego na podstawie dwóch powyższych metod
complete_filtered_tokens = [preprocess_token(token)
    for token in complete_doc if is_token_allowed(token)]

print(complete_filtered_tokens)

#Cześć 12
# Spacy umożliwia nam analizowanie tekstu. Możemy sprawdzać relacje pomiędzy słowami oraz zależności pomiędzy nimi.
piano_text = 'Michał uczy się grać na pianinie'
piano_doc = nlp(piano_text)
for token in piano_doc:
    print (token.text, token.tag_, token.head.text, token.dep_)

#Część 13
# Nawigowanie po drzewie zależności. Spacey udostępnia takie metody jak children, lefts, rights, subtree które pozwalają nawigować po drzewie.
one_line_about_text = ('Michal Rynski jest programistą Java obecnie pracującym dla gdańskiej firmy programistycznej.')
one_line_about_doc = nlp(one_line_about_text)
print([token.text for token in one_line_about_doc[5].children])
print (one_line_about_doc[4].nbor(-1))
print (one_line_about_doc[4].nbor())
print([token.text for token in one_line_about_doc[5].lefts])
print([token.text for token in one_line_about_doc[5].rights])
print (list(one_line_about_doc[4].subtree))

#Część 14
# Shallow Parsing
# Polega na wyodrębnianiu pewnych struktur językowych z tekstu jak na przykład fraza nominalna.
conference_text = ('Michal Rynski jest programistą Java obecnie pracującym dla gdańskiej firmy programistycznej.')
conference_doc = nlp(conference_text)
for chunk in conference_doc.noun_chunks:
    print (chunk)

#Cześć 15
# Named Entity Recognition jest procesem lokalizowania nazw własnych takich jak nazwy osób, nazwy budynków , walut czy wyrażeń czasu.
# Biblioteka jeżeli rozpozna jakąś nazwę własną to jest w stanie przekazać o niej ogólne dane - czym jest.
piano_class_text = ('The Taj Mahal Palace, Mumbai to słynny hotel zbudowany w 1903 roku, położony naprzeciwko Bramy Indii. Roztacza się z niego widok na Morze Arabskie.')
piano_class_doc = nlp(piano_class_text)
for ent in piano_class_doc.ents:
    print(ent.text, ent.start_char, ent.end_char,
          ent.label_, spacy.explain(ent.label_))

# Udogodnienie to może być pomocne na przykład po to, aby automatycznie wykryć w tekście dane personalne takie jakie imię i nazwisko a następnie zamienić je jakąś inną treścią.
# Przykład tego znajduje się poniżej
survey_text = ('Najpopularniejsze polskie imiona to Michał, Anna a także Julia')
def replace_person_names(token):
    if token.ent_iob != 0 and token.ent_type_ == 'PERSON':
        return '[REDACTED] '
    return token.string

def redact_names(nlp_doc):
    for ent in nlp_doc.ents:
        ent.merge()
    tokens = map(replace_person_names, nlp_doc)
    return ''.join(tokens)

survey_doc = nlp(survey_text)
print(redact_names(survey_doc))


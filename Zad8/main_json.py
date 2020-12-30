import json
import requests

#Zapisanie danych do zmiennej w postaci JSON = serializacja
data = {
    "student": {
        "name": "Michal Rynski",
        "group": "175IC_B1"
    }
}

#Zapisanie obiektu data do pliku o rozszerzeniu .json
with open("data_json.json", "w") as write_file:
    json.dump(data, write_file)

data_json = json.dumps(data)
print(data_json)

#Dodanie wycięć przy wyświetlaniu JSONa
data_json_indent = json.dumps(data, indent=2)
print(data_json_indent)

#Wczytanie jsona z pliku i zapisanie do zmiennej
with open("do_wczytania.json", "r") as read_file:
    data = json.load(read_file)

print(data)

#Pobranie jsona przez metode webowa(GET) i zapisanie do zmiennej
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = json.loads(response.text)
print(posts)

#Znalezienie najdłuższego posta dla każdego usera, posortowanie oraz wyświetlenie wyniku
posts_by_user={}
for post in posts:
    try:
        if len(post["body"])> posts_by_user[post["userId"]]:
            posts_by_user[post["userId"]]=len(post["body"])
    except KeyError:
            posts_by_user[post["userId"]]=len(post["body"])

longest_post = sorted(posts_by_user.items(),
                      key=lambda x:x[1], reverse=True)
print(longest_post)

#Wyszukanie z stworzonej wyżej tablicy użytkownika o najdłuzszym poście i wyświetlenie jego id
users_longest_posts=[]
for longest in longest_post:
    if longest_post[0][1]>longest[1]:
        break
    users_longest_posts.append(str(longest[0]))
print((users_longest_posts))

#Utworzenie niestandardowej klasy Elf
class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]

#Próba serializacji obiektu tej klasy nie powiodła się ponieważ moduł JSON nie wspiera tego typu operacji
try:
    elf = Elf(level=4)
    json.dumps(elf)
except TypeError as type_error:
    print("A TypeError has occurred!")
    print("Message: ",type_error.args[0])

#W celu zakodowania niestandardowego obiektu do formatu JSON należy utworzyć odpowiednią metodę
def encode_complex(z):
    if isinstance(z,complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

print(json.dumps(9+5j,default=encode_complex))
print("========")

#Złożone niestandardowe obiekty możemy kodować poprzez stworzenie klasy dziedziczącej po JSONEncoder i nadpisanie metody default
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)

print(json.dumps(2 + 5j, cls=ComplexEncoder))
encode = ComplexEncoder()
print(encode.encode(3 + 6j))

#Odkodowanie niestandardowego obiektu
complex_json = json.dumps(4+17J,cls=ComplexEncoder)
print(json.loads(complex_json))

#Dekodowanie klucza - definicja oraz odkodowanie
def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct

with open("complex_data.json") as complex_data:
     data = complex_data.read()
     z = json.loads(data, object_hook=decode_complex)

print(z)
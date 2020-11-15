import imutils
import cv2

#Funkcja 1
# Ładujemy obraz do zmiennej image za pomocą metody imread
# Metodą shape wydobywamy szserokość, wysokość oraz głębokość obrazu
image = cv2.imread("harry.jpg")
(h, w, d) = image.shape
#print("width={}, height={}, depth={}".format(w, h, d))
# Metodą imshow wyświetlamy obraz który znajduje się w zmiennej image, a także dajemy mu nazwę okienka w którym się wyświetli
cv2.imshow("Zdjecie", image)
# Metoda waitKey zapobiega zamknięcia się obrazku od razu po wyświetleniu
cv2.waitKey(0)

#Funkcja 2
# Pobieranie pojedyńczych pixeli
# Wyświetlenie wartości pixela w formacie RGB o parametrach x=50, y=50
(B, G, R) = image[50, 50]
#print("R={}, G={}, B={}".format(R, G, B))

#Funkcja 3 - Przycinanie obrazka
# ROI - Region of interest
# Wycinanie obszaru z obrazka rozpoczynając od pola x=220 y=40, kończąc na polu x=320, y=140
roi = image[40:140, 220:320]
cv2.imshow("Region of interest", roi)
cv2.waitKey(0)

#Funkcja 4
# Zmiana rozmiaru obrazka na 300x300 bez uwzględnienia aspect ratio przez co zdjęcie jest zniekształcone
resized = cv2.resize(image, (300, 300))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

#Funkcja 5
# Zmiana rozmiaru obrazka na szerokość równą 300 lecz wysokością bazującą na aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)

#Funkcja 6
# Zmiana rozmiaru obrazka za pomocą biblioteki imutils.
# Wystarczy podać samą szerokość lub wysokość, a obrazek skaluje się automatycznie.
resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)

#Funkcja 7
# Funkcje obracające obrazek. Należy jako pierwsze wyliczyć środek obrazka, a następnie za pomocą metody getRotationMatrix2D
# możemy obracać zdjęcie o wybraną ilość stopni
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)

#Funkcja 8
# Ta sama funkcjonalność co powyżej lecz ponownie z wykorzystaniem biblioteki imutils i jej metody rotate
# Metoda rotate automatycznie wylicza centrum a od użytkownika wymaga jedynie podania ilości stopni obrotu zdjęcia
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

#Funkcja 9
# Za pomocą metody rotate_bound możemy obrócić zdjęcie a dodatkowo wyeliminować ucięcię
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

#Funkcja 10
# Aby ułatwić pracę algorytmom przetwarzającym obrazy dobrze jest zredukować zakłócenia nakładające rozmazanie.
# Do tego celu używa się metody GaussianBlue w której jako parametr możemy ustalić poziom rozmazania.
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

#Funkcja 11
# Metoda rectangle umożliwia rysowanie prostokątów na obrazach.
# W parametrach metody należy podać wartości pixeli początkowych oraz końcowych, kolor oraz grubość lini.
output = image.copy()
cv2.rectangle(output, (260, 35), (383, 167), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

#Funkcja 12
# Metoda circle - analogicznie z tym że rysujemy okrąg. Zamiast wartości pixeli początkowego i końcowego
# Podajemy środek okręgu oraz jego promień
output = image.copy()
cv2.circle(output, (315, 130), 65, (255, 0, 0), 2)
cv2.imshow("Circle", output)
cv2.waitKey(0)

#Funkcja 13
# Metoda line rysuje linie prostą. Podajemy wartość pixela początkowego oraz końcowego, reszta parametrów tak jak powyżej.
output = image.copy()
cv2.line(output, (150, 20), (550, 220), (255, 0, 0), 2)
cv2.imshow("Line", output)
cv2.waitKey(0)

#Funkcja 14
# W celu pisania tekstu po obrazku używa się metody putText
# Mamy kilka parametrów jakie przyjmuje metoda między innymi treść tekstu, wartość pixela startowego tekstu, rozmiar, kolor czy font ścieżki.
output = image.copy()
cv2.putText(output, "Harry, Hermiona i Ron", (110, 60),
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)

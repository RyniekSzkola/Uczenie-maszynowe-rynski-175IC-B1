import argparse
import imutils
import cv2

# Dodanie dodatkowych informacji do programu przy starcie
# Parametr -i/--image ustawiliśmy za pomocą IDE
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Scieżka do pliku")
args = vars(ap.parse_args())

# Wczytanie obrazka lini komend
image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)

#Funkcja 1
# Metoda cvtColor konwertuje obraz na skalę szarości
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

#Funkcja 2
# Metoda Canny z biblioteki openCV umożliwia nam detekcję krawędzi obrazka
# Należy wpierw przekonwertować obrazek na skalę szarości jak zrobiliśmy to powyżej
edged = cv2.Canny(gray, 30, 150)
cv2.imshow("Edged", edged)
cv2.waitKey(0)

#Funkcja 3
# Thresholding umożliwia nam zamianę wszystkich kolorów  poniżej jakiejś wartości na jeden konkretny
# Służy do tego metoda threshold
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

#Funkcja 4
# OpenCV udostępnia nam mechanizm wykrywania i rysowania konturów obiektów
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()
# Pętla drukująca każdy znaleziony kontur
for c in cnts:
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
    cv2.imshow("Contours", output)
    cv2.waitKey(0)
# Funkcja zliczająca każdy kontur oraz wyświetlająca tekst o liczbe znalezionych konturów
text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)

#Funkcja 5
# Erozja wykorzystywana jest do zmniejszania jasnych obszarów oraz likwidacji wypukłości
# Wykorzystuje się do tego metode erode z biblioteki OpenCV
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)
# Dylatacja z kolei powoduje rozszerzenie jasnych obszarów oraz wypełnianie zagłębień
# Możliwe jest to dzięki metodzie dilate
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilated", mask)
cv2.waitKey(0)

#Funkcja 6
# Za pomocą maskowania możemy schować pewien fragment zdjęcia i wykluczyć go z dalszej analizy, obróbki
mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Output - Bitwise", output)
cv2.waitKey(0)
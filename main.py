import numpy as np
from moviepy.editor import *

# mamy 259_200 znaków
# jedna strona w wordzie średnie marginesy, 10, to 3889 znaków. 36288 bitów
# możemy zapisać na jedynm zdjęciu w jakiści full_HD 66,65 takich stron. nieźle hull hd 1920 x 1080
# Otwórz plik tekstowy do odczytu. a=01100001
#
# wejścia:
# Plik wejściowy
# rozmiar ( w sensie wymiar)
# ilość klatek na sekundę
# dorobić szyfrowanie danch, jeśli by jednak tak by się dało to zrobić, bo tu jest jakaś zbyt duża optymalizacja i rozmycie F

def binarnie():
    with open('kot.jpeg', 'rb') as file:
        hex_data = file.read()
        binary = ''
        bits_array = []
        for b in hex_data:
            # zamieniamy bajt na postać binarną i formatujemy wynik w postaci 8 bitów
            binary_string = format(b, '08b')
            binary = binary + binary_string

        for b in binary:
            bits_array.append(int(b))

    return bits_array

def hexalnie():
    with open('kot.jpeg', 'rb') as file:
        return [int(b) for b in file.read()]
"""""
# Otwarcie pliku w trybie binarnym z zapisem
with open(filename, 'wb') as f:
    # Zapisanie danych binarnych do pliku
    f.write(binary_data)
"""





"""
 def video(width, height, my_fps, name, data):
 ilosc dostepnych pixeli
my_duration = (ilosc_danych // (width*height*my_fps))+1  # bo robimy podłogę, +1 musimy dodać aby się wszystkie zmieściły
print("dlugosc to: ")
print(my_duration)
"""


width = 100
height = 100
# Utworzenie białego pola o wymiarach 1920 x 1080
white_clip = ColorClip((width, height), color=(255, 255, 255), duration=9)


dane = hexalnie()
print(len(dane))
# print(dane)
z = 0
# Funkcja zwracająca pojedynczą klatkę filmu
def make_frame(t):
    global z
    # Utworzenie pustej tablicy numpy reprezentującej klatkę 1080, 1920
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    # Ustawienie białego koloru dla całej klatki
    frame[::] = [255, 255, 255]

    for i in range(0, height):
        for j in range(0, width):
            z += 1
            if len(dane):  # jeśli są jeszcze jakieś elementy and dane.pop(0) jeśli binarnie, jeśli nie to:
                #frame[i, j] = [0, 0, 0]
                x = dane.pop(0)
                frame[i, j] = [x, x, x]

    return frame

# Utworzenie klipu z tych klatek
line_clip = VideoClip(make_frame, duration=9)

# Sklejenie klipów i zapis do pliku
final_clip = CompositeVideoClip([white_clip, line_clip])
final_clip.write_videofile("random_liczby.mp4", fps=1, audio=False, codec='mpeg4')

print(z)

def dekodowanie():
    clip = VideoFileClip("random_liczby.mp4")
    # showing frame at 2 second
    #clip.show(2, interactive=True)

    for frame in clip.iter_frames():
        print(frame)
        r, g, b = frame[1, 1]
        print(r, g, b)

# dekodowanie()




























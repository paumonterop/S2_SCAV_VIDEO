import os


def exer1():
    os.system('ffmpeg -i bbb.mp4 -ss 00:05:00 -t 00:00:10 bbb_10s.mp4')


def exer2():
    os.system('ffmpeg -i bbb_10s.mp4 -vf "split=2[a][b], [b] histogram, format=yuva444p[hh], '
              '[a][hh]overlay" bbb_histogram.mp4')


def exer3():
    print("Quin canvi de resolució vols aplicar:")
    print("\t 1. 720p")
    print("\t 2. 480p")
    print("\t 3. 360p")
    print("\t 4. 160x120p")
    resize = input("Escull l'opció: ")

    if resize == '1':
        os.system('ffmpeg -i bbb_10s.mp4 -vf scale=-1:720 bbb_720.mp4')
    elif resize == '2':
        os.system('ffmpeg -i bbb_10s.mp4 -vf scale=-1:480 bbb_480.mp4')
    elif resize == '3':
        os.system('ffmpeg -i bbb_10s.mp4 -vf scale=-1:360 bbb_360.mp4')
    elif resize == '4':
        os.system('ffmpeg -i bbb_10s.mp4 -vf scale=160:120  bbb_120.mp4')
    else:
        print("Aquesta opció no existeix. Tornar a introduir l'opció")
        exer3()


def exer4():
    print("Seleccionna l'opció:")
    print('\n')
    print("\t1. Saber quin codec té  el video original")
    print("\t2. Convertir l'àudio del video a MONO i a MP3")
    exer4_input = input("Escull l'opció: ")

    if exer4_input == '1':
        os.system('ffmpeg -i bbb_10s.mp4 -c codec')
    elif exer4_input == '2':
        os.system('ffmpeg -i bbb_10s.mp4 -ac 1 -acodec mp3 bbb_mp3.mp4')
    else:
        print("Aquesta opció no existeix. Tornar a introduir l'opció")
        exer4()


def index():
    print('---- SEMINARI 2 ----')
    print('\n')
    print("Seleccioneu l'exercici que voleu processar:")
    print('\n')
    print('\t 1. Exercici 1: Tallar 10 segons del BBB video.')
    print("\t 2. Exercici 2: Crear un nou video amb l'histograma YUV del video"
          "de Exercici 1.")
    print("\t 3. Exercici 3: Canviar la resolució del video.")
    print("\t 4. Exercici 4: Canviar l'audio a mono i a una altre codec.")
    print('\n')
    option = input("Escolliu l'exercici: ")
    return option


def switch(exer):

    print(exer)

    if exer == '1':
        exer1()
    elif exer == '2':
        exer2()
    elif exer == '3':
        exer3()
    elif exer == '4':
        exer4()
    else:
        print("Aquesta opció no existeix. Torna a seleccionar l'exercici (1, 2 ,3, 4):")
        index()

# -------------- MAIN ---------------------


exer = index()

switch(exer)

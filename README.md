# S2_SCAV_VIDEO
Semianri 2 - SCAV_VIDEO

**Exercici 1.**

Per fer aquest primer exercici que consistia en tallar 10 segons del video Big Buck Bunny (bbb.mp4). Hem utilitzat el comando següent:
Exactament tallem el video del minut 5 al 5:10. Al comando li pasem el video input, el temps d'inici del tall, la duració i la sortida de l'arxiu.

*ffmpeg -i bbb.mp4 -ss 00:05:00 -t 00:00:10 bbb_10s.mp4*

A continuació podem veure una captura de l'execucció del comando al terminal:

![ScreenShot E1](https://github.com/paumonterop/S2_SCAV_VIDEO/tree/main/Imatges/E1_screenshot.png?raw=true)

I el video retallat 10 segons:

![BBB 10s](https://github.com/paumonterop/S2_SCAV_VIDEO/tree/main/Imatges/bbb_10s.mp4?raw=true)

**Exercici 2.**

El comando que hem utilitzat per dur a terme aquest segon exercici és el següent:

ffmpeg -i bbb_10s.mp4 -vf "split=2[a][b], [b] histogram, format=yuva444p[hh], [a][hh]overlay" bbb_histogram.mp4

**Exercici 3.**

*ffmpeg -i bbb_10s.mp4 -vf scale=-1:720 bbb_720.mp4*
*ffmpeg -i bbb_10s.mp4 -vf scale=-1:480 bbb_480.mp4*

**Exerici 4.**

Per saber el codec que porta l'audio del video original:

ffmpeg -i bbb.mp4 -c codec

Passar a mono i a wav

*ffmpeg -i bbb_10s.mp4 -ac 1 -acodec mp3 bbb_mp3.mp4*



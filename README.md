# S2_SCAV_VIDEO
Semianri 2 - SCAV_VIDEO

A l'script *S2_MAIN.py* hi ha tot el codi integrat per tal de poder executar cada exercici independentment i de forma interactiva amb el terminal.

**Exercici 1.**

Per fer aquest primer exercici que consistia en tallar 10 segons del video Big Buck Bunny (bbb.mp4). Hem utilitzat el comando següent:
Exactament tallem el video del minut 5 al 5:10. Al comando li pasem el video input, el temps d'inici del tall, la duració i la sortida de l'arxiu.

*ffmpeg -i bbb.mp4 -ss 00:05:00 -t 00:00:10 bbb_10s.mp4*

A continuació podem veure una captura de l'execucció del comando al terminal:

![ScreenShot E1](https://github.com/paumonterop/S2_SCAV_VIDEO/tree/main/Imatges/E1_screenshot.png?raw=true)

**Exercici 2.**

El comando que hem utilitzat per dur a terme aquest segon exercici és el següent:

ffmpeg -i bbb_10s.mp4 -vf "split=2[a][b], [b] histogram, format=yuva444p[hh], [a][hh]overlay" bbb_histogram.mp4

![ScreenShot E2](https://github.com/paumonterop/S2_SCAV_VIDEO/tree/main/Imatges/E2_screenshot.png?raw=true)

**Exercici 3.**

Per cambiar la resolució del video BBB de 10 segons hem fet servir el comando segunet, on a **RESOLUCIO** se li assigna la resolució de sortida.

*ffmpeg -i bbb_10s.mp4 -vf scale=-1:**RESOLUCIO** bbb_resized.mp4*

![ScreenShot E3](https://github.com/paumonterop/S2_SCAV_VIDEO/tree/main/Imatges/E3_screenshot.png?raw=true)

**Exerici 4.**

Per saber el codec que porta l'audio del video original:

ffmpeg -i bbb.mp4 -c codec

Passar a mono i a mp3. En el parametre *-ac* se li assigna el numero de canals de sortida i en paramentre *-acodec* el nou codec d'audio de sortida.

*ffmpeg -i bbb_10s.mp4 -ac 1 -acodec mp3 bbb_mp3.mp4*

![ScreenShot E4- MONO i MP3](https://github.com/paumonterop/S2_SCAV_VIDEO/tree/main/Imatges/E4_screenshot.png?raw=true)



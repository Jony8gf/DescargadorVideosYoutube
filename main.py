# Este proyecto permite las descarga de videos de Youtube

# Para instalar PYTUBE, instala esta línea en tu consola/Terminal:
#  pip install pytube
from pytube import YouTube

#Le indicamos por teclado la url del video que deseamos
yt = (YouTube) (input("Dime el url de video de Youtube:"))
#Atributos iteresantes
#Title nos indica el nombre del video
print(yt.title)
#Autor nos indica el canal del Youtube de donde procede dicho video
print(yt.author)
#Length nos indica el tiempo total en segundos
print(yt.length)

#Descargar el video, y con la funcion de Highest_Resolution
#Para que este en buena calidad videografica
yt.streams.get_highest_resolution().download()



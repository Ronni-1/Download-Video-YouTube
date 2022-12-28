from pytube import YouTube
#ссылка покоторой происходит скачивание видео
yt = YouTube("https://www.youtube.com/watch?v=hDEqiJK8b-A")

#Параметры видео
print("Наименование видео: ",yt.title)
print("Количество просмотров видео: ",yt.views)
print("Длина видео: ",yt.length) #Длина времени в секундах


#Скачиваем максимально возможное разрешение
ys = yt.streams.get_highest_resolution()

#Печатает слово Загрузка начинается
print("Начинается загрузка видео...")
#Происходит загрузка видео и сохранение по указанному пути
ys.download("/home/Sergei/PycharmProjects/pythonProject/Download_inet")
#Выводит слово Закгрузка завершена после того как видео загрузилось
print("---ЗАГРУЗКА ЗАВЕРШЕНА---")
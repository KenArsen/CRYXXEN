import youtube_dl
from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_music_email_task(recipient_list, message):
    # Отправляет электронное письмо, когда форма обратной связи была отправлена.

    # download music
    music_info = youtube_dl.YoutubeDL().extract_info(url=message, download=False)
    musicname = f"{music_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': musicname,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([music_info['webpage_url']])
    ans = "Загрузка завершена... {}".format(musicname)

    send_mail(
        "Hello",
        "\t" + ans + "\n\n\t" + message + "\n\nСпасибо!",
        "kenjegulov2002@gmail.com",
        [recipient_list],
        fail_silently=False,
    )

import yt_dlp
import os

def process_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': 'input.mp4',
        'cookiefile': 'cookies.txt', # دابا غيلقى الملف واجد فالبلاصة
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    os.system("ffmpeg -i input.mp4 -ss 00:00:10 -t 30 -c copy output_short.mp4")

process_video("https://www.youtube.com/watch?v=Rb5L_kagUZ4")

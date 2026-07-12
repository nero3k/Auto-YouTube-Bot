import yt_dlp
import os

# هاد الـ User-Agent هو "الدرع" اللي غايخلي يوتيوب يتيق فالبوت
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': 'input.mp4',
        'quiet': False,
        'user_agent': user_agent,
        'referer': 'https://www.google.com/', # كنبينو بلي جينا من Google
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # التقطاع بـ ffmpeg
    os.system("ffmpeg -i input.mp4 -ss 00:00:10 -t 30 -c copy output_short.mp4")

# جرب هاد الرابط (ملاحظة: إذا عطاك 403، بدل الرابط بواحد آخر)
download_video("https://www.youtube.com/watch?v=Rb5L_kagUZ4")

import yt_dlp
import os

# هاد السطر كيعطي للبوت بصمة ديال متصفح Chrome حقيقي
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'

def process_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': 'input.mp4',
        'cookiefile': 'cookies.txt', 
        'user_agent': user_agent,     # هادي هي اللي كتقلد المتصفح ديالك
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # التقطاع ديال الفيديو (من ثانية 10، لمدة 30 ثانية)
    os.system("ffmpeg -i input.mp4 -ss 00:00:10 -t 30 -c copy output_short.mp4")

process_video("https://www.youtube.com/watch?v=Rb5L_kagUZ4")

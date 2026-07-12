import yt_dlp
import os

def download_video(url):
    # هاد الخيارات كتقول لـ yt-dlp يخدم بحال إيلا هو متصفح Chrome
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': 'input.mp4',
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'referer': 'https://www.youtube.com/',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # التقطاع
    os.system("ffmpeg -i input.mp4 -ss 00:00:10 -t 30 -c copy output_short.mp4")

download_video("https://www.youtube.com/watch?v=Rb5L_kagUZ4")

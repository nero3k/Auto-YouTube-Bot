import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# الرابط التجريبي
download_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'quiet': False,
        'no_warnings': False,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

download_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

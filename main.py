import yt_dlp

def scrape_channel_shorts(channel_url):
    ydl_opts = {
        'quiet': False,
        'extract_flat': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"جاري البحث في: {channel_url}")
            # كنضيفو /shorts باش يوتيوب تعطينا غير الفيديوهات القصيرة
            info = ydl.extract_info(channel_url + "/shorts", download=False)
            
            for video in info.get('entries', []):
                print(f"Title: {video.get('title')}")
                print(f"URL: https://www.youtube.com/watch?v={video.get('id')}")
                print("-" * 30)
        except Exception as e:
            print(f"وقع خطأ: {e}")

# الرابط ديال القناة اللي عطيتيني
scrape_channel_shorts("https://youtube.com/@swi-n2o")

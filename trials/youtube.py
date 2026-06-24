from yt_dlp import YoutubeDL

link = input("Link : ")

ydl_opts = {
    'noplaylist': True,
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    },
    'extractor_args': {
        'youtube': {
            'player_client': ['android', 'web'],
            'skip': ['dash', 'hls']
        }
    },
}

with YoutubeDL(ydl_opts) as ydl:
    yt = ydl.extract_info(link, download=False)

print("Title: ", yt.get('title'))
print("Author: ", yt.get('uploader'))
print("Published date: ", yt.get('upload_date'))
print("Number of views: ", yt.get('view_count'))
print("Length of video: ", yt.get('duration'), "seconds")
print("Point: ", yt.get('like_count'))
print("Description: ", yt.get('description', '')[:100] + "...")

print("Video downloading...")
ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'

try:
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
except Exception as e:
    print(f"Bir hata oluştu: {e}")

print("Video successfully downloaded from", link)

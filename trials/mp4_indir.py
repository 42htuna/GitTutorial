import argparse
from yt_dlp import YoutubeDL

def mp4_indir(video_url):
    ydl_opts = {
        'noplaylist': True,
        
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': 'mp4/%(title)s.mp4',
        
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
    
    try:
        print(f"\n[Başlatıldı] Video indiriliyor: {video_url}\n")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("\n[BAŞARILI] MP4 videosu klasörünüze kaydedildi!")
        
    except Exception as e:
        print("\nBir hata meydana geldi:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube MP4 İndirme Programı")
    parser.add_argument('--link', '-l', type=str, required=True, help='İndirilecek YouTube video bağlantısı')
    args = parser.parse_args()
    
    mp4_indir(args.link)

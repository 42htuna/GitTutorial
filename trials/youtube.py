from pytube import YouTube

link = input("Link : ")
yt = YouTube(link)

#Showing details
print("Title: ", yt.title)
print("Author: ", yt.author)
print("Published date: ", yt.publish_date.strftime("%Y-%m-%d"))
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, "seconds")
print("Point: ",yt.rating)
print("Description: ", yt.description)

#print all the available streams
for stream in yt.streams:
      print(stream)

#print filtered streams
#print(yt.streams.filter(only_audio=True))
#print(yt.streams.filter(only_video=True))

#download video only
#yt.streams.filter(res='1080p', progressive=False).first().download(filename='video.mp4')

#download audio only
#yt.streams.filter(abr='160kbps', progressive=False).first().download(filename='audio.mp3')

#download filtered stream
#yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

#download first stream to a folder
#video = yt.streams.first()
#video.download("/home/<USER>/Downloads")

yt.streams.filter(abr='160kbps', progressive=False).first().download(filename=yt.title+'.m3u')
print("Audio downloading...")
video = yt.streams.get_highest_resolution()
print("Video downloading...")
video.download()
print("Video successfullly downloaded from", link)

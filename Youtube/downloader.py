from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=K-yhef6ZqOw')
print(yt.get_videos())
video = yt.get('mp4', '720p')
video.download('video')

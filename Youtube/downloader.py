from pytube import YouTube
import subprocess
yt = YouTube('https://www.youtube.com/watch?v=lQ6-nCLeDsI')
print(yt.get_videos())
video = yt.get('mp4', '720p')
video.download('video')
print('starting audio extraction....')
subprocess.call('C:\\ffmpeg-20170221-a5c1c7a-win64-static\\bin\\ffmpeg -i "{}.mp4" -vn -c:a copy {}_soundtrack.m4a'.format(yt.filename,yt.filename))


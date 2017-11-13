from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=HZTgmC0Pmb8')
print(yt.get_videos())

video = yt.get('mp4', '{}p'.format(input('resolution: ')))
video.download('video')
# print('starting audio extraction....')
# subprocess.call('C:\\ffmpeg-20170221-a5c1c7a-win64-static\\bin\\ffmpeg -i "{}.mp4" -vn -c:a copy {}_soundtrack.m4a'.format(yt.filename,yt.filename))


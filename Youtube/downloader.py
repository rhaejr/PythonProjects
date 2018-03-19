from pytube import YouTube

videos = ['https://www.youtube.com/watch?v=8OnitO8wS6A',
          'https://www.youtube.com/watch?v=Nex2B7yFxYs',
          'https://www.youtube.com/watch?v=aZyUO5shXZg',
          'https://www.youtube.com/watch?v=1fhdHPBqUa8']

for i in videos:
    try:
        YouTube(i).streams.first().download()
        print('Finished')
    except Exception as e:
        print(e)

# yt = YouTube('https://www.youtube.com/watch?v=HZTgmC0Pmb8')
# print(yt.get_videos())
#
# video = yt.get('mp4', '{}p'.format(input('resolution: ')))
# video.download('video')
# print('starting audio extraction....')
# subprocess.call('C:\\ffmpeg-20170221-a5c1c7a-win64-static\\bin\\ffmpeg -i "{}.mp4" -vn -c:a copy {}_soundtrack.m4a'.format(yt.filename,yt.filename))


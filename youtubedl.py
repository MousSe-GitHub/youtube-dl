from pytube import YouTube
from pytube import Playlist
import os
import getpass

os.system('cls')

url = str(input('playlist/video url: '))

path = str(input('download path: '))
if path == '':
    print('defaulting to C:\\Users\\User\\Downloads\\')
    path = f"C:\\Users\\{getpass.getuser()}\\Downloads\\"

try:
    mp3_convert = int(input('\nFormat\n1 - mp4\n2 - mp3\n?'))
except:
    print('defaulting to mp3')
    mp3_convert = 2



if 'playlist' in url:

    playlist = Playlist(url)
    for i in range(len(playlist)):
        try:
            print(playlist[i]+'\n...')
            YouTube(playlist[i]).streams.filter(only_audio=True).first().download(f"{path}\\{playlist.title}")
            print(f"done {i+1}/{len(playlist)}\n")

        except:
            print(f"Couldnt download {i+1}/{len(playlist)}\n")

    if mp3_convert == 2:
        os.system(f"cd {path}\\{playlist.title} & ren *.mp4 *.mp3")


else:
    print('\n...\n')
    YouTube(url).streams.filter(only_audio=True).first().download(path)
    os.system(f"cd {path} & ren \"{YouTube(url).title}.mp4\" \"{YouTube(url).title}.mp3\"")
    print('done!')

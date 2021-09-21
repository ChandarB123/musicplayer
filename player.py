import os
from pygame import mixer
import time
from mutagen.mp3 import MP3


def find_all_music():
    start = time.time()
    result = []
    paths = ["C:/", "D:/", "E:/"]
    for path  in paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.mp3'):
                    result.append(os.path.join(root, file))
                    if file not in result:
                        print(os.path.join(root, file))
    return result

def my_music():
    start = time.time()
    result = []
    path = os.getcwd() + r'\\Music\\'
    for file in os.listdir(path):
        if file.endswith(".mp3"):
            result.append("Music\\" + file)
    end = time.time()
    print("The result fetched in " + str(end - start))
    return result

def play_music():
    mixer.init()
    v = 0.5
    choose = int(get_audio("Select the location to search for music: \n\t1.Music Folder \n\t2.Throughout the computer\n"))
    if choose == 1:
        music_list = my_music()
    elif choose == 2:
        music_list = find_all_music()
    
    print("The list of music found is", music_list)

    while True:
        for music in music_list:
            try:
                file_name = str(music)
                print("Playing..." + file_name)
                mixer.music.load(file_name)
                mixer.music.set_volume(v)
                mixer.music.play()
                while True:
                    option = input("Enter an option: ").lower()
                    if option == "pause":
                        mixer.music.pause()
                    elif option == "resume":
                        mixer.music.unpause()
                    elif option == "quit":
                        mixer.music.stop()
                        mixer.quit()
                        break
                    elif option == "rewind":
                        mixer.music.rewind()
                    elif option == "next":
                        mixer.music.stop()
                        print("Finshed playing " + file_name)
                        break
                    elif option == "volume up":
                        mixer.music.set_volume((v + 0.1))
                    elif option == "volume down":
                        mixer.music.set_volume((v - 0.1))
                    
            except Exception as e:
                print("Exception " + str(e) + " occured")

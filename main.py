import urllib.request
import re
from pytube import YouTube
from pytube import Playlist
import os

def songs_in_txt():
        with open('hop.txt', 'r') as f:
           songs = f.read().splitlines()
        #    print(songs)
        return songs


def create_param():
        for song_name in songs_in_txt():
                #print(song_name)
                new_song_name = re.sub("\s","+",song_name)
                #print(new_song_name)
                try:
                    wee_is_searching(new_song_name)
                    delete_downloaded_song()
                except:
                    print(new_song_name+" not found")

def wee_is_searching(search_parameter):
                
                test_search = "https://www.youtube.com/results?search_query=drake+lemon+pepper+freestyle"
                thee_search = "https://www.youtube.com/results?search_query="+search_parameter
                html = urllib.request.urlopen(thee_search)
                decoded_kinda = html.read().decode()

                all_songs_found = re.findall(r"watch\?v=(\S{11})" , decoded_kinda)

                #print(all_songs_found)

                thee_link = "https://www.youtube.com/watch?v="+all_songs_found[0]

                # print(thee_link)
                downloader_mp3(thee_link)


def downloader_mp3(song_id):
            
            yt = YouTube(str(song_id))
            video = yt.streams.filter(only_audio=True).first()
            destination = '.'
            out_file = video.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(yt.title + " has been successfully downloaded.")


def delete_downloaded_song():
        with open("hop.txt", 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[1:])            

create_param()
print("Execution Complete master")
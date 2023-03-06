import urllib.request
import re
from pytube import YouTube
import os

"""
This is what I do:
I work with a txt file to download a song from the list and the kick the downloaded 
song from that list

"""


def songs_in_txt():
        with open('hop.txt', 'r') as f:
           songs = f.read().splitlines()
        #    print(songs)
        return songs


def create_param():
        for song_name in songs_in_txt():
                #print(song_name)
                song_name = refine_name_first(song_name)
                # print(song_name)
                new_song_name = re.sub("\s","+",song_name)
                #print(new_song_name)
                try:
                    wee_is_searching(new_song_name)
                    delete_downloaded_song()
                except Exception as e:
                    print(new_song_name+" not found: ")
                    try:
                       wee_is_searching(new_song_name)
                    except Exception as ef:
                        print(new_song_name+" not found: ")
                        put_it_there(song_name)
                        print(ef)

def wee_is_searching(search_parameter):
                try:
                        test_search = "https://www.youtube.com/results?search_query=drake+lemon+pepper+freestyle"
                        thee_search = "https://www.youtube.com/results?search_query="+search_parameter+"+lyrics"
                        html = urllib.request.urlopen(thee_search,timeout=999999)
                        decoded_kinda = html.read().decode()

                        all_songs_found = re.findall(r"watch\?v=(\S{11})" , decoded_kinda)

                        #print(all_songs_found)
                        try:
                                try:
                                        thee_link = "https://www.youtube.com/watch?v="+all_songs_found[0]
                                except:
                                        thee_link = "https://www.youtube.com/watch?v="+all_songs_found[1]
                        except:
                                try:
                                        thee_link = "https://www.youtube.com/watch?v="+all_songs_found[2]
                                except:
                                        thee_link = "https://www.youtube.com/watch?v="+all_songs_found[3]

                        # print(thee_link)
                        downloader_mp3(thee_link)
                except:
                                
                                test_search = "https://www.youtube.com/results?search_query=drake+lemon+pepper+freestyle"
                                thee_search = "https://www.youtube.com/results?search_query="+search_parameter+"+lyrics"
                                html = urllib.request.urlopen(thee_search,timeout=999999)
                                decoded_kinda = html.read().decode()

                                all_songs_found = re.findall(r"watch\?v=(\S{11})" , decoded_kinda)

                                #print(all_songs_found)
                                try:
                                   try:
                                        thee_link = "https://www.youtube.com/watch?v="+all_songs_found[4]
                                   except:
                                        thee_link = "https://www.youtube.com/watch?v="+all_songs_found[5]
                                except:
                                   try:
                                        thee_link = "https://www.youtube.com/watch?v="+all_songs_found[6]
                                   except:
                                        thee_link = "https://www.youtube.com/watch?v="+all_songs_found[7]

                                # print(thee_link)
                                downloader_mp3(thee_link)

def downloader_mp3(song_id):
            try:
                # print(song_id)
                # print('in dowloader try')
                yt = YouTube(str(song_id))
                video = yt.streams.filter(only_audio=True).first()
                destination = '.'
                out_file = video.download(output_path=destination)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                print(yt.title + " has been successfully downloaded.")
            except Exception as ez:
                
                # print('in except downloader')
                # print(ez)
                audio = YouTube(song_id)     
                output = audio.streams.get_audio_only().download()
                base, ext = os.path.splitext(output)
                new_file = base + '.mp3'
                os.rename(output, new_file)

                print(yt.title + " has been successfully downloaded.")

def refine_name_first(filename):
       
              new_filenames = re.sub("\[SPOTIFY\-DOWNLOADER\.COM\]|clip|ATL ViDz|ATL ViDz|\#|ItsNambaNanneTV|ItsNambaNnaneTV|prod. Dj Nephas|DIR_@TONY_DE_GIGZ|PROD by DJ NEPHAS|iXtendz|The Decimators|DIR-VIKTA DANIELS|Nakuru All Stars|Oolisikia Wapi|dj mistanewa|Dr@viktadaniel|BAETUESDAY|KENYAN VERSION|Dir. by @_Tony De Gigz_|dirby@qvsual|prod by Magix Enga|Xmix|Mad House Sounds|@elanimuziki    to|@elanimuziki|\@MR MIMS 254|Iphone x  Edit|greatlakesmix.com|Lovechild Records|Long Version|short Version|INTRODUCING VARIOUS NEW ARTISTES|CLUB VERSiON|RED ACAPELLA|Visuals|JACK JACK ON THE|ItsNambaNaneTV|or   to|Main Switch|send to|2018|dance crew|\{|\}|JustLife.com|(SongsLover.com)|SongsLover.com|YouTube|Directed by @QuadDub|REFORMAT|5B   5D|unofficial|V2|h264|FHR|full video|hq|1080p|for skiza tune|FOR SKIZA TO 811|0fficial|Song|dial|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
              new_filename = re.sub("(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)
              new_filename = re.sub("(\-)$","",new_filename, flags=re.IGNORECASE)
              new_filenamer = re.sub("(\_)"," ",new_filename, flags=re.IGNORECASE)
              new_filenamerz = re.sub("- -","-",new_filenamer, flags=re.IGNORECASE)
              new_filenamer = re.sub("\--","\-",new_filenamerz, flags=re.IGNORECASE)
              new_filenamer = re.sub("\---","\***",new_filenamerz, flags=re.IGNORECASE)
              new_filenamers = re.sub("(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)
              
              return new_filenamers

def delete_downloaded_song():
        with open("hop.txt", 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[1:])   

def put_it_there(songer):

    with open("undownloaded.txt", "a") as f:
        f.write("\n")
        f.write(songer)
                 

create_param()
print("Execution Complete master")

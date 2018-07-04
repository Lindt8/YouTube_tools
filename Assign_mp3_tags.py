'''
Created on Jun 12, 2016

This code assumes that a number of mp3s have just been downloaded using Hexotic Software's YouTube Downloader.
http://hexotic.net/software/ytdownloader/

This code's purpose is to automatically assign tags to a mp3 file given song information in the mp3 filename.
The Hexotic YT downloader saves mp3s with the filename being the same as the video title.  
*Typically* people on YouTube use a naming syntax similar to:
[Genre (optional)] Artist - Song Name
This is exactly what this code is expecting.  All files fed to the code should have the artist first with the 
song name following, separated by a - (hyphen) character.  The code will look for a genre, but it is not required.
If a second hyphen is placed in the file name, anything beyond it will be ignored.

The code asks the user to provide a directory.  The code will then do this process for all mp3 files in the fodler.

@author: Hunter
'''

#import taglib #@UnresolvedImport
from mutagen.easyid3 import EasyID3
import os
from datetime import datetime
import urllib.request
from tkinter import Tk
from tkinter import filedialog
import re

# EasyID3 method:  https://stackoverflow.com/questions/4040605/does-anyone-have-good-examples-of-using-mutagen-to-write-files

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
path_dir = filedialog.askdirectory(initialdir=r"D:\Music\YouTube_Downloads", title="Select directory with files to be tagged") # show an "Open" dialog box and return the path to the selected file

Label_all_songs_as_single_album = False
album_name = 'Example Album Name'

for file in os.listdir(path_dir):
    if file.endswith(".mp3"):
        song_file = path_dir + "/" + file
        base = os.path.basename(song_file)
        filename, ext = os.path.splitext(base)
        
        if "[" in filename[:10]: 
            genre_incl = True
            #print(re.split(r'[]-]',filename))
            genre, artist, songname = re.split(r'[]-]',filename)[0:3]
            genre = re.sub('[[]', '', genre)
            genre = genre.rstrip()
            genre = genre.lstrip()
        else:
            genre_incl = False
            try:
                print(filename)
            except:
                print(filename.encode("utf-8"))
            songname = filename
            artist, songname = re.split(r'[]-]',filename)[0:2]
        
        #artist = artist.rstrip()
        #artist = artist.lstrip()
        songname = songname.rstrip()
        songname = songname.lstrip()
        
        # Manually set artist and album
        #artist = 'Example  Artist'
        
        
        #if genre_incl: print(genre)
        #print(artist)
        #print(songname)
        
        
        #f = taglib.File(song_file)
        #f.tags["ARTIST"] = artist
        #f.tags["TITLE"] = songname
        #if genre_incl: f.tags["GENRE"] = genre
        
        f = EasyID3(song_file)
        f["artist"] = artist
        f["title"] = songname
        if genre_incl: f["genre"] = genre
        
        if Label_all_songs_as_single_album:
            # Manually set album
            #f.tags["ALBUM"] = album_name
            f["album"] = album_name
        
        # Manually set genre
        #f.tags["GENRE"] = "Example Genre"
        
        #retval = f.save()
        f.save()

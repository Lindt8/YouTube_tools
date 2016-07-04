------------------------------------------------------------------------------------------------------
Assign_mp3_tags.py


This code assumes that a number of mp3s have just been downloaded using Hexotic Software's YouTube Downloader.
http://hexotic.net/software/ytdownloader/

This code's purpose is to automatically assign tags to a mp3 file given song information in the mp3 filename.  The Hexotic YT downloader saves mp3s with the filename being the same as the video title.  
*Typically* people on YouTube use a naming syntax similar to:

[Genre (optional)] Artist - Song Name

This is exactly what this code is expecting.  All files fed to the code should have the artist first with the song name following, separated by a - (hyphen) character.  The code will look for a genre, but it is not required.  If a second hyphen is placed in the file name, anything beyond it will be ignored.

The code asks the user to provide a directory.  The code will then do this process for all mp3 files in the folder.


------------------------------------------------------------------------------------------------------
thumbnail_grabber.py


This code expects a text file of 1 YouTube URL per line.  It will crawl through each URL in the text file and save an image from each with the filename being the same as the video title.

------------------------------------------------------------------------------------------------------
'''
Created on Mar 18, 2016
https://stackoverflow.com/questions/2068344/how-do-i-get-a-youtube-video-thumbnail-from-the-youtube-api
https://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know
@author: Hunter

This code expects a text file of 1 YouTube URL per line.  It will crawl through each URL in the text file and save an image from each with the filename being the same as the video title.

'''

import os
from datetime import datetime
import urllib.request
from tkinter import Tk
from tkinter import filedialog
import re

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
path_text_file = filedialog.askopenfilename(initialdir=r"D:\Music\YouTube_Downloads", title="Select text file with URLs") # show an "Open" dialog box and return the path to the selected file
fp = open(path_text_file)

output_dir = "Covers_" + datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
path_dil = "\\" # "\\" for getcwd, "/" for path.split
output_dir = os.path.split(path_text_file)[0] + path_dil + output_dir
#output_dir = os.getcwd() + path_dil + output_dir 
print(output_dir)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)  # Make directory if it does not already exist
im_url_0 = r"http://i1.ytimg.com/vi/"
im_url_1 = r"/hqdefault.jpg"
#im_url_1 = r"/0.jpg"

with open(path_text_file) as inf:
    for line in inf:
        vid = re.split("=",line)[1][0:11]
        im_url = im_url_0 + vid + im_url_1
        print(im_url)
        
        try:
            response = urllib.request.urlopen(line)
            if response.getcode() == 200:
                #print('Bingo')
                page_source = response.read(20000)
                page_src_str = page_source.decode('utf8')
                #page_src_str = page_source.decode('unicode_escape')
                title_start = "<title>"
                title_end = "</title>"
                title = re.split(title_start,page_src_str)[1]
                title = re.split(title_end,title)[0]
                title = re.sub('[<>:"/\|?*]', '', title)
                #print(title)
                title = re.sub(r'[^\x00-\x7f]',r'',title)
            else:
                print('The response code was not 200, but: {}'.format(
                    response.get_code()))
                title = vid
        except urllib.error.HTTPError as e:
            print('''An error occurred: {}
        The response code was {}'''.format(e, e.getcode()))
        
        out_fp = output_dir + path_dil + title + ".jpg"
        urllib.request.urlretrieve(im_url, out_fp)



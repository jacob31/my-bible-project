#!/usr/bin/python
from gtts import gTTS
import os

# get file name without extension
txt_file = os.sys.argv[1]
f_name, f_ext = os.path.splitext(str(txt_file))

# open the text file
file = open(txt_file, "r").read().replace("\n", " ")

language = 'en'

# convert text to mp3 file
speech = gTTS(text = str(file), lang = language, slow = False)
speech.save(f"{f_name}.mp3")

# start mp3 file
os.system(f"start {f_name}.mp3")

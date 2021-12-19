import re
import os

# get file name without extension
txt_file = os.sys.argv[1]
f_name, f_ext = os.path.splitext(str(txt_file))

book_collection = []

book = r"^[0-9A-Z][0-9A-Z][0-9A-Z]"

#get file object
file = open(str(txt_file), "r")
new_file = open(str(f_name)+"-new.txt", 'x')

while(True):
	#read next line
    line = file.readline()
	#check if line is not null  remember::: new_verse.group()
    if line:
        if re.match(book, line):
            book_collection.append(re.search(book, line).group())
        else:
            pass
	#you can access the line
    else:

        break

#close file
no_dup_book_collection = set(book_collection)
new_file.write(str(no_dup_book_collection))

new_file.close()
file.close

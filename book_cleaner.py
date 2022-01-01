import re
import os


#https://archive.org/details/cu31924067146773/page/n265/mode/2up
#28,904  £
# get file name without extension
txt_file = os.sys.argv[1]
f_name, f_ext = os.path.splitext(str(txt_file))

scrolls = {'GEN': 'Genesis', 'EXO': 'Exodus', 'LEV': 'Leviticus', 'NUM': 'Numbers',
'DEU': 'Deuteronomy', 'JOS': 'Joshua', 'JDG': 'Judges', 'RUT': 'Ruth',
'1SA': '1 Samuel', '2SA': '2 Samuel', '1KI': '1 Kings', '2KI': '2 Kings',
'1CH': '1 Chronicles', '2CH': '2 Chronicles', 'EZR': 'Ezra', 'NEH': 'Nehemiah',
'EST': 'Esther', 'JOB': 'Job', 'PSA': 'Psalm', 'PRO': 'Proverbs',
'ECC': 'Ecclesiastes', 'SOL': 'Song of Solomon', 'ISA': 'Isaiah',
'JER': 'Jeremiah', 'LAM': 'Lamentations', 'EZE': 'Ezekiel', 'DAN': 'Daniel',
'HOS': 'Hosea', 'JOE': 'Joel', 'AMO': 'Amos', 'OBA': 'Obadiah', 'JON': 'Jonah',
'MIC': 'Micah', 'NAH': 'Nahum', 'HAB': 'Habakkuk', 'ZEP': 'Zephaniah',
'HAG': 'Haggai', 'ZEC': 'Zechariah',  'MAL': 'Malachi', 'TOB': 'Tobit',
'JDT': 'Judith', 'ESG': 'Esther (Greek)', 'WIS': 'Wisdom', 'SIR': 'Sirach',
'BAR': 'Baruch',  'PRA': 'Azariah', 'SUS': 'Susanna',  'BEL': 'Bel',
'1MA': '1 Maccabees', '2MA': '2 Maccabees', '1ES': '1 Esdras', 'PRM': 'Manasseh',
'4ES': '4 Esdras',  '1EN': '1 Enoch', 'MAT': 'Matthew', 'MAR': 'Mark', 'LUK': 'Luke', 'JOH': 'John',
'ACT': 'Acts', 'ROM': 'Romans', '1CO': '1 Corinthians', '2CO': '2 Corinthians',
'GAL': 'Galatians', 'EPH': 'Ephesians', 'PHI': 'Philippians', 'COL': 'Colossians',
'1TH': '1 Thessalonians', '2TH': '2 Thessalonians', '1TI': '1 Timothy',
'2TI': '2 Timothy', 'TIT': 'Titus', 'PHM': 'Philemon', 'HEB': 'Hebrews',
'JAM': 'James', '1PE': '1 Peter', '2PE': '2 Peter', '1JO': '1 John',
'2JO': '2 John', '3JO': '3rd John', 'JUD': 'Jude', 'REV': 'Revelation'}

new_chptr = r"^[0-9A-Z][A-Z][A-Z] [0-9]*:1 "
verse = r"^[0-9A-Z][A-Z][A-Z] [0-9]*:[0-9]* "
book_rgx = r"^[0-9A-Z][0-9A-Z][0-9A-Z]"
chptr_rgx = r" [0-9]+"
return_rgx = r"(¶)"
#get file object
file = open(str(txt_file), "r")
new_file = open(str(f_name)+"-new.txt", 'x')

while(True):
	#read next line
    line = file.readline()
    pos = max(line.find(':'), 0) + 1
	#check if line is not null  remember::: new_verse.group()
    if line:
        new_chapter = re.match(new_chptr, line)
        return_symbol = re.search(return_rgx, line)
        if new_chapter:
            book = re.search(book_rgx, line).group()
            chapter = re.search(chptr_rgx, line).group()
            new_file.write(f"\n{scrolls[book]}" + f" Chapter {chapter}" + "\n\n")
            new_file.write(line[pos:].strip()+"\n")
        elif return_symbol:
            pos = max(line.find(':'), 0) + 1
            new_file.write("\n" + line[pos:].strip() + "\n")
        else:
            new_file.write(line[pos:].strip() + "\n")
	#you can access the line
    else:

        break

#close file
new_file.close()
file.close

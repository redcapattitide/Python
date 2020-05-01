﻿from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import telegram.bot
import logging

def get_info():
    # reading recept_info regenerated by Recept.exe everytime something moves in the office
    # and declaring some basic stuff
    f = open('C://Users/Tom/Documents/Python/Bot/Receptura/Recept/Recept/bin/Release/recept_info.txt', 'r', encoding= 'UTF-8')
    s = []
    list_of_prosecutor = []
    list_of_deputy = []
    deputy_on_duty = False
    prosecutor_on_duty = False
    s = f.read().split('\n')
    f.close()
    # print(s)
    if s[1] == '+':
        deputy_on_duty = True
    else:
        deputy_on_duty = False
    deputy_count = int(s[2])
    i = 3

    # getting names into local variables form recept_info
    while s[i] != 'шеф':
        if (s[i] != '') and (s[i] != ' '):
            list_of_deputy.append(s[i])
        i += 1
    if s[i+1] == '+':
        prosecutor_on_duty = True
    else:
        prosecutor_on_duty = False
    prosecutor_count = int(s[i+2])
    i += 3
    while i < len(s):
        if (s[i] != '') and (s[i] != ' '):
            list_of_prosecutor.append(s[i])
        i += 1
    
    # forming final output strings for deputy and prosecutor
    deputy_result = 'Заместитель '
    prosecutor_result = 'Прокурор '

    if deputy_on_duty :
        deputy_result += 'на месте'
        if deputy_count == 0 : 
            deputy_result += ', у него никого\n'
            for item in list_of_deputy:
                deputy_result += item + '\n'
        else :
            deputy_result += ', у него ' + str(deputy_count) + ' чел'
            deputy_result += ':\n'
            for item in list_of_deputy:
                deputy_result += item + '\n'
    else:
        deputy_result += 'не на месте\n'
        for item in list_of_deputy:
            deputy_result += item +'\n'
    
    if prosecutor_on_duty :
        prosecutor_result += 'на месте'
        if prosecutor_count == 0 : 
            prosecutor_result += ', у него никого\n'
            for item in list_of_prosecutor:
                prosecutor_result += item + '\n'
        else :
            prosecutor_result += ', у него ' + str(prosecutor_count) + ' чел'
            prosecutor_result += ':\n'
            for item in list_of_prosecutor:
                prosecutor_result += item + '\n'
    else:
        prosecutor_result += 'не на месте\n'
        for item in list_of_prosecutor:
            prosecutor_result += item + '\n'
    if 'Прокурор' in deputy_result:
        return deputy_result
    elif 'Заместитель' in prosecutor_result:
        return prosecutor_result
    else:
        return deputy_result, prosecutor_result
    
def main():
    
    logging.basicConfig(level=logging.DEBUG)
    message = get_info()
    print(str(message))


if __name__ == "__main__":
    main()
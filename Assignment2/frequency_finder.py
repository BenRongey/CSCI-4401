# Ben Rongey
# Spring 2019
# CSCI 4401

# This script will analyze the a file containing the first 10^9 bytes of Wikipedia English dump from 2006.  It will determine the frequency of each word length in that text from 1 letter to 8 or more letters as a percentage.  This version will only be single-threaded, to compare final analysis speeds to a multi-threaded version.

# import re

# file_obj = open("enwik9", "r")

# for line in file_obj:
#     one = []
#     one = line.replace('<', '')
#     one = line.replace('>', '')
#     print(len(line))


# print(len(file_obj.readline()))
# one = []
# one = file_obj.readline()
# one.replace('<', '')
# one.replace('>', '')
# print(len(one))
# print(one)

def get_freq(name):
    
    num_lines = 0
    num_words = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    
    if name:
        with open(name, 'r') as file_obj:
            for line in file_obj:
                while num_lines < 1:
    
                    line = line.replace('/', ' ')
                    line = line.replace('[', ' ')
                    line = line.replace(']', ' ')
                    line = line.replace('*', ' ')
                    line = line.replace("'", " ")
                    line = line.replace('!', ' ')
                    line = line.replace('@', ' ')
                    line = line.replace('$', ' ')
                    line = line.replace('%', ' ')
                    line = line.replace('^', ' ')
                    line = line.replace('&', ' ')
                    line = line.replace('+', ' ')
                    line = line.replace('~', ' ')
                    line = line.replace('`', ' ')
                    line = line.replace('\\', ' ')
                    line = line.replace('|', ' ')
                    line = line.replace('?', ' ')
                    line = line.replace('{', ' ')
                    line = line.replace('}', ' ')
                    line = line.replace('#', ' ')
                    line = line.replace('"', ' ')
                    line = line.replace('.', ' ')
                    line = line.replace('=', ' ')
                    line = line.replace(':', ' ')
                    line = line.replace('<', ' ')
                    line = line.replace('>', ' ')
                    
                    word_list = line.split( )
                    for word in word_list:
                        if len(word) == 1:
                            count_1 += 1
                    num_lines += 1
                    num_words += len(word_list)
            
        print('There are ' + str(count_1) + ' words of length 1')
        print('There are ' + str(count_2) + ' words of length 2')
        print('There are ' + str(count_3) + ' words of length 3')
        print('There are ' + str(count_4) + ' words of length 4')
        print('There are ' + str(count_5) + ' words of length 5')
        print('There are ' + str(count_6) + ' words of length 6')
        print('There are ' + str(count_7) + ' words of length 7')
        print('There are ' + str(count_8) + ' words of length 8 and 8+')
        print()
        print('Total Lines: ' + str(num_lines))
        print('Total Words: ' + str(num_words))
        print()

        file_obj.close


get_freq('enwik9')




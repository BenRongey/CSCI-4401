# Ben Rongey
# Spring 2019
# CSCI 4401

# This script will analyze the a file containing the first 10^9 bytes of Wikipedia English dump from 2006.  It will determine the frequency of each word length in that text from 1 letter to 8 or more letters as a percentage.  This version will only be single-threaded, to compare final analysis speeds to a multi-threaded version.

import time

# Used to calculate time (using seconds and float)
start_time = time.time()


def get_freq(name):

    # These variables will store our relevant data
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
    
    # If the given file name exists, open it and read it line by line
    if name:
        with open(name, 'r') as file_obj:
            for line in file_obj:
    
                # Remove all non-essential characters per the given instructions
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
                
                # Split the words by spaces 
                word_list = line.split( )

                # Sort the word size into the correct variables.  Default Python doesn't have switch statements, which seems kinda crazy.
                for word in word_list:
                    if len(word) == 1:
                        count_1 += 1
                    elif len(word) == 2:
                        count_2 += 1
                    elif len(word) == 3:
                        count_3 += 1
                    elif len(word) == 4:
                        count_4 += 1
                    elif len(word) == 5:
                        count_5 += 1
                    elif len(word) == 6:
                        count_6 += 1
                    elif len(word) == 7:
                        count_7 += 1
                    else:
                        count_8 += 1
                
                # Not required for the assignment, but I was curious
                num_lines += 1
                num_words += len(word_list)
            
        # Display the data to the terminal
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

        # Close the open stream
        file_obj.close

# Run the actual function defined above
get_freq('enwik9')

# Subtract current time from the above saved time to get the total float (seconds) of run time for the script
print('--- %s seconds ---' % (time.time() -start_time))



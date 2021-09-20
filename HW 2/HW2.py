# Stevens Institute of Technology, 2021

##########################################
# Name: Tyler Seliber
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
##########################################
from math import floor    # E.g., floor(5.3) -> 5, floor(3.9) -> 3

######################################################################
# Task 1: Given an 8-digit decimal number representing the date,
#         calculate the day of the week using Zeller's congruence:
#
#           https://en.wikipedia.org/wiki/Zeller%27s_congruence
#
# Input:  8-digit decimal number in the format of YYYYMMDD
#
# Output: Weekday as a [0-6] number, where 
#         0: Saturday, 1: Sunday, 2: Monday, ..., 6: Friday  
######################################################################
def getWeekday(date):
    # Parse date into year, month, and day values
    
    # Get day, which is last two digits of date
    day = date % 100
    date //= 100
    # Get month, which is last two digits of date
    month = date % 100
    date //= 100
    # Get year, which is now equal to date
    year = date

    # Convert January to 13 and February to 14, and subtract 1 from year
    if month == 1:
        month = 13
        year -= 1
    elif month == 2:
        month = 14
        year -= 1
 

    weekday = (day +floor((13 * (month + 1) / 5)) + (year % 100) + floor((year % 100) / 4) + floor((floor((year / 100)) / 4)) + (5 * floor((year / 100)))) % 7

    return weekday

######################################################################
# Task 2: Create two functions, an encoder and a decoder for the
#         Caesar cipher:
#
#           https://en.wikipedia.org/wiki/Caesar_cipher
#
# Note: You can try out this cipher at the link below:
#
#           https://cryptii.com/pipes/caesar-cipher
######################################################################

######################################################################
# This provided helper function may be useful
# Input:  List of ASCII values (Ex: [72, 69, 76, 76, 79])
# Output: String (Ex. 'HELLO')       'H   E   L   L   O'
######################################################################
def asciiToString(asciiList):
    return ''.join(map(chr, asciiList))

######################################################################
# Caesar Encoder
#
# Input: A string (assume all-caps: leave everything else as-is),
#        and a shift value       (Ex. 'HELLO WORLD', 3)
#
# Output: An encoded string      (Ex. 'KHOOR ZRUOG')
#
# Hint: The ord() function converts single-character strings to ASCII
#       (Its inverse, the chr() function, is used in the provided helper)
######################################################################
def caesarEncoder(str, shift):

    # Convert str to list of ASCII characters
    asciiList = list(map(ord, str))

    # Function to applyOffset to asciiList characters
    def applyOffset(ch):
        
        # Ignore spaces
        if ch == 32:
            return ch

        # Map alphabet to be from [0, 25] 
        ch -= 65
        # Apply offset, using mod 26 to wrap around the alphabet
        ch = (ch + shift) % 26
        # Convert back to ASCII
        ch += 65

        return ch

    # Apply the offset to asciiList characters
    encodedASCII = list(map(applyOffset, asciiList))
    # Convert back to a string
    encodedStr = asciiToString(encodedASCII)
    return encodedStr

######################################################################
# Decoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. KHOOR ZRUOG, 3)
# Output: A decoded string             (Ex. HELLO WORLD)
# Hint: The chr() function converts ASCII to a single-character string
######################################################################
def caesarDecoder(str, shift):
    return caesarEncoder(str, shift * -1)

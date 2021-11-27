"""
Created by Daniel Maciejewski 11/17/2021
INFOST 691-202 Digital Forensics Final Project

Assignment Prompt
-----------------
Using your favorite programming language, create a software tool (application) that would act as a 
hex editor. That is. The tool would be able to open any type of files at the binary level similar to 
the hexedit tool we learned in this course.

Sources Cited
-------------
https://www.qtrac.eu/pyhexviewer.html
https://www.youtube.com/watch?v=kJSOuPTjH50
/end Comments
"""
#Variable Declaration

bytesRead = 0 #count the number of bytes being read in the 'for' loop
contentLine = [] #list (array) holds the contents of the 'for' loop

print("HexaPy")#Project Name


file = input("Enter a file name: ") #Create a string to hold the name of the target file

"""
use python open() method to open chosen file in binary format
using the 'with' operator closes the file to free memory after it has been read, using read(), into the script

"""
with open(file,'rb') as openedFile:
    fileContent = openedFile.read()

for byte in fileContent:#The 'for' loop prints out the data read from file
    bytesRead = bytesRead+1#increment the line counter
    contentLine.append(byte)#add the contents read from byte to contentLine list
    """
    print() notes
    overview: display outputted line in console as a formatted printout 
    -the format(byte,2) method displays the string (byte) placeholder to be passed in to print with several modifications
        -'{}' delimits the formatted output
        -':x' reads the output as lower case hex format
        -'end=" "' parameter places an empty space at the end of the printed line rather than default newline character
    """
    print("{0:0{1}x}".format(byte,2), end=" ")
    if bytesRead % 16 == 0:
        print("#",end=" ")
        for byteTwo in contentLine:
            if (byteTwo >= 32) and (byteTwo <= 126):
                print(chr(byteTwo), end = "")
            else:
                print("*", end=" ") 
        contentLine = []
        print("")
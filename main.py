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
https://www.youtube.com/watch?v=kJSOuPTjH50
"""
#imports
import os
#Variable Declaration
class hexaPy:
    def __init__(self,file,bytesRead,contentLine,lowerAscii,upperAscii):
        self.file = ""
        self.bytesRead = 0 #count the number of bytes being read in the 'for' loop
        self.contentLine = [] #list (array) holds the contents of the 'for' loop
        self.lowerAscii = 32#the lower range of human-readable ascii
        self.upperAscii = 126#the upper range of human-readable ascii
    
    def getFile():
        print("=================================================================================================================================================\nHexaPy: Feed me a file and I'll feed you its hex content! 0w0",
        "\n=================================================================================================================================================\n")#Project Name


        file = input("file name: ") #Create a string to hold the name of the target file
        return file

    def analyzeFile(file):
        """
        use python open() method to open chosen file in binary format
        using the 'with' operator closes the file to free memory after it has been read, using read(), into the script

        """
        with open(file,'rb') as openedFile:
            fileContent = openedFile.read()

        global bytesRead, contentLine, lowerAscii, upperAscii
        bytesRead = 0 #count the number of bytes being read in the 'for' loop
        contentLine = [] #list (array) holds the contents of the 'for' loop
        lowerAscii = 32#the lower range of human-readable ascii
        upperAscii = 126#the upper range of human-readable ascii
        bytesRead = 0
        for byte in fileContent:#The 'for' loop prints out the data read from file
            bytesRead = bytesRead+1#increment the line counter
            contentLine.append(byte)#add the contents read from byte to contentLine list
            """
            print() notes
            overview: display outputted line in console as a formatted hex printout 
            -the format(byte,2) method displays the string (byte) placeholder to be passed in to print with several modifications
                -'{}' delimits the formatted output
                -':x' reads the output as lower case hex format
                -'end=" "' parameter places an empty space at the end of the printed line rather than default newline character
            """
            print("{0:0{1}x}".format(byte,2), end=" ")
            if bytesRead % 16 == 0:#if the line has 16 characters outputted mark the end
                print("#",end=" ")
                """
                this 'for' loop reads content line and dumps human-readable characters from the ascii values of each hex code and omits assembly instructions
                """
                for asciiNumber in contentLine:
                    if (asciiNumber >= lowerAscii) and (asciiNumber <= upperAscii):
                        print(chr(asciiNumber), end = "")
                    else:
                        print("*", end=" ") 
                contentLine = []
                print("")
        print("\n=================================================================================================================================================\n",
        "Yum ^w^! Hex Dump Complete\n================================================================================================================================================\n")

#execute code
hexaPy
file = hexaPy.getFile()
hexaPy.analyzeFile(file)
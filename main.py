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
#imports
import os, sys
import tkinter as tk

print("HexaPy")#Project Name


file = input("Enter a file name: ")
openedFile= open(file,'rb')

bytesRead = 0
contentLine = []

fileContent = openedFile.read()
for byte in fileContent:
    bytesRead = bytesRead+1
    contentLine.append(byte)
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
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 07:46:36 2018

@author: mtjansen
"""
import os

path=input("Please enter a file directory:") #input() asks the user for input and interprets it as a string

try:
    files=os.listdir(path)
    groups={}
    for f in files:
        if len(f.split("."))>1:
            extension=f.split(".")[-1] 
            name=f.split(".")[0] 
            if extension in groups.keys():
                groups[extension].append(name)
            else:
                groups[extension]=[name]
        elif len(f.split("."))==1:
            name=f
            if "folders" in groups.keys():
                groups["folders"].append(name)
            else:
                groups["folders"]=[name]
            
    
    for g in groups.keys():
        print(g+" : ")
        print(groups[g])
        
    print("Counts")
    print({g:len(groups[g]) for g in groups.keys()})

except:
    print("This is not a valid file path! Don't forget to flip Windows slashes!")
    


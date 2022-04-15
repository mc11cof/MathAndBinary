#!/usr/bin/env python3
# Created by Marc-Alistair Coffi
# Created in April 2022
# Module holding functions

def printInstructions(insruction):
    print(insruction)
    
def getUserScore(userName):
    file = open("userScores.txt", "r")
    for n in file:
        content = file.split()
        if userName == content:
            return content
        else:
            return "-1"
    
#!/usr/bin/env python3
# Created by Marc-Alistair Coffi
# Created in April 2022
# Module holding functions

# This function prints out the instructions of the game
def printInstructions(instruction):
    print(instruction)


# This function looks at the username to see if the user already played or if it is his first time
def getUserScore(userName):
    try:
        input = open("userScores.txt", "r")
        for line in input:
            content = line.split(", ")
            if content[0] == userName:
                input.close()
                return content[1]
        input.close()
        return "-1"
    except IOError:
        print("File not found. A new file will be created.")
        input = open("userScores.txt", "w")
        input.close()
        return "-1"


# This function updates the score of the different players based on their username
def updateUserScore(newUser, userName, score):
    from os import remove, rename

    if newUser == True:
        input = open("userScores.txt", "a")
        input.write(userName + ", " + score + "\n")
        input.close()
    else:
        temp = open("userScores.tmp", "w")
        input = open("userScores.txt", "r")
        for line in input:
            content = line.split(", ")
            if content[0] == userName:
                temp.write(userName + ", " + score + "\n")
            else:
                temp.write(line)

        input.close()
        temp.close()

        remove("userScores.txt")
        rename("userScores.tmp", "userScores.txt")

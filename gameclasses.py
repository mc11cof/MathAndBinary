#!/usr/bin/env python3
# Created by Marc-Alistair Coffi
# Created in April 2022
# The 3 classes for the game

# This class is for both the math and binary game, it ask the user the amount of questions they want to anwer
class Game:
    def __init__(self, noOfQuestions=0):
        self._noOfQuestions = noOfQuestions

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print("\nMinimum Number of Questions = 1")
            print("Hence, number of questions will be set to 1")
        elif value > 10:
            self._noOfQuestions = 10
            print("\nMaximum Number of Questions = 10")
            print("Hence, number of questions will be set to 10")
        else:
            self._noOfQuestions = value


# This class defines how the binary game will function
class BinaryGame(Game):
    def generateQuestions(self):
        from random import randint

        score = 0

        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            userResult = input("\nPlease convert %d to binary: " % (base10))
            while True:
                try:
                    answer = int(userResult, base=2)
                    if answer == base10:
                        print("Correct Answer!")
                        score = score + 1
                        break
                    else:
                        print(
                            "Wrong answer. The correct answer is {:b}.".format(base10)
                        )
                        break
                except:
                    print("You did not enter a binary number. Please try again.")
                    userResult = input("\nPlease convert %d to binary: " % (base10))

        return score


# This class defines how the math game will be functionning
class MathGame(Game):
    def generateQuestions(self):
        from random import randint

        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ["", "", "", ""]
        operatorDict = {1: " + ", 2: " - ", 3: "*", 4: "**"}

        for i in range(self.noOfQuestions):
            for index in range(0, 5):
                numberList[index] = randint(1, 9)
            # refer to explanation below
            for index in range(0, 4):
                if index > 0 and symbolList[index - 1] == "**":
                    symbolList[index] = operatorDict[randint(1, 3)]
                else:
                    symbolList[index] = operatorDict[randint(1, 4)]

            questionString = str(numberList[0])

            for index in range(0, 4):
                questionString = (
                    questionString + symbolList[index] + str(numberList[index + 1])
                )

            result = eval(questionString)

            questionString = questionString.replace("**", "^")

            userResult = input("\nPlease evaluate %s: " % (questionString))

            while True:
                try:
                    answer = int(userResult)
                    if answer == result:
                        print("Correct Answer!")
                        score = score + 1
                        break
                    else:
                        print(
                            "Wrong answer. The correct answer is {:d}.".format(result)
                        )
                        break
                except:
                    print("You did not enter a valid number. Please try again.")
                    userResult = input("\nPlease evaluate %s: " % (questionString))

        return score

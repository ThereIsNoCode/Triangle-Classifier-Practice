#import pygame
#import pygame.gfxdraw
import random
import sys
import math

ListOfPositions = []
#Github = ThereIsNoCode/Triangle-Classifier-Practice
#region-1
class Vector2: #Handles User input and stores Positon
    def __init__(self, _userinput):
        self.x = 0.0
        self.y = 0.0

        splitInput = _userinput.split(",")
        self.x = float(splitInput[0])
        self.y = float(splitInput[1])
#region-1



def ClassifyTriangle(): #Classifies Triangle

    i = 0
    b = 0
    amountOfSidesEqual = 0

    side1Length  = CalculateLength(Pos1.x, Pos1.y, Pos2.x, Pos2.y)
    side2Length = CalculateLength(Pos1.x, Pos1.y, Pos3.x, Pos3.y)
    side3Length = CalculateLength(Pos2.x, Pos2.y, Pos3.x, Pos3.y)

    side1Slope  = CalculateSlope(Pos1.x, Pos1.y, Pos2.x, Pos2.y)
    side2Slope = CalculateSlope(Pos1.x, Pos1.y, Pos3.x, Pos3.y)
    side3Slope = CalculateSlope(Pos2.x, Pos2.y, Pos3.x, Pos3.y)


    sidesLengthHolder = [side1Length, side2Length, side3Length]
    sidesSlopeHolder = [side1Slope, side2Slope, side3Slope]

    for x in sidesLengthHolder: #Checks which sides are Equal
        i += 1
        if i > 2:
                i = 0
        if x == sidesLengthHolder[i]:
            amountOfSidesEqual += 1
    for x in sidesSlopeHolder: #Checks which sides are Equal
        b += 1
        if b > 2:
                b = 0
        if x == 0 and sidesSlopeHolder[b] == 999:
            amountOfSidesEqual = 5
        if sidesSlopeHolder[b] != 0:
            if x == -1/sidesSlopeHolder[b]:
                amountOfSidesEqual = 5



    if amountOfSidesEqual == 0:
        print("Scalene Triangle")
    elif amountOfSidesEqual == 1:
        print("Isosceles Triangle")
    elif amountOfSidesEqual == 3:
        print("Equilateral Triangle")
    elif amountOfSidesEqual == 5:
        print("Right angle triangle")

def CalculateSlope(x1, y1, x2, y2): #Calculates Slope of line
    y2 -= y1
    x2 -= x1
    if(x2 == 0):
        return 999;
    return y2 / x2

def CalculateLength(x1,y1, x2, y2): #Calculates length of 2 points joined as a line

    x2 -= x1
    y2 -= y1

    x2**=2
    y2**=2

    return x2 + y2

     #WILL NOT SQUAREROOT FOR YOU DASS


#region-2
userinput =  input("First Point Positon? \n")
Pos1 = Vector2(userinput)
ListOfPositions.append(Pos1)

userinput =  input("Second Point Positon? \n")
Pos2 = Vector2(userinput)
ListOfPositions.append(Pos2)

userinput =  input("Third Point Positon? \n")
Pos3 = Vector2(userinput)
ListOfPositions.append(Pos3)

ClassifyTriangle()

#region-2

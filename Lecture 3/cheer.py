# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:51:57 2016

@author: ericgrimson
"""
def intToBin(num, binStr, isNeg = False):
    """
    Input: num = rest of the number to be evaluated, binStr = string to be printed
    Output: num = number after being divided by 2, binStr = rightmost bit + string to be printed
    
    Uses recursion to take output as input
    """
    if num < 0:
        print("Number is negative")
        isNeg = True
        num = abs(num)
    if num == 0:
        if isNeg == True:
            print("The binary string of -", num, "is -" + binStr)
        else:
            print("The binary string of ", num, "is ", binStr)
    else:
        binStr = str(num%2) + binStr
        print(binStr)
        num = num//2
        intToBin(num, binStr, isNeg)
        

intToBin(-678, '')

def decToBin(num, binStr, isNeg = False, isInt = True):
    """
    Input
    num = number being converted to binary
    binStr = string being printed
    isNeg = True if number is negative else False if number is positive
    isInt = True if number is integar else False if number is decimal
    
    output
    num = remaining number being calculated after computation
    binStr = string being printed after one iteration
    isNeg = True if number is negative else False if number is positive
    isInt = True if number is integar else False if number is decimal
    """
    #convert the whole part and fractional part at the same time
    #reduces computational time by O(n/2) assuming whole and fractional length are same
    
    if num < 0:
        print("Number is negative")
        isNeg = True
        num = abs(num)
    #Determine if the number is only an integar
    if num%1 == 1:
        print("Number is decimal")
        isInt = False
    #Reach the final amount flip the binary bits around    
    if num == 0:
        binStr = binStr[::-1] #OH YEAAAAA you can just reverse strings like this. Completely forgot
        if isNeg == True:
            print("The binary string of is ", binStr)
        else:
            print("The binary string of -", binStr)
    else:
        #Calculate only as integar if number is int
        if isInt == True:
            binStr = str(num%2) + binStr
            print(binStr)
            num //= 2
            decToBin(num, binStr, isNeg, isInt)
        else:
        #Figure out how to convert the fractional part
        #Have two expressions evaulating the whole and fractional part
            
        #1 - Whole to Binary
            wholeNum = num//1
            binStr = binStr + str(wholeNum%2)
            wholeNum //= wholeNum
            
        #2 - Fractional to Binary
            fracNum = num%1
            fracNum *= 2    #Takes the whole number of the fractional part when multiplied by 2
            binStr = str(fracNum//1) + binStr 
            fracNum %= fracNum
            
        #3 - Combine the two parts together
            num = wholeNum + fracNum
            decToBin(num, binStr, isNeg, isInt)
            
            
                        
            
            
            
            
    
        
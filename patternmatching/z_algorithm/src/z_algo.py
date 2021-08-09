import sys

"""
Author: Aqeel Ahlam Rauf
Date: 09/07/2021

Linear time Pattern Matching Algorithm:
- This algorithm was designed to find all occurances of a pattern in a text in linear time. 
- Reference: https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/

Time Complexity: O(length(pattern) + length(string))
Space Complexity: O(length(pattern) + length(string))

Command Line Input: python3 z_algo.py text pattern

Note: 
Array output will return the length of the matched pattern. 
Full Match: If the length of the pattern is equal to the number in the array
"""
def main():
    # Get input from command Line:
    text = sys.argv[1]
    pattern = sys.argv[2]

    ZArrayPrefix = preprocessPrefix(text, pattern)
    count = 0
    positionsList = []

    for i in range(len(pattern)+1, len(ZArrayPrefix)):
        if ZArrayPrefix[i]>0:
            count += 1
            positionsList.append(i- len(pattern)-1)

    while True:
        if count <= 0:
            print("No Matches Found")
            sys.exit()
        elif input("Do You want an array? (y/n)\n") == 'y':
            print(ZArrayPrefix[len(pattern)+1:])
            sys.exit()
        else:
            for i in range(len(positionsList)):
                print("Position", positionsList[i])
            sys.exit()

def ZAlgoPrefix(string):
    """
    This function is used to calculate and return the Z-Value array for a String from the start to end
    :param string: String to calculate Z-Values
    :return: Z-Array
    :Time Complexity(Worst): O(N)
    :Space Complexity(Worst): O(N)
    """
    patLen = len(string)
    # Initialization of Z-Array
    ZArray = [0] * patLen
    ZArray[0] = patLen
    leftZBox = 0
    rightZBox = 0

    for i in range(1, patLen):
        """
        Case 1: Where i is outside the Zbox, we don't have any pre-computed values, therefore perform explicit
        comparisons
        """
        if i > rightZBox:
            ZArray[i] = PrefixCompare(string, i)
            # Update Left and Right ZBox
            rightZBox = ZArray[i] + i - 1
            leftZBox = i
        # Case 2: Where i is inside the Z-Box, Dynamic Programming Begins
        else:
            k = i - leftZBox
            rem = rightZBox - i + 1
            # When Z Array Element is less than remaining
            if ZArray[k] < rem:
                ZArray[i] = ZArray[k]
            # When Z Array Element is greater than remaining
            elif ZArray[k] > rem:
                ZArray[i] = rem
            # Case 2c: Z[k] == rem 
            else:
                ZArray[i] = rem + PrefixCompare(string, rightZBox + 1, rem)
    return ZArray


def PrefixCompare(string, i, k=0):
    """
    This function is used to compare two positions in a string until a mismatch
    :param string: String to compare
    :param i: Index position of string to compare
    :param k: Index position of string to compare
    :return: A Z-Value (Length of a string until mismatch occurred)
    """
    zVal = 0
    while i < len(string):
        if string[i] == string[k]:
            i += 1
            k += 1
            zVal += 1
        else:
            break
    return zVal


def preprocessPrefix(text, pattern):
    string = pattern + '$' + text

    return ZAlgoPrefix(string)

if __name__ == "__main__":
    main()

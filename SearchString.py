import unittest

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        if aStr[0] == char:
            return True
        if aStr[0] != char:
            return False
    if len(aStr) > 1:
        if aStr[int(len(aStr) / 2)] == char:
            return True
        if char < aStr[int(len(aStr) / 2)]:
            isIn(char, aStr[0 : int(len(aStr) / 2)-1])
        if char > aStr[int(len(aStr) / 2)] :
            isIn(char, aStr[int(len(aStr) / 2) : ])
    return False

if __name__ == "__main__":
    print(isIn('o', 'ffoqvy') )
#!/usr/bin/python3

def isPermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    elif (set(string1) == set(string2)):
        return True
    else:
        return False
    
def main():
    pass

if __name__ == "__main__":
    main()

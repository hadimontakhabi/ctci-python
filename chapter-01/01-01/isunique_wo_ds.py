#!/usr/bin/python3

def isUnique(string):
    for i,c in enumerate(string):
        for j in range(i+1,len(string)):
            if string[i] == string[j]: return False
    return True
        
def main():
    pass

if __name__=="__main__":
    main()

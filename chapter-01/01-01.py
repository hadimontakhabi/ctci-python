#!/usr/bin/python3

def isunique(string):
    if len(set(string)) == len(string):
        return True
    else:
        return False

    
def main():
    for w in ['aa','00','121','35435']:
        if isunique(w) == True:
            print('Failed')
    for w in ['','0','a','asdwe231', 'e[2cov]\'']:
        if isunique(w) == False:
            print('Failed')
    

if __name__=="__main()__": main()

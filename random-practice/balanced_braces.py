import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.info)

def braces(values):
    stack = []
    open_chars = ['(','{','[']
    close_chars = [')','}',']']
    return_array = [None] * len(values)
    for index, value in enumerate(values):
        for i in range(len(value)):
            if value[i] in open_chars:
                stack.append(value[i])
                logging.debug('Appnded : {}  Stack: {}'.format(value[i],stack))
            elif value[i] in close_chars:
                try:
                    popped = stack.pop()
                except Exception as e:
                    print ('FUCK! ' ,e)
                    return_array[index] = 'NO'
                    break
                logging.debug('popped= {} , value[i]= {}'.format(popped, value[i]))
                if (value[i] == ')' and popped != '(') or (value[i] == '}' and popped != '{') or (value[i] == ']' and popped != '['):
                    return_array[index] = 'NO'
                    break
        if stack == []:
            return_array[index] = 'YES'
    return return_array


print (braces(('2','{}[]()','{[}]')))

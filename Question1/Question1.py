import re

special_sym = {
    '+' : ['Plus-sign', 11],
    '-' : ['Minus-sign', 12],
    '(' : ['Left-parenthesis',41],
    ')' : ['Right-parenthesis',42],
    '{' : ['Left-bracket',43],
    '}' : ['right-bracket',44],
    '*' : ['Multiplication-symbol',13],
    '/' : ['Division-symbol',14],
    '$' : ['Dollar-sign',19],
    '%' : ['Percent-symbol',15],
    '=' : ['Equal-sign',17],
    '<' : ['Less-than',21],
    '>' : ['Greater-than',22],
    '<=': ['Less-Than-Equal',23],
    '>=': ['Greater-Than-Equal',24],
    }

#These are our key words containing for, if, while, etc...
keyWords = {
        'for' : ['for-loop', 31],
        'if' : ['if-statement, 32'],
        'while' : ['while-loop', 33],
        'do' : ['do', 34],
        'int' : ['integer', 35],
        'float' : ['floating-point', 36],
        'switch': ['switch-statement', 37]
    }
   
#Here is where we tokenize each of our lexemes and determine what they are with reg expressions
def tokenize(fileInput):
    first = fileInput[0]
    num = False
    val = False
    number= re.fullmatch(r"[0-9]", first)
    identifier = re.fullmatch(r"[a-zA-Z]", first)
    special = re.fullmatch(r"[^a-zA-z0-9]", first)
    curr = "" + first
    x = 0
    if number:
        value = "INTEGER"
        num = True
        val = True
    if identifier:
        value = "IDENTIFIER" 
    while identifier or special:
        x = x+1
        if(x>100):
            print("broken")
            break
        fileInput = fileInput[1:]
        if len(fileInput)>0:
            token = fileInput[0]
            curr = curr + token
            identifier = re.fullmatch(r"[a-zA-Z][a-zA-Z0-9]*", curr)
            special = re.fullmatch(r"[^a-zA-Z0-9]*", curr)
            if identifier:
                value = "IDENTIFIER"
            elif special:
                value = "ERROR"
            else:
                identifier = None
        else:
            if identifier:
                if curr in keyWords:
                    val = True
                    value = keyWords.get(curr)[0] + ' token-code = ' + str(keyWords.get(curr)[1])
                else:
                    val = True
                    break
            if curr in special_sym:
                val = True
                value = special_sym.get(curr)[0]
            break


    while num:
        x = x+1
        if(x>100):
            print("broken")
            break
        fileInput = fileInput[1:]
        if len(fileInput)>0:
            token = fileInput[0]
            curr = curr + token
            integer = re.fullmatch('[1-9][0-9]*', curr)
            floats = re.fullmatch('([+|-])?(\d+([.]\d*)?([e]([+|-])?\d+)?|[.]\d+([eE]([+|-])?\d+)?)', curr)
            octal = re.fullmatch('0[0-7]+', curr)
            if integer:
                value = "INTEGER"
            elif octal:
                value = "OCTAL"
            elif floats:
                value = "FLOATING-POINT"
            else:
                Integer, floats, octal = (None, None, None)
            number = integer or floats or octal
        else:
            if number:
                val = True
            break

    if not val:
        print("Lexical Error")
        return 'ERROR'
    else:
        print(value + ' : ' + curr)

#Main method, where we access a test file to make sure our program works
if __name__ == "__main__":
    print("\nUnedited java file")
    word = open('Assignment3/Question1/test_input.txt', 'r')
    print(word.read())
    word.close()
    print("\nJave File tokenized:")
    with open('Assignment3/Question1/test_input.txt', 'r') as fileInput:
        words = re.split(';| |\n|\t',fileInput.read())
        for i in range (0, len(words)):
            if words[i]:
                    checker = tokenize(words[i]) 
                    if checker=='ERROR':
                        break
                    else:
                        continue  
            else:
                continue     
    pass
    


    
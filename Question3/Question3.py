import sys
import re


FLOAT = 2
IDENT = 1
INTEGER = 90
Left_parenthesis = 41
Right_parenthesis = 42
Plus_sign = 11
minus_sign = 12
Division_symbol = 14
Multiplication_symbol = 13

# This is a dictionary or hashmap containing our special symnols, and I map them to a string name and numerical token code
special_sym = {
    '+': ['Plus_sign', 11],
    '-': ['Minus_sign', 12],
    '(': ['Left_parenthesis', 41],
    ')': ['Right_parenthesis', 42],
    '{': ['Left_bracket', 43],
    '}': ['right_bracket', 44],
    '*': ['Multiplication_symbol', 13],
    '/': ['Division_symbol', 14],
    '$': ['Dollar_sign', 19],
    '%': ['Percent_symbol', 15],
    '=': ['Equal_sign', 17],
    '<': ['Less_than', 21],
    '>': ['Greater_than', 22],
    '<=': ['Less_Than_Equal', 23],
    '>=': ['Greater_Than_Equal', 24],
    }
# This is a dictionary or hashmap containing our key words, and I map them to a string name and numerical token code
keyWords = {
        'for': ['for-loop', 31],
        'if': ['if-statement', 32],
        'while': ['while-loop', 33],
        'do': ['do', 34],
        'int': ['integer', 35],
        'float': ['floating-point', 36],
        'switch': ['switch-statement', 37]
    }

#This is our recursive subprogram which is based on the following eBNF:: <selection_statement>  if ‘(‘ <boolexpr> ‘)’ <statement> [ else <statement> ]
def ifStatement():
    if(nextToken != If_Code):
        error()
    else:
        lex()
        if(nextToken != Left_parenthesis):
            error()
        else:
            lex()
            boolexpr()
            if(nextToken != Right_Parenthesis):
                error()
            else:
                lex()
                statement()
                if(nextToken == Else_Code):
                    lex()
                    statemment()

#This is our recursive subprogram which is based on the following eBNF:
def while_loop():
    if(nextToken != While_Code):
        error
    else:
        lex()
        if(nextToken != Left_parenthesis):
            error()
        else:
            lex()
            expression()
            if(nextToken != Right_Parenthesis):
                error()
            else:
                lex()
                statement()

#This is our recursive subprogram which is based on the following eBNF: <for_loop> --> for ‘(‘ [<expression>] ’;’ [<expression>] ‘;’ [<expression>] ‘)’ <statement> 
def for_loop():
    if(nextToken != For_Code):
        error()
    else:
        lex()
        if(nextToken != Left_parenthesis):
            error()
        else:
            lex()
            expression()
            if(nextToken != Semicolon):
                error()
            else:
                lex()
                statement()
                if(nextToken != Semicolon):
                    error()
                else:
                    lex()
                    expression()
                    if(nextToken != Right_parenthesis):
                        error()
                    else:
                        lex()
                        statment()
        
#incomplete program for the funtion statement
def statement():
    # The following will be similar to a switch statement
    if(nextToken == If_Code):
        ifStatement()
        
    elif(nextToken == While_Code):
        while_loop
        
    elif(nextToken == Left_Bracket):
        block()
        
    #.....
    else:
        error()

#Call to get the next lexeme/token code
def lex():
    global i, nextToken, arr
    i = i + 1
    if(i < len(arr)):
        nextToken = arr[i]
        print(nextToken)

'''This was taken from our lexical analyzer, This will classify the tokens, 
and give an array of the order of tokens'''
def tokenize(fileInput):
    global lexArray
    first = fileInput[0]
    num = False
    val = False
    number = re.fullmatch(r"[0-9]", first)
    identifier = re.fullmatch(r"[a-zA-Z]", first)
    special = re.fullmatch(r"[^a-zA-z0-9]", first)
    curr = "" + first
    x = 0
    if number:
        value = "INTEGER"
        num = True
        val = True
    if identifier:
        value = "IDENT"
        
    while identifier or special:
        x = x+1
        if(x > 100):
            print("broken")
            break
        fileInput = fileInput[1:]
        if len(fileInput) > 0:
            token = fileInput[0]
            curr = curr + token
            identifier = re.fullmatch(r"[a-zA-Z][a-zA-Z0-9]*", curr)
            special = re.fullmatch(r"[^a-zA-Z0-9]*", curr)
            if identifier:
                value = "IDENT"
            elif special:
                value = "ERROR"
            else:
                identifier = None
        else:
            if identifier:
                if curr in keyWords:
                    val = True
                    value = keyWords.get(curr)[0]
                else:
                    val = True
                    break
            if curr in special_sym:
                val = True
                value = special_sym.get(curr)[0]
            break

    while num:
        x = x+1
        if(x > 100):
            print("broken")
            break
        fileInput = fileInput[1:]
        if len(fileInput) > 0:
            token = fileInput[0]
            curr = curr + token
            integer = re.fullmatch('[1-9][0-9]*', curr)
            floats = re.fullmatch(
                '([+|-])?(\d+([.]\d*)?([e]([+|-])?\d+)?|[.]\d+([eE]([+|-])?\d+)?)', curr)
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
        #print("Lexical Error")
        return 'ERROR'
    else:
        lexArray.append(value)
        #print(value + ' : ' + curr)

#Turns the string value of the tokens into its integer token code
def convertor(array):
    newArray = []
    
    for i in range (0, len(array)):
        if(array[i]=='IDENT' ):
            newArray.append(1)
        elif(array[i]=='INTEGER'):
            newArray.append(90)
        elif(array[i]=='Left_parenthesis'):
            newArray.append(41)
        elif(array[i]=='Right_parenthesis'):
            newArray.append(42)
        elif(array[i]=='Plus_sign'):
            newArray.append(11)
        elif(array[i]=='minus_sign'):
            newArray.append(12)
        elif(array[i]=='Division_symbol'):
            newArray.append(14)
        elif(array[i]=='Multiplication_symbol'):
            newArray.append(13)
        elif(array[i]=='percent_symbol'):
            newArray.append(15)
        else:
            return None
    
    return newArray

#where the lex analyzer begins
def mainLexAnalzer():
    global lexArray
    lexArray = []
    print("\nUnedited java file")
    word = open('Assignment3/Question3/TestInput.txt', 'r')
    print(word.read())
    word.close()
    #print("\nJave File tokenized:")
    with open('Assignment3/Question3/TestInput.txt', 'r') as fileInput:
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

if __name__ =='__main__':
    mainLexAnalzer()
    print(lexArray)
    for i in range (0, len(lexArray)):
        if(lexArray[i]=='while-loop'):
            while_loop()
        elif(lexArray[i]=='for-loop'):
            for_loop()
        elif(lexArray[i]=='if-statement'):
            ifStatement()
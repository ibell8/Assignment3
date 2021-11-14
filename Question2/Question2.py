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

keyWords = {
        'for': ['for-loop', 31],
        'if': ['if-statement, 32'],
        'while': ['while-loop', 33],
        'do': ['do', 34],
        'int': ['integer', 35],
        'float': ['floating-point', 36],
        'switch': ['switch-statement', 37]
    }


def lex():
    global i, nextToken, arr
    i = i + 1
    if(i < len(arr)):
        nextToken = arr[i]
        print(nextToken)


def expr():
    print("Enter <expr>")
    # Parse the first term */
    term()
    ''' As long as the next token is + or -, get
     the next token and parse the next term '''
    while(nextToken == Plus_sign or nextToken == minus_sign):
        lex()
        term()

    print("Exit <expr>")

# <term> -> <factor> {(* | /) <factor>}


def term():
    print("Enter <term>")
    # Parse the first factor */
    factor()
    # As long as the next token is * or /, get the next token and parse the next factor
    while (nextToken == Multiplication_symbol or nextToken == Division_symbol):
        lex()
        factor()

    print("Exit <term>")

# <factor> -> id | int_constant | ( <expr> )


def factor():
    print("Enter <factor>")
    # Determine which RHS
    if (nextToken == IDENT or nextToken == INTEGER):
        # Get the next token
        lex()
        # If the RHS is ( <expr> ), call lex to pass over the left parenthesis, call expr, and check for the right parenthesis
    else:
        if (nextToken == Left_parenthesis):
            lex()
            expr()  # left par
            if (nextToken == Right_parenthesis):
                lex()
            else:
                error()
        # It was not an id, an integer literal, or a left parenthesis '''
        else:
            error()

    print("Exit <factor>")


def exiter():
    sys.exit()


def error():
    print("Syntactical error: This is not a valid expression!")
    exiter()


def mainSynAnalyzer(array):
    # arr = [26, 11, 21, 11, 27]
    # arr = [26, 11, 21, 12, 27, 24, 11, -1]
    global i, nextToken, arr
    arr = array
    i = 0
    nextToken = arr[0]
    print(nextToken)
    expr()
    # expr = (leftPar, ident, add, ident, rightPar)


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
                    value = keyWords.get(curr)[0] + ' token-code = ' + \
                                         str(keyWords.get(curr)[1])
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
        print("Lexical Error")
        return 'ERROR'
    else:
        lexArray.append(value)
        print(value + ' : ' + curr)

   

def mainLexAnalzer():
    global lexArray
    lexArray = []
    print("\nUnedited java file")
    word = open('Assignment3/Question2/testInput.txt', 'r')
    print(word.read())
    word.close()
    print("\nJave File tokenized:")
    with open('Assignment3/Question2/testInput.txt', 'r') as fileInput:
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

       
if __name__ == "__main__":
    array = mainLexAnalzer() 
    newLexArray = convertor(lexArray)
    newLexArray.append(-1)
    mainSynAnalyzer(newLexArray)


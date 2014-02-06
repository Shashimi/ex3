import string
from arithmetic import *


while True:
    user_input = raw_input("> ")

    tokens = string.split(user_input)

    if tokens[0] == "+":
        if len(tokens) < 3:
            print "Please enter at least two numbers to add. For example:   + 1 2"
        else:
            tokens.pop(0)
            answer = int(tokens.pop(0))
            for i in tokens:
                answer += int(i)
            print answer

    elif tokens[0] == "-":
        if len(tokens) < 3:
            print "Please enter at least two numbers to subtract. For example:   - 3 1"
        else:
            tokens.pop(0)
            answer = int(tokens.pop(0))
            for i in tokens:
                answer -= int(i)
            print answer

    elif tokens[0] == "*":
        if len(tokens) < 3:
            print "Please enter at least two numbers to multiply. For example:   * 4 2"
        else:
            tokens.pop(0)
            answer = int(tokens.pop(0))
            for i in tokens:
                answer *= int(i)
            print answer

    elif tokens[0] == "/":
        if len(tokens) < 3:
            print "Please enter at least two numbers to divide. For example:   / 4 2"
        else:
            tokens.pop(0)
            answer = float(tokens.pop(0))
            for i in tokens:
                answer /= int(i)
            print answer

    elif tokens[0] == "square":
        if len(tokens) != 2:
            print "Please enter one number to square. For example:   square 3"
        else:
            tokens[1] = int(tokens[1])
            print square(tokens[1])

    elif tokens[0] == "cube":
        if len(tokens) != 2:
            print "Please enter one number to cube. For example:   cube 2"
        else:
            tokens[1] = int(tokens[1])
            print cube(tokens[1])

    elif tokens[0] == "power":
        if len(tokens) != 3:
            print "Please enter exactly two numbers. For example:   power 2 5"
        else:
            tokens[1] = int(tokens[1])
            tokens[2] = int(tokens[2])
            print power(tokens[1], tokens[2])

    elif tokens[0] == "mod":
        if len(tokens) != 3:
            print "Please enter exactly two numbers. For example:   mod 5 3"
        else:
            tokens[1] = int(tokens[1])
            tokens[2] = int(tokens[2])
            print mod(tokens[1], tokens[2])

    elif tokens[0] == "q":
        exit()

    else:
        print "Sorry, I'm not sure what that means. Please enter a valid argument."

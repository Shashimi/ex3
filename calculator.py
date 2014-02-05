import arithmetic.py

# take user's input
# tokenize input
# check to see if they input the right # of args for that function
# perform calculation

while True:
    user_input = raw_input("> ")

    tokens = input.split(" ")

    if tokens[0] == "+":
        pass
    elif tokens[0] == "-":
        pass
    elif tokens[0] == "*":
        pass
    elif tokens[0] == "/":
        pass
    elif tokens[0] == "%":
        pass
    elif tokens[0] == "square":
        pass
    elif tokens[0] == "cube":
        pass
    elif tokens[0] == "power":
        pass
    elif tokens[0] == "mod":
        pass
    elif tokens[0] == "q":
        exit()
    else:
        print "Sorry, I'm not sure what that means. Please enter a valid argument."

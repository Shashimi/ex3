def add(*args):
    thesum = 0
    for num in args:
        thesum += num
    return thesum

def subtract(*args):
    answer = args[0]
    for i in range(1, len(args)):
        answer -= args[i]
    return answer

def multiply(*args):
    theproduct = 1
    for num in args:
        theproduct *= num
    return theproduct 

def divide(*args):
    thequotient = args[0]
    for i in range(1, len(args)):
        thequotient /= args[i]
    return thequotient

def square(num1):
    return num1 * num1 

def cube(num1):
    return num1 * num1 * num1 

def power(num1, num2):
    # thenum = 1
    # for i in range(num2):
    #     thenum *= num1
    # return thenum

    return pow(num1, num2)

def mod(num1, num2):
    return num1 % num2 

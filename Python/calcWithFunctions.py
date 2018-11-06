def zero(content=None): 
    try: 
        content = "0" + content 
        return int(eval(content))
    except TypeError:
        return "0"

def one(content=None):
    try: 
        content = "1" + content 
        return int(eval(content))
    except TypeError:
        return "1"

def two(content=None): #your code here
    try: 
        content = "2" + content 
        return int(eval(content))
    except TypeError:
        return "2"

def three(content=None): #your code here
    try: 
        content = "3" + content 
        return int(eval(content))
    except TypeError:
        return "3"

def four(content=None): #your code here
    try: 
        content = "4" + content 
        return int(eval(content))
    except TypeError:
        return "4"

def five(content=None): #your code here
    try: 
        content = "5" + content 
        return int(eval(content))
    except TypeError:
        return "5"

def six(content=None): #your code here
    try: 
        content = "6" + content 
        return eval(content)
    except TypeError:
        return "6"

def seven(content=None): #your code here
    try: 
        content = "7" + content 
        return eval(content)
    except TypeError:
        return "7"

def eight(content=None): #your code here
    try: 
        content = "8" + content 
        return int(eval(content))
    except TypeError:
        return "8"

def nine(content=None): #your code here
    try: 
        content = "9" + content 
        return int(eval(content))
    except TypeError:
        return "9"

#___________________________

def plus(content): 
    return ("+ " + content)

def minus(content):
    return ("- " + content)

def times(content):
    return ("* " + content)

def divided_by(content):
    return ("/ " + content)

print(seven(times(six())))
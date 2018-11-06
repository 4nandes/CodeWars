import random

class befungeInterpreter:

    def __init__(self, code):
        #this is the default direction and should be changed as the interpreter goes through the program
        self.direction = "right"
        self.stack = []
        self.code = [str(x) for x in code.split("\n")]
        self.xPos = 0
        self.yPos = 0
        self.response = ""

    def run(self):
        self.processCommand()
        while (self.code[self.yPos][self.xPos] != "@"):
            self.updateCursorPosition()
            self.processCommand()
        return self.response

    def updateCursorPosition(self):
        """
        This is bad practice and honestly should be made in some way that is a lot cleaner
        For some reason I get afraid of any amount of if/else statements because
        it makes me feel like I am writing bad code
        
        But on the real what this function does is it gets the current direction that the pointer is going in
        and it updates the current position of the pointer accordingly
        """
        if self.direction == "right":
            self.xPos += 1

        elif self.direction == "left":
            self.xPos -= 1
        
        elif self.direction == "up":
            self.yPos -= 1 
        
        elif self.direction == "down":
            self.yPos += 1

    def getVals(self):
        try:
            a = self.stack.pop(0)
        except IndexError:
            a = 0
        try:
            b = self.stack.pop(0)
        except IndexError:
            b = 0
        return a, b

    def processCommand(self):
        command = self.code[self.yPos][self.xPos]
        # Uncomment these if you would like to see the debugging output
        ##########################################
        # print((self.yPos,self.xPos), end='')
        # print(command)
        ##########################################
        if command.isnumeric():
            self.stack.insert(0, int(command))
            return
        elif command == "^":
            self.direction = "up"
            return
        elif command == ">":
            self.direction = "right"
            return
        elif command == "v":
            self.direction = "down"
            return
        elif command == "<":
            self.direction = "left"
            return
        elif command == ".":
            self.response += str(self.stack.pop(0))
            return
        elif command == ":":
            if len(self.stack) == 0:
                self.stack.insert(0, 0)
                return
            self.stack.insert(0, self.stack[0])
            return
        elif command == "_":
            if (self.stack.pop(0) == 0):
                self.direction = "right"
                return
            self.direction = "left"
            return
        elif command == "+":
            a,b = self.getVals()
            self.stack.insert(0, (a + b))
            return
        elif command == "-":
            a,b = self.getVals()
            self.stack.insert(0, (b-a))
            return
        elif command == "*":
            a,b = self.getVals()
            self.stack.insert(0, (a*b))
            return
        elif command == "/":
            a,b = self.getVals()
            if (a == 0):
                self.stack.insert(0,0)
                return
            self.stack.insert(0,(b/a))
            return
        elif command == "%":
            a,b = self.getVals()
            if (a == 0):
                self.stack.insert(0,0)
                return
            self.stack.insert(0, (b%a))
        elif command == "!":
            if (self.stack.pop(0) == 0):
                self.stack.insert(0,1)
                return
            self.stack.insert(0,0)
            return
        elif command == "`":
            a,b = self.getVals()
            if (b>a):
                self.stack.insert(0,1)
                return
            self.stack.insert(0,0)
            return
        elif command == "?":
            self.direction = {1:"up",2:"down", 3:"left",4:"right"}[random.randint(1,4)]
        elif command == "|":
            if (self.stack.pop(0) == 0):
                self.direction = "down"
                return
            self.direction = "up"
            return
        elif command == '"':
            self.updateCursorPosition()
            while (self.code[self.yPos][self.xPos] != '"'):
                self.stack.insert(0, ord(self.code[self.yPos][self.xPos]))
                self.updateCursorPosition()
        elif command == "\\":
            self.stack[0],self.stack[1] = self.stack[1], self.stack[0]
            return
        elif command == "$":
            self.stack.pop(0)
            return
        elif command == ",":
            self.response += chr(self.stack.pop(0))
            return
        elif command == "#":
            self.updateCursorPosition()
        elif command == "p":
            y,x = self.getVals()
            v = self.stack.pop(0)
            self.code[y] = self.code[y][0:x] + chr(v) + self.code[y][x+1:]
            return
        elif command == "g":
            y,x = self.getVals()
            self.stack.insert(0, ord(self.code[y][x]))
            return
    

def main():
    print("The example code has been commented out in main()")
    # Counts to 9 then outputs the numbers
    ###################################
    # test = befungeInterpreter('>987v>.v\nv456<  :\n>321 ^ _@')
    # print(test.run())
    ###################################

    #  Basic Hello World
    ###################################
    # test = befungeInterpreter('>25*"!dlroW olleH":v\n                v:,_@\n                >  ^ ')
    # print(test.run())
    ###################################

    # Do not run this unless you want to make the terminal hang
    ###################################
    # test.loadCode("v>>>>>v\n 12345 \n ^?^   \n> ? ?^ \n v?v   \n 6789  \n >>>> v\n^    .<")
    # test.run()
    ###################################

if __name__ == '__main__':
    main()
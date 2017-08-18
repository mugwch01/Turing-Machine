#My name is Charles Mugwagwa. This is an implementation of a Turing Machine that reverses words with the letters: 'r','e','v','s'.

delta = {(0,'$'):(0,'$','R'),(0,'r'):('r','$','L'),(0,'e'):('e','$','L'),(0,'v'):('v','$','L'),(0,'s'):('s','$','L'),(0," "):('clean'," ",'*'),(1,'$'):(0,'$','R'),(1,'r'):(1,'r','R'),(1,'e'):(1,'e','R'),(1,'v'):(1,'v','R'),(1,'s'):(1,'s','R'),('r','$'):('r','$','L'),('r','r'):('r','r','L'),('r','e'):('r','e','L'),('r','v'):('r','v','L'),('r','s'):('r','s','L'),('r'," "):(1,'r','R'),('e','$'):('e','$','L'),('e','r'):('e','r','L'),('e','e'):('e','e','L'),('e','v'):('e','v','L'),('e','s'):('e','s','L'),('e'," "):(1,'e','R'),('v','$'):('v','$','L'),('v','r'):('v','r','L'),('v','e'):('v','e','L'),('v','v'):('v','v','L'),('v','s'):('v','s','L'),('v'," "):(1,'v','R'),('s','$'):('s','$','L'),('s','r'):('s','r','L'),('s','e'):('s','e','L'),('s','v'):('s','v','L'),('s','s'):('s','s','L'),('s'," "):(1,'s','R'),('clean'," "):('clean'," ",'L'),('clean','$'):('clean'," ",'L'),('clean','r'):('dollar','r','R'),('clean','e'):('dollar','e','R'),('clean','v'):('dollar','v','R'),('clean','s'):('dollar','s','R'),('dollar'," "):('dollar2','$','L'),('dollar','r'):('dollar','r','L'),('dollar','e'):('dollar','e','L'),('dollar','v'):('dollar','v','L'),('dollar','s'):('dollar','s','L'),('dollar2'," "):('halt-accept','$','L'),('dollar2','r'):('dollar2','r','L'),('dollar2','e'):('dollar2','e','L'),('dollar2','v'):('dollar2','v','L'),('dollar2','s'):('dollar2','s','L')}

class TuringMachine:
    def __init__(self):
        self.tape = Tape()       
        self.head = self.tape.head
        self.startStateId = 0
    def run(self): 
        self.tape.head = 46        
        initialSymbols = ['$','r','e','v','e','r','s','e','$']
        #initialSymbols = ['$','v','e','r','s','e','s','$']
        #initialSymbols = ['$','s','e','r','v','e','$']
        #initialSymbols = ['$','s','r','v','$']
        for symbol in initialSymbols:
            self.tape.write(symbol)
            self.tape.moveRight()       
        for symbol in initialSymbols:#back to starting point
            self.tape.moveLeft()           
        currentSymbol = self.tape.read()
        state = self.startStateId 
        while state != 'halt-accept': #while not accepting state           
            state,newSymbol,direction = delta[(state, currentSymbol)]                      
            self.tape.write(newSymbol)           
            if not direction == '*':
                if direction == 'R':
                    self.tape.moveRight()                    
                elif direction == 'L':
                    self.tape.moveLeft()                   
            currentSymbol = self.tape.read()            
            if currentSymbol == '': #fix for small bug that affets indexing
                currentSymbol = " "      

class Tape:
    def __init__(self):
        self.array = ['']*100        
        self.head = 50
    def moveRight(self):
        if self.head != len(self.array)-1:
            self.head += 1                       
        else:           
            self = self.enlargeTape()          
    def moveLeft(self):
        if self.head != 0:
            self.head -= 1            
        else:
            self.enlargeTape()             
    def __str__(self):
        outputString = "|"
        self.head = 0
        while self.array[self.head] != '$':
            self.moveRight()        
        outputString = outputString+self.read()+"|"
        self.moveRight()        
        while self.array[self.head] != '$':            
            outputString = outputString+self.read()+"|"
            self.moveRight()
        outputString = outputString+self.read()+"|"
        return outputString
    def write(self, symbol):
        self.array[self.head] = symbol              
    def read(self):       
        return self.array[self.head]         
    def enlargeTape(self): 
        oldSize = len(self.array)
        newSize = 2*oldSize
        leftCellsIncrement = 0
        aSymbol = False
        for x in self.array:            
            if x != "":
                aSymbol = True
                break
        if not aSymbol: #check if array has atleast one non-blank symbol
            self.array = self.array * 2
            self.head = ((1/2)*oldSize)+ self.head
            return self
        leftSpaces = 0 
        while self.array[leftSpaces] == '': #counting cells without symbols for balancing.left side
            leftSpaces += 1
        rightSpacesIndex = oldSize - 1
        rightSpaces = 0
        while self.array[rightSpacesIndex] == '': #counting cells without symbols for putting contents in the middle.
            rightSpacesIndex -= 1
            rightSpaces += 1        
        if leftSpaces > rightSpaces:
            newCells = 0
            for x in range(0,leftSpaces-rightSpaces,1): #counting cells without symbols for putting contents in the middle.
                self.array.append(" ")
                newCells +=1
            amountLeft = 100-newCells           
            alist = [" "]*int(amountLeft/2)
            self.array = alist + self.array + alist            
            self.head = self.head + leftCellsIncrment 
        else: # rightSpaces > leftSpaces
            newCells = 0
            for x in range(0,rightSpaces-leftSpaces,1):#putting symbols in the middle of the tape
                self.array.insert(0," ")
                leftCellsIncrement += 1
                newCells +=1
            amountLeft = 100-newCells           
            alist = [" "]*int(amountLeft/2)
            self.array = alist + self.array + alist
            leftCellsIncrement = int(amountLeft/2)                  
            self.head = self.head + leftCellsIncrement                
        return self
        
def main():    
    tMachine = TuringMachine()
    tMachine.run()   
    print(tMachine.tape)
    print('End of the Program.')    
if __name__ == "__main__":
    main()                
        
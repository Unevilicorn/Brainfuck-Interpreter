# ProgStr = the brainfuck code
# Buffer = an array of 0s
def BF(progStr, buffer):
    
    pointer = 0
    lookUp = {}
    
    BuildLookUp(progStr, lookUp)
    
    index = 0
    # Loop till the end of the string
    while index < len(progStr):
        char = progStr[index]
        if(char == '>'):
            pointer += 1
        elif(char == '<'):
            pointer -= 1
        elif(char == '+'):
            buffer[pointer] += 1
        elif(char == '-'):
            buffer[pointer] -= 1
        elif(char == '.'):
            print(chr(buffer[pointer]))
        elif(char == ','):
            DoInput(buffer, pointer)            

        elif(char == ']'):
            if index in lookUp:
                if not buffer[pointer] == 0 :
                    # Jump to the corrosponding bracket
                    index = lookUp[index] 
            else:
                raise Exception("Mismatch brackets at position " + str(index + 1))


        index += 1


# Build a lookup table so no need to find it during run time
def BuildLookUp(progStr, lookUp):
    # Find the first occurence of the open bracket to start the recursion
    firstBracketIndex = progStr.find('[')
    
    if(firstBracketIndex == -1):
        return
    
    AddToLookUp(progStr, lookUp, firstBracketIndex)


# Recursivly adding bracket pair location to a lookup dictionary                
def AddToLookUp(progStr, lookUp, curPos):
    
    for index in range(curPos+1, len(progStr)):
        char = progStr[index]

        # Makes sure that the current character isn't checked
        if index not in lookUp:
            
            # Recursively find the nested bracket pair
            if(char == '['):
                closePos = AddToLookUp(progStr, lookUp, index)
                #Set current index to the new found close bracket index
                index = closePos + 1
                
            elif(char == ']'):
                # Save both indecies to allow 2 way look up
                lookUp[index] = curPos
                lookUp[curPos] = index
                
                # return the closing bracket position to skip unnecessary checks
                return curPos
        
    raise Exception("Missing close bracket at index " + str(curPos))
    
# Handles single character input
# either takes the first character
# or just set to 0
def DoInput(buffer, pointer):
    a = input("Enter a character: ")
    
    if(len(a)==0):
        buffer[pointer] = 0
    else:
        buffer[pointer] = ord(a[0])

if __name__ == "__main__":
    # execute only if run as a script
    BF(input("Enter the brainfuck code:\n"), [0]*1000)

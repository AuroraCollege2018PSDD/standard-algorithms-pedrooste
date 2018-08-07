""" Basic code that demonstrates the use of subroutines
"""

__author__ = "Pedro"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "pedro.oste@education.nsw.com.au"
__status__ = "Development"

#subroutines
def loadArray():
    ''' This subroutine allows the user to enter numbers into an array.
it also checks if the input entered is a number or a character before adding to the array'''
    loop = True
    while loop:
        arrayNumber = input("What number would you like to add the array?\n Press q to go back to the main menu:\n ")
        if arrayNumber == 'q':
            loop = False
        elif arrayNumber.isnumeric():
            arrayNumber = int(arrayNumber)
            array.append(arrayNumber)
            print('Your number has been sucessfully added')
        else:
            print('Incorrect input')

def printArray():
    ''' This subroutine prints the array and also prints how long the array is'''
    print(*array)
    if len(array) <= 1:
        print('The total length of the array is',(len(array)),'number long')
    else:
        print('The total length of the array is',(len(array)),'numbers long')
    
def sumArray():
    '''This subroutine adds together all of the numbers within the array'''
    print('The total sum of this array is',(sum(array)))
    if len(array) <= 1:
        print('The total length of the array is',(len(array)),'number long')
    else:
        print('The total length of the array is',(len(array)),'numbers long')

def maximum():
    print('This feature has not be implemented yet')
    
def minimum():
    print('This feature has not be implemented yet')
    
#sets up a blank array
array = []
play = True
question = "What action would you like to perform:\n I - Add a number to an array\n P - Print the array and the array length\n A - Add the numbers within the array\n H - Find the maximum value within the array\n L - Find the lowest value witin the array\n Q - Quit the programe\n : "
while play:
    choice = input(question)
    choice = choice.lower() #whatch out for those nasties with caps
    if choice == "q":
        play = False #exits the loop
    elif choice == "i":
        loadArray()
    elif choice == "p":
        printArray()
    elif choice == "a":
        sumArray()
    elif choice == "h":
        maximum()
    elif choice == "l":
        minimum()
    else:
        print('That is not an option')
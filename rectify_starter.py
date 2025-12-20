def rectify(stream, nb_rows, nb_cols):
"""Display contents of character stream in rows and columns.
This function is used to rectify two-dimensional content that had been
flattened into a one-dimensional stream of characters.
"""
c = getc(stream) # This statement reads the next character from the file
# and stores it in the variable c. (The function that does
# this is implemented below and you are allowed to look at
# it, if you are curious, but you are not required to
# understand how it works.)
print(c,end='') # This statement prints the character stored in the
# variable c to the command window. The end='' argument
# prevents the print function from moving the print
# location down one line when finished. This way,
# consecutive calls will result in characters printed
# left-to-right (in a row) instead of downwards.
print() # An empty print() call just moves the next print location
# down to the next line. This will affect the *next*
# printing command, not anything that was already printed.
# YOUR TASK: use the three provided statements repeatedly, using loops, to
# print the contents of stream in nb_rows rows of nb_cols columns.
for i in range(nb_rows): #outer loop for each row
for j in range(nb_cols): #inner loop for each colum
c= getc(stream) #reads next character from stream
print(c, end ='') #prints character w/o a new line
print() #moves to next line after each row
return
### Your work is finished. Below are functions and statements we use to test
### your solution. Feel free to look, but know that if you make any changes
### here they will just be overwritten by our grader. The assignment
### description explains how the submitted script will be called and what the
### expected results should be. That is all you need to know.
def getc(stream):
return stream.read(1)
def _rectify():
fname = input("Name of file to rectify: ")
Mega = int(input("How many rows? "))
nano = int(input("How many columns? "))
with open(fname, 'r') as S:
rectify(S, Mega, nano)
pass
if __name__ == '__main__':
_rectify()

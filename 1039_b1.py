'''
    Aim   : Practice Programs
    Name  : Ankush Patil
    Prn   : 1541039
    Batch : T2

    Feature : v1.3 user validation added with terminal clearance

'''
#importing libraries
import os
import math


def Display_menu():
    dec = 'y'
    while(checkDecision(dec)):
        
        #clearing the terminal 
        os.system('clear')

        print "_______________MENU_________________"
        print "\n1.Find square root of no : "
        print "2.Find area of rectangle : "
        print "3.Swap two nos : "
        print "4.Data Structures: list,dictonaries,tuples"
        print "5.Find No. is even or odd"
        print "6.Largest among three no.s"
        print "7.Check if year is leap or not"
        print "8.Fibonacci Sequence"
        print "9.While loop"
        print "10.Prime no upto n nos:"
        print "11.Perform operations on word \"govenrmentcollege\" "
        

        try:
            choice = int(input("Enter your choice : "))

        except NameError:
            print ""
            print "That's not a number"
            continue
        
        print ""
        print "_____________________________________"
        print ""
        #summing it up in options dictionery
    
        options = { 1  : findSqrt,
                    2  : findArea,
                    3  : swapper,
                    4  : useDS,
                    5  : findEvenOdd,
                    6  : findLargest,
                    7  : isLeap,
                    8  : findFibbo,
                    9  : useWhile,
                    10 : findPrimeUptoN,
                    11 : operation
        }

        #checking choice is available or not
        try:
            options[choice]()
        except:
            print ""
            print "Invalid Choice Please Enter Valid One"

        print "______________________________________"
        print ""
        dec = raw_input("Do you want to try again (y/n) : ")
        print ""




#supportive functions 
def checkDecision(ans):
    #converting ans to lower first
    if ans.lower() == 'y':
        return True 
    else:
        return False

def findSqrt():
    
    try:
        number = int(input("Enter a number to find its square root : "))
    except NameError:
        print ""
        print "That's not a number."

    sqrt = math.sqrt(number)
    print "Square root of the number is "+str(sqrt)

def findArea():
    print "in"

def findEvenOdd():
    print "in"

def findLargest():
    print "in"

def findFibbo():
    print "in"

def swapper():
    print "in"

def isLeap():
    print "in"

def useDS():
    print "in"

def useWhile():
    print "in"

def findPrimeUptoN():
    print "in"

def operation():
    print "in"



if __name__=="__main__":
    Display_menu()
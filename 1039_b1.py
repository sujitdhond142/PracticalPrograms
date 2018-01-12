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
    numbers = raw_input("Enter width and height of the rectangle separating space : ").split()
    
    try:
        width = int(numbers[0])
        height = int(numbers[1])
    except NameError:
        print ""
        print "One is not a number out of width and height"
    area = width * height
    print "The area of the rectangle is "+ str(area)

def findEvenOdd():
   
    try:
        number = int(raw_input("Enter a number to check its parity : "))
        if(number%2==1):
            print "The number is odd"
        else:
            print "The number is even"
    except NameError:
        print ""
        print "Please enter a valid number"


def findLargest():
    numbers = raw_input("Enter three number with spaces inbetween :").split()
    try:
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        n3 = int(numbers[2])

        if n1>n2 and n1 >n3:
            print str(n1) + " is greater."
        elif n1<n2 and n2>n3:
            print str(n2) + " is greater."
        else:
            print str(n3) + " is greater."
    
    except NameError:
        print ""
        print "Please enter valid numbers"

def findFibbo():
    b=1
    i=0
    num=int(input("Enter a no : "))
    print("Fibonacci series :")
    a=1
    for i in range(num):
        print str(a) + ", ",
        tmp=b
        b=a+b
        a=tmp
    print ""


def swapper():
    number = raw_input("Enter the two number to swap : ").split()
    try:
        n1 = int(number[0])
        n2 = int(number[1])
        print "Number before swapping : n1=" + str(n1) + " and n2=" + str(n2)
        n1,n2=n2,n1
        print "Number after swapping :  n1=" + str(n1) + " and n2=" + str(n2)
    except NameError:
        print ""
        print "Error:Please enter the valid numbers"

def isLeap():
    a=int(input("Enter year : "))
    if a%4==0:
        if a%400==0:
            print("Not a leap year")
        else:
            print("It's a leap year")	
    else:
            print("Not a leap year")
  

def useDS():
    print("Data structures : ")
    a=[20,"Here I am second in the a.",223]
    print("1. List  :")
    print(a)
    b=(4,"Here I am second in the b.",21326)
    print("2. Tuple :")
    print(b)
    c={1:"one",2:"two",3:"three"}
    print("3. Dictionary :")
    print(c)

def useWhile():
    num=6
    while num > 0:
        num=num-1
        print("I am in while loop")
    else:
        print("I am in else loop")


def findPrimeUptoN():
    num = int(input("Enter your range : "))
    flag=0
    for i in range(num):
        count = 0
        for j in range(i):
            if i%(j+1)==0:
                count=count+1
        if count==2:
            flag=flag+1
    print(" Prime nos in given range : ",flag)

def operation():
    string = "governmentcollege"
    print("Second letter of word is : ",string[1:2])
    print("First four letters are : ",string[:4])
    print("Last six letters are :",string[-6::1])



if __name__=="__main__":
    Display_menu()
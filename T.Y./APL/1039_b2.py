'''
	Aim   : Program to demonstrate the use of functions and various datastructures like lists,tuples and dictonaries
	Name  : Ankush Patil
	Prn   : 1541039
	Batch : T2

	Feature : v1.3 user validation added with terminal clearance

'''

#importing libraries to clear terminal
import os

def displayMenu():
	dec = 'y'
	while(checkDecision(dec)):
		#clearing the terminal
		os.system('clear')
		print "________________MENU_________________"
		print "\n1.To demonstrate use of functions  "
		print "2.To demonstrate use of data structures  "

		options = { 1 : useFunction,
					2 : useDatastructures
		}
		#take input as choice with validation)
		choice = takeInput("Enter your choice :")

		if choice != -1:
			try:
				options[choice]()
			except:
				print ""
				print "Please enter valid choice."

		print "____________________________________________"
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
def takeInput(msg):
	try:
		user_input = int(raw_input(msg))
	except:
		print ""
		print "Error : You entered something else other than number"
		return -1
	return user_input

#programm functions

def useFunction():
	print "\nDemonstration of function by calculating the max subarray sum in an array and minimum value in the array "
	n = takeInput("\nEnter size of array : ")
	if n!=-1:
		numbers = raw_input("Enter the ele. of array : ").split()
		max_sum,minn = calculateMaxSubarraySum(numbers) #passing the array in string format
		print "The maximum subarray sum of the array is : " + str(max_sum)
		print "And the minimum value of the array is :" + str(minn)
	else:
		print "Error: Size must be a number"

def calculateMaxSubarraySum(numbers):

	#algo to calculate max subarray sum complexity O(n)
	best = 0
	max_sum = 0;
	m = 1000000
	for k in xrange(0,len(numbers)):
		max_sum = max(int(numbers[k]),max_sum+int(numbers[k]));
		best = max(best,max_sum);
	for k in numbers:
		m = min(m,int(k))
	return best,m   #returning an the best

def useDatastructures():

	print "\nWhich one do you want to use :"
	print "1. List as stack"
	print "2. Demonstrate tuples"
	print "3. Book's list using dictonaries"

	sub_options = { 1 : useLists
	}
	#take input as choice with validation)

	sub_choice = takeInput("Enter your choice :")
	if sub_choice != -1:
		try:
			sub_options[sub_choice]()
		except:
			print ""
			print "Please enter valid choice."

	print "____________________________________________"
	print ""

def useLists():
    
	stack = []  #defining list as stack
	
	ans = 'y'
	
	while ans=='y' or ans=='Y':
		print "\nCall from below "
		print "1.Push 2. Pop 3. PrintStck "

		call_nu = takeInput("Enter choice :")
		if call_nu != -1:
			
			if call_nu == 1:
    			
				n = int(raw_input("Enter number to push : "))
				stack.append(n)
			
			elif call_nu == 2:
    		
				n = stack.pop()
				print str(n)+ " is popped out."
			elif call_nu == 3:
    		
				for i in stack:
    		
					print i
		else:
			print "Invalid Choice"
		print ""
		ans = raw_input("Try again ? (y/n) : ")



if __name__=="__main__":
	displayMenu()
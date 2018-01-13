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
		print "\n1.Find occurence of character with use of functions  "
		print "2.To demonstrate use of data structures  "

		options = { 1 : useFunction,
					2 : useDatastructures
		}
		#take input as choice with validation)
		choice = takeInput("Enter your choice :")

		if choice != -1:
			options[choice]()

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
	str1=raw_input("Enter first string: ")
	str2=raw_input('Enter character to check occurences :')
	
	occ = count(str1,str2)
	
	print "The number of Occurences of str2 in str 1 are :" + str(occ)


def count(text, ch, ignore_case=True):
	if ignore_case:
		text = text.lower()
		ch = ch.lower()
	n = 0
	for t in text:
		if ch == t:
			n += 1
	return n


def useDatastructures():

	print "\nWhich one do you want to use :"
	print "1. Lists"
	print "2. Demonstrate tuples"
	print "3. Marks table using dictionaries"

	sub_options = { 1 : useLists,
					2 : useTuples,
					3 : useDictonaries
	}
	#take input as choice with validation)

	sub_choice = takeInput("Enter your choice :")
	if sub_choice != -1:
		sub_options[sub_choice]()

	print "____________________________________________"
	print ""


def min_max(numbers):
	smallest = largest = numbers[0]
	for item in numbers:
		if item > largest:
			largest = item
		elif item < smallest:
			smallest = item
	return smallest, largest

def useLists():
	
	ans = 'y'
	while ans=='y' or ans=='Y':
		minn, maxx = min_max([1, 2, 7, 6, 3, 1, 2, 8, 4])
		print "Minimum = "+str(minn)+" and Maximum is :" +str(maxx)
		ans = raw_input("Try again ? (y/n) : ")

def useTuples():
	
	'''
	months = ('January','February','March','April','May','June',\
				'July','August','September','October','November','  December')
	
	date = raw_input("\nEnter you birthdate (dd-mm-yyyy) : ").split("-")
	print "<(0 _ 0)> You launched in this world in " + months[int(date[1])-1] + " , "+ date[2]

	# calculating month name and year using number 
	'''

	print "\nEnter the colour in rgb format :"
	r = int(raw_input("r = "))
	g = int(raw_input("g = "))
	b = int(raw_input("b"))
	if(r>255 or g>255 or b>255):
		print "Invalid colour format"
	rgb = r,g,b
	print "The rgb tupple is :"
	print rgb  

def useDictonaries():
	d = { }

	print "\nEnter inputs :"

	ans = 'y'
	while ans == 'y' or ans == 'Y':
			
		prn = raw_input("\nEnter prn : ")
		marks = raw_input("Enter marks  : ")
		d[prn]=marks

		ans = raw_input("want to add more entries y/n : ")

	print "\nThe dictonaries after entries is : "
	for key in d.iterkeys():
		print "%s : %s " % (key,d[key])

	print "\nThe dictonary after sorting : "
	
	for key in sorted(d.iterkeys()):
		print "%s : %s" % (key, d[key])


if __name__=="__main__":
	displayMenu()
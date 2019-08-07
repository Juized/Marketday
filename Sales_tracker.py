#!/usr/bin/python3
import sys
import os
import time
p= {}

try:
	f = open("sales_list.txt","r")
	for line in f:
		p.append(line.strip())
	f.close()
except:
	pass

def mainScreen():
	os.system('clear') # for linux 'clear'
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("     Day at the Market   ")
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("Please choose from the following options:\n")
	print("Total Sales for the Day: € ", totalsales())
	print("(a)dd to the list")
	print("(v)iew the list")
	print("(s)um all Sales")
	print("(q)uit the program")
	choice = input("\nchoice: ")
	if len(choice) > 0:
		if choice.lower()[0] == "a":
			newsale()
		elif choice.lower()[0] == "v":
			viewScreen()
		elif choice.lower()[0] == "s":
		    profits()
		elif choice.lower()[0] == "q":
			sys.exit()
		else:
			mainScreen()
	else:
		mainScreen()


def newsale():
    global p
    os.system('clear')
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     New Sale        ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print('Press enter to return to the main menu')
    item = input('Item name or Description?')
    if len(item) >0:
        price = int(input('What price was it sold for?'))
        p[item]= price
        print(item,' added to todays sales! :)')
        write()
        time.sleep(1)
        newsale()
    else:
        mainScreen()

def viewScreen():
    os.system('clear')
    print('Todays sales are saved in shopping_list.txt in this folder')
    print('A new list will be saved to the old list everytime the program is run.')
    print('Current items in the list include:\n')
    os.system('cat sales_list.txt')
    print("Press enter to return to the main menu")
    input()
    mainScreen()

def profits():
    print('Sum: ',totalsales())
    mainScreen()

def totalsales():
    global p
    sum= 0
    for i in p.values():
        sum = sum + i
    return sum


def write():
    global p
    f = open("sales_list.txt", "w")
    for item,price in p.items():
        f.write(str(item) + ' >>> '+ str(price) + '\n\n')
    f.close

mainScreen()

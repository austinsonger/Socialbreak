#!/usr/bin/python3
import os
import time
import sys
### Modules
import instainsane
import ts
import gemailhack 
import fb 

## Check if User is root or using Sudo
if not os.geteuid()==0:
    sys.exit('You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.')
time.sleep(1)
os.system('cls||clear')


def switchMenu(choice):
    if choice == '1':
        bffacebook()
    if choice == '2':
        bfgmail()
    if choice == '3':
        bfinstagram()
    if choice == '4':
        bftwitter()
    if choice == '0':
        exit()
    else:
        mainMenu()

def mainMenu():
    print("\n --------------------------------- ")
    print("\n             Socialbreak           ")
    print("\n --------------------------------- ")
    print(" What would you like to do? ")
    print("\n OPTION 1: Brute Force Facebook Account")
    print(" OPTION 2: Brute Force Gmail Account")
    print(" OPTION 3: Brute Force Instagram Account")
    print(" OPTION 4: Brute Force Twitter Account")
    print(" OPTION 0: Exit Tool")
    switchMenu(input())



#option = input("Please enter the number")
#if option == "1": # Start Bruteforce attack of Facebook Account
#elif option == "2": # Start Bruteforce attack of Gmail Account
#elif option == "3": # Start Bruteforce attack of Instagram Account
#elif option == "4": # Start Bruteforce attack of Twitter
#else:


def mainMenu():
    print("\n --------------------------------- ")
    print("\n             Socialbreak           ")
    print("\n --------------------------------- ")
    print(" What would you like to do? ")
    print("\n OPTION 1: Brute Force Facebook Account")
    print(" OPTION 2: Brute Force Gmail Account")
    print(" OPTION 3: Brute Force Instagram Account")
    print(" OPTION 4: Brute Force Twitter Account")
    print(" OPTION 0: Exit Tool")
    switchMenu(input())


def bffacebook(choice):
    print(" --------------------------------- ")
    print("        Bruteforce Facebook        ")
    print(" --------------------------------- ")
    mainMenu()


def bfgmail(choice):
    print(" --------------------------------- ")
    print("        Bruteforce Gmail           ")
    print(" --------------------------------- ")
    mainMenu()

def bfinstagram(choice):
    print(" --------------------------------- ")
    print("        Bruteforce Instagram       ")
    print(" --------------------------------- ")
    mainMenu()

def bftwitter(choice):
    print(" --------------------------------- ")
    print("        Bruteforce Twitter         ")
    print(" --------------------------------- ")
    mainMenu()
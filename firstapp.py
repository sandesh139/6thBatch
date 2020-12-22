# -*- coding: utf-8 -*-
"""
Spyder Editor
author Sandesh Timilsina
This is a temporary script file.
"""
import sys 
  
#print("Whats up python!")
# importing calendar module
import calendar
# Program make a simple calculator
# This function adds two numbers 
def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def getFloat(arr):
    for elem in arr:
       if(is_number(elem)):
           if (float(elem)< 0):
               print("Please give the positive number")
               mainMethod()
           else:
               return float(elem)
       
    print("Please give the decimal")
    mainMethod()
    


          
def mainMethod():               
    print("\n")
    print("We have two apps for you:")
    print("1.Calculator")
    print("2.Converter")
    print("3.Calendar")
    app = input("Select one app from above\n (1 for Calculator 2 for converter 3 for calender e for exit): ")
    if app == '1':
        print("Thanks for choosing calculator, \n please Select one operation from below:")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        choice = input("Enter choice(1/2/3/4): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1,"+",num2,"=", add(num1,num2))
        elif choice == '2':
            print(num1,"-",num2,"=", subtract(num1,num2))
        elif choice == '3':
            print(num1,"*",num2,"=", multiply(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"=", divide(num1,num2))
        else:
            print("Invalid input")
            mainMethod()
    elif app == '2':
        print("Thanks for choosing converter, \n please Select one operation from below:")
        print("1.Temperature")
        print("2.Distance")
        print("3.Weight")
        print("4.Data size")
        choice = input("Enter choice(1/2/3/4) or e for exit : ")
        if(choice == '2'):
            print("Thanks for choosing converter, \n please Select one operation from below:")
            print("1.KM to Miles")
            print("2.Miles to KM")
            choice = input("Enter choice(1/2): ")
           
            if choice =='1':
                string1 = input("enter distance in kilometers")
                strList = string1.split()
                print("Distance in miles : " +str(getFloat(strList) * 0.621371))
            elif choice == '2':
                string1 = input("enter distance in Miles")
                strList = string1.split()
                print("Distance in Kilometers : " +str(getFloat(strList) / 0.621371))
            else:
                print("Please give the valid input")
        elif (choice == 'e'):
            sys.exit("exited")
        else:
            print("The feature has not been implemented yet")
        
                
    elif app =='3':
        # To take month and year input from the user
        yy = int(input("Enter year: "))
        mm = int(input("Enter month: "))
    
    # display the calendar
        print("\n")
        print(calendar.month(yy, mm))
        mainMethod()
    elif app =='e':
        sys.exit("exited")
    mainMethod()
mainMethod()

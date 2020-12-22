Data Analytics Professional Training
2020- 6th Batch
Stream
Classwork
People
Grades
Data Analytics Professional Training
2020- 6th Batch
Class code
ndqifzb
Upcoming
No work due soon
View all

Announce something to your class

Post by Kiran Sharma
Kiran Sharma
Created 8:23 PM8:23 PM
Thank you and also i am stuck on 4th one as well


Post by Sandesh Timilsina
Sandesh Timilsina
Created 8:17 PM8:17 PM
Utility app.

UtilityApp_sandesh.py
Text


Post by Rocky Kharel
Rocky Kharel
Created 8:09 PM8:09 PM
If any one has done this one, please let me know how you guys did it.
02-04 Escape Sequence

"This is the oneJohnson and Emmanuel are starting a new cybersecurity company called SPYDER TECHNOLOGIES, INC.  They designed a sweet-looking logo in a text file using ASCII characters, but they need to insert it into their software.  They have promised you big money if you create a system of print statements that will print the logo (below) in a Python program for them."

Eniza thapa8:17 PM
That make sense. Thanks Shuvham.


Post by NIraj Adhikari
NIraj Adhikari
Created 1:59 AM1:59 AM
just a quick question guys: do we submit the assignment given in jira? if yes where?
i know some of us will be presenting but i am not sure if we need to submit our code!

NIraj Adhikari3:36 PM
thanks eniza :)


Post by Rocky Kharel
Rocky Kharel
Created Dec 18Dec 18
Just wanted to know if anyone is able to work on repl.it? I don't see anything when I log in now. Please let me know if anyone has the same problem.
1 class comment

Sandesh TimilsinaDec 19
I dont see it either, Rocky.

Material: "Walk-through JIRA"
Max Gupta posted a new material: Walk-through JIRA
Created Dec 18Dec 18
Material: "SCRUM in 10 mins"
Max Gupta posted a new material: SCRUM in 10 mins
Created Dec 18Dec 18
Material: "SCRUM on your own"
Max Gupta posted a new material: SCRUM on your own
Created Dec 18Dec 18
Material: "SCRUM Introduction"
Max Gupta posted a new material: SCRUM Introduction
Created Dec 18Dec 18
Material: "Python Screening Questions"
Max Gupta posted a new material: Python Screening Questions
Created Dec 18Dec 18
Material: "Basic Python Interview Questions with answers"
Max Gupta posted a new material: Basic Python Interview Questions with answers
Created Dec 18Dec 18

Post by Sandesh Timilsina
Sandesh Timilsina
Created Dec 18Dec 18
I One interesting thing I noticed.
We all know that the function cannot be called before its declaration.
However, we can call an undeclared function before its declaration inside another function. and declare it later.
This example works fine in which funcTwo is called before its declaration.:
#-----PythonCode----
x = 5

def funcOne(x):
    print(x)
    x-=1
    if(x == 0):
        return
    funcTwo(x)

def funcTwo(x):
    print(x)
    x -=1
    if(x==0):
        return
    funcOne(x)
    

funcOne(x)
1 class comment

Prakat BhattaDec 18
Thank you Sandesh


Announcement: "#Change this function to get the…"
Max Gupta
Created Dec 17Dec 17
#Change this function to get the smallest number from a list.
def max_num_in_list( list ):
    max = list[ 0 ]#10
    for a in list: #10
        if a > max: 
            max = a
    return max

Material: "Class Notes- 04132020"
Max Gupta posted a new material: Class Notes- 04132020
Created Dec 16Dec 16 (Edited Dec 17)
Material: "References- Python Built in functions"
Max Gupta posted a new material: References- Python Built in functions
Created Dec 16Dec 16

Announcement: "Create a list a which contains the…"
Max Gupta
Created Dec 16Dec 16
Create a list a which contains the first three odd positive integers and a list b which contains the first three even positive integers.
Create a new list c which combines the numbers from both lists (order is unimportant).
Create a new list d which is a sorted copy of c, leaving c unchanged.
Reverse d in-place.
Set the fourth element of c to 42.
Append 10 to the end of d.
Append 7, 8 and 9 to the end of c.
Print the first three elements of c.
Print the last element of d without using its length.
Print the length of d.

Kiran SharmaDec 17
2. # Create 2 list with odd and even with  3 numbers in each list:
a= [1,3,5]
b= [2,4,6]
print (a)
print(b)
[1, 3, 5]
[2, 4, 6]

3. # Create a new list c which combines the numbers from both lists (order is unimportant):
c = a + b
print(c)
[1, 3, 5, 2, 4, 6]

4. #Create a new list d which is a sorted copy of c, leaving c unchanged:
d = sorted(c)
print(d)
[1, 2, 3, 4, 5, 6]

5. # Reverse d in-place:
d.reverse()
print(d)
[6, 5, 4, 3, 2, 1]

6. #Set the fourth element of c to 42:
c[3]= 42
print(c)
[1, 2, 3, 42, 5, 6]

7. #Append 10 to the end of d:
d.append(10)
print(d)
[6, 5, 4, 3, 2, 1, 10]

8. #Append 7, 8 and 9 to the end of c:
c.append(7)
c.append(8)
c.append(9)
print(c)
[1, 2, 3, 42, 5, 6, 7, 8, 9]

9. # Print the first three elements of c.
print('First three element of c: ',c[0:4])
First three element of c:  [1, 2, 3, 42]

10. #Print the last element of d without using its length.
print('The last element of d : ',d[-1])
The last element of d :  10

11. #Print the length of d
print ('The length of d:' ,len(d))
The length of d: 7


Announcement: "Find the smallest and 5th highest…"
Max Gupta
Created Dec 16Dec 16
Find the smallest and 5th highest number from following list:
[327, 16, 369, 306, 235, 829, 679, 781, 335, 367, 245, 463, 882, 727, 507, 386, 847, 512, 985, 640, 694, 158, 742, 231, 984, 82, 940, 660, 510, 558, 323, 947, 333, 787, 499, 986, 741, 793, 109, 466, 118, 742, 745, 372, 437, 245, 483, 430, 92, 341, 926, 616, 40, 246, 352, 839, 492, 503, 969, 366, 191, 388, 205, 718, 677, 115, 431, 243, 351, 925, 167, 822, 542, 224, 702, 871, 355, 105, 538, 468, 832, 677, 928, 175, 114, 731, 108, 629, 31, 35, 522, 763, 490, 884, 198, 529, 479, 641, 425, 855]

Kiran SharmaDec 17
list1= [327,
        16, 369, 306, 235, 829, 679, 781, 335, 367, 245, 463, 882, 727, 507, 386, 847, 512, 985, 640, 694, 158, 742, 231, 984, 82, 940, 660, 510, 558, 323, 947, 333, 787, 499, 986, 741, 793, 109, 466, 118, 742, 745, 372, 437, 245, 483, 430, 92, 341, 926, 616, 40, 246, 352, 839, 492, 503, 969, 366, 191, 388, 205, 718, 677, 115, 431, 243, 351, 925, 167, 822, 542, 224, 702, 871, 355, 105, 538, 468, 832, 677, 928, 175, 114, 731, 108, 629, 31, 35, 522, 763, 490, 884, 198, 529, 479, 641, 425, 855]
list1.sort()
print(list1)
[16, 31, 35, 40, 82, 92, 105, 108, 109, 114, 115, 118, 158, 167, 175, 191, 198, 205, 224, 231, 235, 243, 245, 245, 246, 306, 323, 327, 333, 335, 341, 351, 352, 355, 366, 367, 369, 372, 386, 388, 425, 430, 431, 437, 463, 466, 468, 479, 483, 490, 492, 499, 503, 507, 510, 512, 522, 529, 538, 542, 558, 616, 629, 640, 641, 660, 677, 677, 679, 694, 702, 718, 727, 731, 741, 742, 742, 745, 763, 781, 787, 793, 822, 829, 832, 839, 847, 855, 871, 882, 884, 925, 926, 928, 940, 947, 969, 984, 985, 986]

lowest_num =list1[0]
print('The smallest numlber is:' ,lowest_num)
The smallest numlber is: 16

fifth_highest_num = list1[-5]
print('The fifth highest number is:' , fifth_highest_num)
The fifth highest number is: 947


Post by Kiran Sharma
Kiran Sharma
Created Dec 16Dec 16
name = input('What is your name? ')
yearborn = int(input('What year were you born? '))
if yearborn <= 1999:
  print(name , ',Your are eligible to buy Alcohol!')
else:
   print(name , ',You are not eligible to buy Alcohol!')
1 class comment

Kiran SharmaDec 16
.pop( ) > will  remove the last item from the list
.pop(1) > will remove only index 1 item from the list 
.remove(' ') > will remove specific item from the list


Announcement: "Whats the difference between remove()…"
Max Gupta
Created Dec 15Dec 15
Whats the difference between remove() and pop() function in list.

Shriju RegmiDec 16
pop() removes the last value or pop(2) removes the value at the third position and returns the same. It takes the index value as its parameter. For example:
list_1=[1,3,5,7,9]
print(list_1.pop())
print(list_1.pop(2))
will print,
9
5
whereas,
remove() function is used where we do not need the value to be returned and it takes value as it is.
list_2=[1,3,5,7,9]
list_2.remove(3)
print(list_2)
will return,
[1,5,7,9]


Announcement: "Ask your user for their name and the…"
Max Gupta
Created Dec 15Dec 15
Ask your user for their name and  the year they born and Print a message whether they can buy Alcohol or not.

Rocky KharelDec 16
name=input('Please enter your name')
birth_year=int(input('What is your year of birth?'))
age=2020-birth_year
if age>=18:
    print('You are eligible to buy alcohol')
else:
    print('You are not eligible to buy alcohol')

Data Analytics Professional Training 2020- 6th Batch
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
UtilityApp_sandesh.py
Displaying UtilityApp_sandesh.py.
# Activity 2: Create a program that calculates how many days old you are from your birthdate to today's date.

import datetime

todays_date = datetime.datetime.now()

y = todays_date.strftime("%Y")
m = todays_date.strftime("%m")
d = todays_date.strftime("%d")

dob = datetime.datetime(1996, 11, 7)

y1 = dob.strftime("%Y")
m1 = dob.strftime("%m")
d1 = dob.strftime("%d")  #putting both dates into the program


print("Today's date is: " + y,m,d +"." + " Date of birth is: " + y1,m1,d1 +".") #message checks dates are correct 

#find the differece between dates in years VVV
yeardiff = int(y) - int(y1) 

#account for the fact a year may have passed but you have not had a birthday this calendar year VVV

if int(m) < int(m1) or int(d) < int(d1):
    yeardiff = int(yeardiff) - 1
else:
    yeardiff = int(yeardiff) - 0  

print("Your are" , yeardiff , "years old.")

years_to_days = 0
years_to_days = int(yeardiff) * 365

#find the differece between dates in years in months VVV

monthsdiff = 0

if int(m) < int(m1):
    monthsdiff = 12 - int(m1) + int(m)
elif int(m) == int(m1):
    monthsdiff = 0
else:
    monthsdiff = 12 - int(m1)

# print(monthsdiff, "months old")

months_to_days = float(monthsdiff) * 30.44

#find the differece between dates in years in days VVV

daysdiff = 0 
if int(d) <= int(d1):
    daysdiff = int(d1) - int(d)
else:
    daysdiff = int(months_to_days) - int(d)


age_in_days = int(years_to_days) + int(months_to_days) + int(daysdiff)


print("You are", age_in_days, "days old.")

#Create a variable called password. Check how many letters are in the password, 
# if there are less than 8 print that the password is too short. 
# Otherwise print the password.

def passcheck(password):
    password_lengh = len(password)
    if password_lengh < 8:
        print("password is too short")
    else:
        print("password meets required length")
    
passcheck("qwerty12")

#  Create a variable called num. Check if the variable is divisible by 3 or 5. If it is output
# "This number is divisible by 3 or 5 . Otherwise log This number is not divisible by 3 or 5"

import random


num = random.randint(1,30)

if num % 3 == 0 or num % 5 == 0:
    print("This number is divisible by 3 or 5")
else:
    print("This number is not divisible by 3 or 5")

print(num)

# Create a variable called num2. 
# If num is divisible by 3 print "fizz",
#  if it is divisible by 7 print "buzz", 
# if it is divisible by both 3 and 7 print "fizz buzz". Otherwise print num.

num2 = random.randint(1,30)

if num2%3 == 0 and num2%7 == 0:
    print("fizz buzz")
elif num2 % 3 == 0:
    print("fizz")
elif num2 % 7 == 0:
    print("buzz")
else:
    print("num")

print(num2)

# Create a variable called word that takes a string. 
# Create an if statement that checks if the last letter is the same as the first. 
# If it is return true,otherwise return false.

def word_check(word):
    first = word[0]
    last = word[-1]
    if first == last:
        print("True")
    else:
        print("False")

word_check("yay")

# Create a variable called time, a variable called place_of _work.
# Create an if statement that prints where someone is at times of the day.
# For example if it is 7 I'm at home, if it is 8 I'm commuting or if it is 9 I am at work.
# It's up to you how you do this!


def spacetime(time, place_of_work):
    if time > 6:
        print("I'm at home")
    elif time < 5:
        print("I'm at work")
    elif time == 5 or 6:
        print("I'm commuting")
    if place_of_work == "Home":
        print("No commute")
    elif place_of_work == "Office":
        print("Communte to work")

spacetime(5, "Office")

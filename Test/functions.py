                                                     #Functions tasks

# Create a funtion practice

def h_w():
    print("Hello, World!")

h_w()

bootcamp_sub = 1

def bootcamp_welcome(bootcamp_sub):
    print(f"welcome to the {bootcamp_sub} bootcamp")

bootcamp_welcome("Software Engineering")

# Activity 1: Create a function that takes two parameters for: name and age, 
# and outputs a Birthday message "Happy Birthday "name" I hear you are "age" today!"

def hbd(name, age):
    print(f"Happy Birthday {name} I hear you are {int(age)} today!")

hbd("Daniel", 26)


# Create a function that takes two parameters: size and type of drink, and then outputs the drinks order.

def drink_order(size, drink):
    print(f"Your order is a {size} {drink}")

drink_order("Large", "Chai Latte")


# Edit the code below to include two more parameters and a running order count when the function is called.


order_count = 0
def take_order(topping, base, crust):
    global order_count
    print (f"Pizza with {topping} {base} {crust}")
order_count += 1

take_order("cheese", "thin", "stuffed")

# Create a cash machine program that takes a pin number and amount. 
# Output cash is being dispensed if the pin is correct and there is enough money to withdraw. 
# Finally outputs the new balance.

# Cash machine program

def cash_machine(pin_number, amount):
    balance = 150
    if pin_number == 5555 and amount <= balance:
        print("Cash is being dispensed") 
    if pin_number != 5555:
        print("Wrong pin")
    new_balance = balance - amount
    print("Remaining balance is", new_balance)
    

cash_machine(55545, 95)


    

# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruitlist =["apple", "pear","orange", "banana"]

# TODO: Use a for loop to print each fruit in the list

for x in fruitlist:
  print(x)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
countdown = [5 , 4, 3, 2, 1]
i = 0
while i < len(countdown):
  print(countdown[i])
  i = i + 1    

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for x in range(1, 11):
  square = x ** 2
  print(square)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colorlist = ("blue", "red", "purple", "orange")
# TODO: Use a for loop to select and print 3 random colors from the list
for x in range(3):
    print(random.choice(colorlist))

# TODO: Import the custom module and use its functions
import math_operations


# TODO: Use a while loop to create a simple calculator
while True:
        print(f"--------Simple Calculator--------")
        print(f"1. Addition")
        print(f"2. Subtraction")
        print(f"3. Multiplication")
        print(f"4. Divition")
        print(f"5. Exit")

        choice = input(f"Enter your choice(1-5): ")

        if choice == '5':
            print("GoodBye")
            break
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input(f"please enter value 1: "))
                num2 = float(input(f"please enter value 2: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        
        if choice == '1':
            result = math_operations.add(num1,num2 )

        elif choice == '2':            
            result = math_operations.subtract(num1,num2 )
        elif choice == '3':
            result = math_operations.multiply(num1,num2 )
        elif choice == '1':
            result = math_operations.divide(num1,num2 )
        else:
            print("invalid")
        print(result)
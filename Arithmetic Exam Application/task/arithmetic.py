import random
# Function to return sum
def plus(a,b):

    return a+b
# Function to return substract
def minus(a,b):

    return a-b
# Function to return multiply
def mul(a,b):

    return a*b
# Function to generate task 1
def taskGen1():

    # Generate first and second numbers in range 2 to 9
    a = random.randrange(2, 10)
    b = random.randrange(2, 10)
    # Get a list of operators
    oplist = ["+", "-", "*"]
    # Get a random operator
    op = random.choice(oplist)
    # Print random task
    task = str(a) + " " + str(op) + " " + str(b)
    print(task)
    # Return a list of string with first number, operator, second number
    return task
# Function to generate task 2
def taskGen2():

    # Generate a random number in range 11 to 29
    c = random.randrange(11, 30)
    print(c)
    return c
# Function to evaluate results of operations
def evaluate(s, a):

   if s[1] == "+":
        if a == plus(int(s[0]), int(s[2])):
            return "Right!"
        else:
            return "Wrong!"
   elif s[1] == "-":
        if a == minus(int(s[0]), int(s[2])):
            return "Right!"
        else:
            return "Wrong!"
   elif s[1] == "*":
        if a == mul(int(s[0]), int(s[2])):
            return "Right!"
        else:
            return "Wrong!"
# Function to evaluate results of integral square
def evaluate_sq(s,a):

    if a == mul(s, s):
        return "Right!"
    else:
        return "Wrong!"
# Check for negative integers
def is_number(n):

    try:
        float(n)
    except ValueError:
        return False
    return True
if __name__ == "__main__":

    ntask = 0
    right_count = 0
    # Create a dictionary with level and level descriptions
    level_dict = {"1": "simple operations with numbers 2-9", "2": "integral squares of 11-29"}
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    a1 = input()
    while (a1 != "1" and a1 != "2"):
        print("Incorrect format.")
        a1 = input()
    if a1 == "1":
        while (ntask < 5):
            # Generate a math task and split into 3 parts: first num, operator, sec num
            s = taskGen1().split(" ")
            # Ask for answer
            a = input()
            # While input is incorrect, keep asking input
            while is_number(a) != True :
                print("Incorrect format.")
                a = input()
                # If correct input, evaluate operation
            s_count = evaluate(s, int(a))
            # Print result of evaluation
            print(s_count)
                # If answer is right, add to right_count
            if s_count == "Right!":
                right_count += 1
            # Increase ntask by 1 after each loop
            ntask += 1
                # Print total right result
    elif a1 == "2":
        while (ntask < 5):
            s = taskGen2()
            # Ask for answer
            a = input()
            # While input is incorrect, keep asking input
            while is_number(a) != True:
                print("Incorrect format.")
                a = input()
            # If correct input, evaluate operation
            s_count = evaluate_sq(s, int(a))
            # Print result of evaluation
            print(s_count)
            # If answer is right, add to right_count
            if s_count == "Right!":
                right_count += 1
            # Increase ntask by 1 after each loop
            ntask += 1
    # Print total right result
    print(f"Your mark is {right_count}/5. Would you like to save the result? Enter yes or no.")
    # Give a list of possible answers for yes
    yeslist = ["yes","YES","Yes","y"]
    a2 = input()
    # If input is yes, ask for name
    if a2 in yeslist:
        print("What is your name?")
        # Take name as input
        name = input()
        with open("results.txt", "a") as f:
            f.write(f"{name}: {right_count}/5 in level {a1} ({level_dict[a1]})")
        f.close()
        print("The results are saved in 'results.txt'.")
    # If input is any other thing, exit the program
    else:
        exit()
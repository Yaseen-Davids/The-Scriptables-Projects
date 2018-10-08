# Import library 'time'
import time

# Define function getValues()
def getValues():
    # Gets user first number input
    firstNo = int(input("Enter first number: "))
    # Gets user math operation
    mathOperator = input("Enter Math Operator: ")
    # Gets user second number input
    secondNo = int(input("Enter Second number: "))
    # Take variables and run getAnswer() with parameters
    getAnswer(firstNo, secondNo, mathOperator)

# Define function getAnswer() with parameters from getValues()
def getAnswer(firstNo, secondNo, mathOperator):
    # Print empty line
    print("")
    # If mathOperator equals addition
    if mathOperator == "+":
        # Print Answer
        print("Answer =", firstNo + secondNo)
    # If mathOperator equals subtraction
    elif mathOperator == "-":
        # Print Answer
        print("Answer =", firstNo - secondNo)
    # If mathOperator equals division
    elif mathOperator == "/":
        # Print Answer
        print("Answer =", firstNo / secondNo)
    # If mathOperator equals multiplication
    elif mathOperator == "*":
        # Print Answer
        print("Answer =", firstNo * secondNo)
    # Else print Error Message and rerun getValues()
    else:
        print("Invalid Operator")
        getValues()

# Run getValues()
getValues()

# Terminal closes after 60 seconds
time.sleep(60)

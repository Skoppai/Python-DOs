def add(num1, num2):
    print("your answer is: {} + {} = {}".format(num1, num2, num1+num2))
def substract(num1, num2):
    print("your answer is: {} - {} = {}".format(num1, num2, num1-num2))
def multiply(num1, num2):
    print("your answer is: {} * {} = {}".format(num1, num2, num1*num2))
def divide(num1, num2):
    print("your answer is: {} / {} = {}".format(num1, num2, num1/num2))
def commands(listStr):
    if listStr == "a":
        print("add(num1, num2) adds num1 and num2 together")
    if listStr == "s":
        print("substract(num1, num2) substracts num1 and num2")
print("Module calc+ V1.0a")
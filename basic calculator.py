print("1 - Add")
print("2 - Sub")
print("3 - mux")
print("4 - div")
options = int(input("choose an operation:"))

if(options in [1,2,3,4]):
    num1 = int(input("enter a frist number:"))
    num2 = int(input("enter a  second number:"))

    if(options == 1):
        result = num1 + num2
    elif(options == 2):
        result = num1 - num2
    elif(options == 3):
        result = num1 * num2
    elif(options == 4):
        result = num1 // num2

else:
    print("Invalid operation entered")

print("The result of the operations is {}".format(result))

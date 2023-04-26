num1 = int(input("ENtr first number: "))
num2 = int(input("ENtr second number: "))

def add():
        print ("The addition is", num1+num2)

def sub():
        print ("The subtraction is", num1-num2)

def mul():
        print ("The multiplcation is", num1*num2)

def div():
        print ("The division is", num1/num2)

while True:
    print("Select an opertor: \n 1. Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Exit")
    a = int(input("Enter your choice: "))

    match a: 
            case 1:
                  add()
            case 2:
                  sub()
            case 3:
                  mul()
            case 4:
                  div()
            case _:
                  print("Enter between the range 1-4")
                
    b=input("Do you want to continue?(Y/N): ")    
    if b.upper()=="Y":
        continue
    else:
           break
                  
           
    

        
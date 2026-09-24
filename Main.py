def show_result(result):
    print(result)
    if result == 41:
        print("You reached 41! Special result detected.")


def add(x,y):
    show_result(x+y)


def subtract(x,y):
    show_result(x-y)


def multiply(x,y):
    show_result(x*y)


def division(x,y):
    show_result(x/y)

#################################################
while(True):
    print ('Howdy. What would you like to do')
    print ('Type (a)dd (s)ubtract (m)ultipyly (d)ivide (q)uit')
    choice = input(": ")
    if choice == 'q':
            break
    #print (choice)
    x = int(input('enter first number: '))
    y = int(input('enter second number: '))

    if choice == 'a':
        add(x,y)
    elif choice =='s':
        subtract(x,y)
    elif choice == 'm':
        multiply(x,y)
    elif choice == 'd':
        division(x,y)
    else:
        print("I don't understand that")

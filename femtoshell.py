from random import randint, random, randrange
while 1:
    usr_input=input("abdoshell > ")
    if usr_input == "rand":
        print(randint(0,100000000000))
        continue
    elif usr_input == "fact":
        number=int(input("Enter a number : "))
        sum=1
        for i in range(1,(number+1)):
            sum=i*sum
        print("Result is : "+sum)
        continue
    elif usr_input == "fib":
        fib_num1=1
        fib_num2=0
        fib_sequence="0"
        number=int(input("Enter a number : "))
        for i in range(number):
            fib_sequence+=", "+str(fib_num1)
            fib_num1+=fib_num2
            fib_num2=fib_num1-fib_num2
        print("The sequence is : "+fib_sequence)
        continue
    elif usr_input == "exit":
        print("Good Bye :)")
        break
    print("You said: "+usr_input)

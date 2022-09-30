import os
from random import randint
import re
while 1:
    usr_input=input("abdoshell > ")
    if usr_input.startswith("rand"):
        print(randint(0,100000000000))
        continue
    elif usr_input.startswith("fact"):
        number=int(input("Enter a number : "))
        sum=1
        for i in range(1,(number+1)):
            sum=i*sum
        print("Result is : "+str(sum))
        continue
    elif usr_input.startswith("fib"):
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
    elif usr_input.startswith("exit"):
        print("Good Bye :)")
        break

    # new assingment

    elif usr_input.startswith("echo"):
        print(usr_input[5:])
        continue
    elif usr_input.startswith("pwd"):
        print(os.getcwd())
    elif usr_input.startswith("cp"):
        args=usr_input.split()
        nfile=open(os.path.join(os.getcwd(),args[1]),"r")
        cpfile=open(os.path.join(os.getcwd(),args[2]),"w+")
        for i in nfile:
            cpfile.write(i)
        nfile.close()
        cpfile.close()
    elif usr_input.startswith("mv"):
        args=usr_input.split()
        pattern=re.findall("^/.+/(.+)",args[1])
        nfile=open(os.path.join(os.getcwd(),args[1]),"r")
        if len(pattern) == 0:
            mvfile=open(os.path.join(args[2],args[1]),"w+") 
        else:
            mvfile=open(os.path.join(args[2],pattern[0]),"w+") 
        for i in nfile:
            mvfile.write(i)
        nfile.close()
        mvfile.close()
        os.remove(os.path.join(os.getcwd(),args[1]))

    


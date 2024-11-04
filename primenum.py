inputfromuser=int(input("enter a number to find out if it is a prime number or not "))
if(inputfromuser>1):
    for i in range(2,inputfromuser):
        if(inputfromuser%i==0):
            print("it is not a prime number")
            break
        else:
            print("you have successfuly found a prime number well done")
            break
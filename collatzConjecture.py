import time
print("welcome to the collatz conjecture.")

def getStart():  #find out if user wants to use this program
    inp = input("would you like to do a collatz conjecture calculation? enter y or n:")
    choice(inp)

def getNum():  #get a number from the user
    number_input = int(input("Please enter an integer greater than 1:"))
    return number_input


def choice(ans):  #make sure input is valid - if so, run the main program
    if ans == "y" or ans == "Y":
        collatz(getNum())
    elif ans == "n" or ans == "N":
        print("then fuck off buddy, stop wasting my time.")
    else:
        print("invalid response. try again")
        getStart()

def collatz(n):
    count = 0   #debatable whether or not the number input is step 0 or step 1. In this case it is step 0.
    time_start = time.time()
    first_n = n  #saves the original number in a seperate vairable for later use
    while n != 1:
        if n % 2 == 0:  #aka if n is even
            n = n / 2
            print(n)
            count += 1            
        elif n % 2 == 1:  #aka if n is odd
            n = n*3 + 1
            print(n)
            count += 1

    time_end = time.time()
    time_diff = round(time_end - time_start, 2)  #calculates difference in the beggining and ending times
    print("")
    print("You input the number:",first_n)
    print("it took",count,"steps to return to 1.")
    print("it took about",time_diff,"seconds to run this collatz conjecture calculation.")
    print("thank you.")
    getStart()

getStart()

from os import system
### this module is used to create a list to choose from ###

def makeAchoice(lst, inpE):
    inp = -1
    while inp not in range(1, inpE+1):
        for i in lst:
            print(i)
        try:
            inp = int(input("Input: "))
        except KeyboardInterrupt:
            exit(2)
        except:
            print("Make sure you entered a number!!")
        print("\n\n")
    #system("clear")    
    return inp

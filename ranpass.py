import colorsys
import random
import string
import time

class colors:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'


print("Welcome to randpass")
time.sleep(1)

print("")

while True:
    try:
        length = int(input(colors.yellow + "Password length -> "))

        onlyletornum = input(colors.yellow + "Only letters and numbers? \"T/F\" -> ")

        if onlyletornum == "t" or onlyletornum == "T":

            lower = string.ascii_lowercase
            
            upper = string.ascii_uppercase

            all = lower + upper

            tempa = random.sample(all, length)

            passwd = "".join(tempa)

            print(colors.green + passwd)


        elif onlyletornum == "f" or onlyletornum == "F":

            lower = string.ascii_lowercase
            
            upper = string.ascii_uppercase

            num = string.digits

            sym = string.punctuation

            all = lower + upper + num + sym

            tempa = random.sample(all, length)

            passwd = "".join(tempa)

            print(colors.green + passwd)




        else:
            print( colors.red + "ERROR." + colors.yellow + "Invalid input")

    except ValueError:
        print( colors.red + "ERROR. " + colors.yellow + "Invalid input")

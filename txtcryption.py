from decryption import *

# Getting optional answer from user...
def yes_no():
    yes_no_ans = input("Do you want to Decrypt the Encrypted message [Y/N] : ").upper()
    if yes_no_ans == "Y":
        decrypt(encrypted)
    elif yes_no_ans == "N":
        print("Thank You!")
    else:
        print("WARNING!  *Invalid Answer*")
        yes_no()
yes_no()

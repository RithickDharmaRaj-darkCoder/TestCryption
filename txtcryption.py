#Encryption Section...
def encrypt(sentance = input("Type a message : ")): #Creating a User  as def encrypt()...
    encrypted = " "
    for letters in sentance:
        if letters in "A":              # Special symbols for uppercase...
            encrypted += "╚"
        elif letters in "B":
            encrypted += "Ä"
        elif letters in "C":
            encrypted += "ß"
        elif letters in "D":
            encrypted += "▼"
        elif letters in "E":
            encrypted += "░"
        elif letters in "F":
            encrypted += "≡"
        elif letters in "G":
            encrypted += "█"
        elif letters in "H":
            encrypted += "◙"
        elif letters in "I":
            encrypted += "⌂"
        elif letters in "J":
            encrypted += "ç"
        elif letters in "K":
            encrypted += "←"
        elif letters in "L":
            encrypted += "╪"
        elif letters in "M":
            encrypted += "≤"
        elif letters in "N":
            encrypted += "⌡"
        elif letters in "O":
            encrypted += "√"
        elif letters in "P":
            encrypted += "±"
        elif letters in "Q":
            encrypted += "≥"
        elif letters in "R":
            encrypted += "╙"
        elif letters in "S":
            encrypted += "╫"
        elif letters in "T":
            encrypted += "Γ"
        elif letters in "U":
            encrypted += "Σ"
        elif letters in "V":
            encrypted += "σ"
        elif letters in "W":
            encrypted += "τ"
        elif letters in "X":
            encrypted += "Φ"
        elif letters in "Y":
            encrypted += "δ"
        elif letters in "Z":
            encrypted += "∞"
        elif letters in "a":                # Special symbols for lowercase...
            encrypted += "☺"
        elif letters in "b":
            encrypted += "☻"
        elif letters in "c":
            encrypted += "♥"
        elif letters in "d":
            encrypted += "♦"
        elif letters in "e":
            encrypted += "♣"
        elif letters in "f":
            encrypted += "♠"
        elif letters in "g":
            encrypted += "◘"
        elif letters in "h":
            encrypted += "○"
        elif letters in "i":
            encrypted += "♂"
        elif letters in "j":
            encrypted += "♀"
        elif letters in "k":
            encrypted += "♪"
        elif letters in "l":
            encrypted += "♫"
        elif letters in "m":
            encrypted += "☼"
        elif letters in "n":
            encrypted += "►"
        elif letters in "o":
            encrypted += "↕"
        elif letters in "p":
            encrypted += "‼"
        elif letters in "q":
            encrypted += "§"
        elif letters in "r":
            encrypted += "▬"
        elif letters in "s":
            encrypted += "↨"
        elif letters in "t":
            encrypted += "↑"
        elif letters in "u":
            encrypted += "↓"
        elif letters in "v":
            encrypted += "→"
        elif letters in "w":
            encrypted += "∟"
        elif letters in "x":
            encrypted += "↔"
        elif letters in "y":
            encrypted += "╥"
        elif letters in "z":
            encrypted += "Ω"
        elif letters in " ":                # Special symbol for empty space...
            encrypted += "φ"
        elif letters in "1":                # Special symbols for Numbers...
            encrypted += "ε"
        elif letters in "2":
            encrypted += "∩"
        elif letters in "3":
            encrypted += "₧"
        elif letters in "4":
            encrypted += "¥"
        elif letters in "5":
            encrypted += "á"
        elif letters in "6":
            encrypted += "ñ"
        elif letters in "7":
            encrypted += "ü"
        elif letters in "8":
            encrypted += "├"
        elif letters in "9":
            encrypted += "½"
        elif letters in "0":
            encrypted += "╦"
        elif letters in ".":                # Special symbol for Dot'.' ...
            encrypted += "│"
        else:
            encrypted += letters
    return encrypted

encrypted = encrypt()               # Calling the UserDefined Function...
print(f"Encrypted Message :"+encrypted)

#Decryption Section...
def decrypt(encrypted): #Creating a User  as def decrypt()...
    decrypted = " "
    for letter in encrypted:
        if letter in "╚":              # Decryption for uppercase...
            decrypted += "A"
        elif letter in "Ä":
            decrypted += "B"
        elif letter in "ß":
            decrypted += "C"
        elif letter in "▼":
            decrypted += "D"
        elif letter in "░":
            decrypted += "E"
        elif letter in "≡":
            decrypted += "F"
        elif letter in "█":
            decrypted += "G"
        elif letter in "◙":
            decrypted += "H"
        elif letter in "⌂":
            decrypted += "I"
        elif letter in "ç":
            decrypted += "J"
        elif letter in "←":
            decrypted += "K"
        elif letter in "╪":
            decrypted += "L"
        elif letter in "≤":
            decrypted += "M"
        elif letter in "⌡":
            decrypted += "N"
        elif letter in "√":
            decrypted += "O"
        elif letter in "±":
            decrypted += "P"
        elif letter in "≥":
            decrypted += "Q"
        elif letter in "╙":
            decrypted += "R"
        elif letter in "╫":
            decrypted += "S"
        elif letter in "Γ":
            decrypted += "T"
        elif letter in "Σ":
            decrypted += "U"
        elif letter in "σ":
            decrypted += "V"
        elif letter in "τ":
            decrypted += ""
        elif letter in "Φ":
            decrypted += "X"
        elif letter in "δ":
            decrypted += "Y"
        elif letter in "∞":
            decrypted += "Z"
        elif letter in "☺":                # Decryption for lowercase...
            decrypted += "a"
        elif letter in "☻":
            decrypted += "b"
        elif letter in "♥":
            decrypted += "c"
        elif letter in "♦":
            decrypted += "d"
        elif letter in "♣":
            decrypted += "e"
        elif letter in "♠":
            decrypted += "f"
        elif letter in "◘":
            decrypted += "g"
        elif letter in "○":
            decrypted += "h"
        elif letter in "♂":
            decrypted += "i"
        elif letter in "♀":
            decrypted += "j"
        elif letter in "♪":
            decrypted += "k"
        elif letter in "♫":
            decrypted += "l"
        elif letter in "☼":
            decrypted += "m"
        elif letter in "►":
            decrypted += "n"
        elif letter in "↕":
            decrypted += "o"
        elif letter in "‼":
            decrypted += "p"
        elif letter in "§":
            decrypted += "q"
        elif letter in "▬":
            decrypted += "r"
        elif letter in "↨":
            decrypted += "s"
        elif letter in "↑":
            decrypted += "t"
        elif letter in "↓":
            decrypted += "u"
        elif letter in "→":
            decrypted += "v"
        elif letter in "∟":
            decrypted += "w"
        elif letter in "↔":
            decrypted += "x"
        elif letter in "╥":
            decrypted += "y"
        elif letter in "Ω":
            decrypted += "z"
        elif letter in "φ":                # Decryption for empty space...
            decrypted += " "
        elif letter in "ε":                # Decryptions for Numbers...
            decrypted += "1"
        elif letter in "∩":
            decrypted += "2"
        elif letter in "₧":
            decrypted += "3"
        elif letter in "¥":
            decrypted += "4"
        elif letter in "á":
            decrypted += "5"
        elif letter in "ñ":
            decrypted += "6"
        elif letter in "ü":
            decrypted += "7"
        elif letter in "├":
            decrypted += "8"
        elif letter in "½":
            decrypted += "9"
        elif letter in "╦":
            decrypted += "0"
        elif letter in "│":                # Decryption for Dot'.' ...
            decrypted += "."
        else:
            decrypted += letter
    print("Decrypted Message :"+decrypted)

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

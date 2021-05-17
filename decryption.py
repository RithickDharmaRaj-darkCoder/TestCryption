from encryption import *

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

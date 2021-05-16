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
    print( f"Encrypted Message :{encrypted}")

encrypt()               # Calling the UserDefined Function...

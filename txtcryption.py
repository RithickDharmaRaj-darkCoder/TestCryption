def encrypt(sentance = input("Type a message : ")):
    encrypted = " "
    for letters in sentance:
        if letters in "Aa":
            encrypted += "1"
        elif letters in "Bb":
            encrypted += "2"
        elif letters in "Cc":
            encrypted += "3"
        elif letters in "Dd":
            encrypted += "4"
        elif letters in "Ee":
            encrypted += '"'
        elif letters in "Ff":
            encrypted += "6"
        elif letters in "Gg":
            encrypted += "7"
        elif letters in "Hh":
            encrypted += "8"
        elif letters in "Ii":
            encrypted += "9"
        elif letters in "Jj":
            encrypted += "0"
        elif letters in "Kk":
            encrypted += "!"
        elif letters in "Ll":
            encrypted += "@"
        elif letters in "Mm":
            encrypted += "#"
        elif letters in "Nn":
            encrypted += "$"
        elif letters in "Oo":
            encrypted += "%"
        elif letters in "Pp":
            encrypted += "^"
        elif letters in "Qq":
            encrypted += "&"
        elif letters in "Rr":
            encrypted += "*"
        elif letters in "Ss":
            encrypted += "("
        elif letters in "Tt":
            encrypted += ")"
        elif letters in "Uu":
            encrypted += "_"
        elif letters in "Vv":
            encrypted += "'"
        elif letters in "Ww":
            encrypted += "?"
        elif letters in "Xx":
            encrypted += ">"
        elif letters in "Yy":
            encrypted += "<"
        elif letters in "Zz":
            encrypted += "/"
        elif letters in " ":
            encrypted += "5"
        else:
            encrypted += letters
    print( f"Encrypted Message :{encrypted}")

encrypt()

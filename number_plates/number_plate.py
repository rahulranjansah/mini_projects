def plate_regulation(name):
    if 6 >= len(name) >= 2 and name[0:2].isalpha() and name.isalnum():
        for char in name:
            #checks if the first string is digit and checks rest all string if digit then true.
            if char.isdigit():
                index = name.index(char)
                if name[index:].isdigit() and char != "0":
                    return True
                else:
                    return False
        return True

if __name__ == "__main__":
    plates = input("vanity plate: ")
    if plate_regulation(plates):
        print ("Valid")
    else:
        print ("Invalid")

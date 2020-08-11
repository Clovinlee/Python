import random, string

def randomPassword():
    while True:
        length = random.randint(8, 16)
        upp = 0
        low = 0
        dig = 0
        pun = 0
        password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k = length))
        for x in password:
            for i in string.ascii_uppercase :
                if i in x :
                    upp = 1
            for i in string.ascii_lowercase:
                if i in x :
                    low = 1
            for i in string.digits:
                if i in x :
                    dig = 1
            for i in string.punctuation:
                if i in x :
                    pun = 1
        if upp + low + dig + pun == 4 :
            print('Password successfully generated!')
            print("Your password successfully changed to", password)
            break
    return password
def main():
    while True :
        e_len = 0
        e_capital = 0
        e_lower = 0
        e_number = 0
        e_special = 0
        e_space = 1
        error = []
        password = input("\nPlease enter your password ")
        if len(password ) >= 8 and len(password) < 17:
            e_len = 1
        if ' ' in password:
            e_space = 0
        for x in password :
            if x.islower() :
                e_lower = 1
            if x.isupper() :
                e_capital =1
            if x.isdigit() :
                e_number = 1
            for x in password:
                for i in string.punctuation :
                    if i in x :
                        e_special = 1
        if e_len == 0 :
            error.append("Error : Password need to be at least 8 to 16 character long!")
        if e_capital == 0:
            error.append("Error : At least 1 capital letter is required!")
        if e_lower == 0:
            error.append("Error : At least 1 lower letter is required!")
        if e_number == 0:
            error.append("Error : At least 1 number is required!")
        if e_special == 0:
            error.append("Error : At least 1 special character is required!")
        if e_space == 0:
            error.append("Error : Please dont use any space in the password!")
        for x in error :
            print (x)
        if error == []:
            break
    print("\nPassword acccepted!")
    print("Your password successfully changed to", password)
start = input("Welcome! type 1 to create a password , or 2 to generate a random password")
while True :
    if start == '1' :
        main()
        break
    elif start =='2' :
        randomPassword()
        break
    else : print("Invalid input, please try again\n")
    start = input("Type 1 to create a password, or 2 to generate a random password")

# Task 1
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
def name_length_checker(f_name, l_name):
    name_length1 = len(f_name)
    if name_length1 < 2:
        print("Your name isn't long enough")
    else:
        print(f"Your first name is {name_length1} characters long...")
    name_length2 = len(l_name)
    if name_length1 < 2:
        print("Your name isn't long enough")
    else:
        print(f"Your last name is {name_length2} characters long...")

name_length_checker(f_name, l_name)

# Task 2
password = input("Enter your password: ")
lowercase = 0
uppercase = 0
special = 0
digit = 0

def password_checker(password):

        global lowercase
        global uppercase
        global digit
        global special

        for i in password:

            if (i.islower()):
                lowercase += 1

            if (i.isupper()):
                uppercase += 1

            if (i.isdigit()):
                digit += 1

            if(i=='@'or i=='$' or i=='_'):
                special+=1
        if len(password) < 8:
            print("Password needs to be at least 8 characters long!")
        elif lowercase < 1:
            print("You need a lowercase letter")
        elif uppercase < 1:
            print("You need an uppercase letter")
        elif special < 1:
            print("You need a special character")
        elif digit < 1:
            print("You need a digit")
        else:
            valid_password = True
            print("Valid Password")

password_checker(password)



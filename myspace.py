#Create Myspace (ALWAYS ASK QUESTIONS DURING TECHNICAL)
#user profile to sign up for a account
#first and last name, email address, phone number, password, date of birth, user namne) 
#complex password (alpha numeric only, no special characters)
#can sign in with either email or user name
#after login, print out Welcome NAME to Myspace! print all the info.

#STRATEGY FIRST BEFORE CODING 
## Display Introduction when accessing myspace.com
## Ask if you are signing in or signing up
## If user wants to sign up, then ask questions to obtain info
## if user wants to sign in, then ask for email address/user name and password. 
## If it is correct, Display "Welcome to your user profile
## If email address/password is wrong, output invalid credentials 

#REQUIREMENTS** 
#Enter colon with all questions (DONE)
#line 36 need to accept user name and email. (DONE)
#when you put wrong credentials, please ask again to sign in. (loops)
#username alphanumeric 
#email has @ and not .com
#password is not longer thatn 10 characters, if it is 10 characters, ask again
#after login, print out Welcome NAME to Myspace! print all the info. (DONE)
#next week deadline. 


print("Welcome to Myspace! Please sign in or sign up below")
signIn_choice = input("Would you like to sign in or sign up? ")

if signIn_choice == "sign up":
    print("Please fill out this form to create your profile")
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    email_address = input("Please enter your email: ")
    user_name = str(input("Please enter your user name: "))
    phone_number = input("Please enter your phone number: ")
    password = input("Please enter a password: ")
    date_ofBirth = input("Please enter your date of birth MM/DD/YYY: ")
    print("Your account has been created! Please enter your credentials: ")
    signIn_user = input("Please enter your username/email: ") 
    signIn_password = input("Please enter your password: ")

if signIn_user == email_address or signIn_user == user_name and signIn_password == password:
  print("Welcome" + " " + first_name + " " + last_name + " " + "to your user profile! ")
  print("Your email is: " + email_address)
  print("Your user_name is: " + user_name)
  print("Your phone number is: " + phone_number)
  print("Your date of birth is: " + date_ofBirth)
else:
  print("You credentials are invalid, please sign in again. ")

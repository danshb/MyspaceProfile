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

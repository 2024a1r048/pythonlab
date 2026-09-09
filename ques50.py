#WAP that asks the user to enter a username attempts.If the correct credintials are entered,display"LOgin Successful"and stop the loop.If all the attempts are used ,display "Acoounted Locked".
  

correct_username = "samaad"
correct_password = "abc@123"
for i in range(0,3):
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    if username == correct_username and  password == correct_password:
        print("Login successfull:")
        break
    else:
        print("Account Locked:")
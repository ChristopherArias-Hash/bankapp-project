def loginSystem():
    # Read the username and password from the file
    with open("data.txt", "r") as file: 
        currentUsername = file.readline().strip()
        currentPassword = file.readline().strip()
        
    # Check if username or password is missing in the file
    if not currentUsername or not currentPassword:
        raise Exception("Username or password not found in data.txt")
    
    while True:
        # Prompt the user for username and password
        usernamePrompt = input("Please sign in using your Username\n") 
        passwordPrompt = input("Please sign in using your Password\n") 
        # Check if the input username and password match the stored username and password
        if passwordPrompt == currentPassword and usernamePrompt == currentUsername:
            break
        else:
            # If the input username and password do not match, prompt the user to try again
            print("Your Username or Password is incorrect!\nPlease try again!")

    return currentUsername, currentPassword

def continueResponse(currentUsername, currentPassword):
    # Read current user data from the file
    with open("data.txt", "r") as file: 
      file.readline().strip()  # Skip the username
      file.readline().strip()  # Skip the password
      currentBalance = file.readline()

    # Check if the balance is positive and continue the loop
    while int(currentBalance) >= 0:
        currentBalance = int(currentBalance)
        # Add two empty lines before the input prompt
        print("\n" * 2)
        # Display current balance and prompt for action
        balanceSheet = input("Your current balance is ${}\n"
                             "Would you like to Deposit or Withdraw money?\n"
                             "Type 'D' for Deposit, 'W' for Withdrawal, or 'X' to Exit:\n".format(currentBalance))
        # Add two empty lines after the input prompt
        print("\n" * 2)

        # Process the selected action
        if balanceSheet == "D":
            depositInfo = input("How much would you like to deposit: ")
            currentBalance += int(depositInfo)
            # Update the balance in the file
            with open("data.txt", "w") as file:
                file.write(currentUsername + "\n")
                file.write(currentPassword + "\n")
                file.write(str(currentBalance) + "\n")
        elif balanceSheet == "W":
            withdrawInfo = input("How much would you like to withdraw: ")
            if int(withdrawInfo) > int(currentBalance):
                print("ERROR U MUST HAVE CERTAIN AMOUNT")
            else:
                currentBalance -= int(withdrawInfo)
                print("Remaining balance:", currentBalance)
                # Update the balance in the file
                with open("data.txt", "w") as file:
                    file.write(currentUsername + "\n")
                    file.write(currentPassword + "\n")
                    file.write(str(currentBalance) + "\n")
        elif balanceSheet == "X":
            print("Bye have a good one!")
            break

try:
    # Try to continue with existing user data
    currentUsername, currentPassword = loginSystem()
    continueResponse(currentUsername, currentPassword)

except Exception as e:
    print(e)
    # Prompt for new user data
    usernameResponse = input("Please type in the Username you will like the create: ")
    passwordResponse = input("Please type in the Password you will like the create: ")
    firstResponse = input("How much money do you have in your checking account? \n") 
    with open("data.txt", "w") as file:
        file.write(usernameResponse + "\n")
        file.write(passwordResponse + "\n")
        file.write(firstResponse + "\n")

    # Continue with the new user data
    continueResponse(usernameResponse, passwordResponse)

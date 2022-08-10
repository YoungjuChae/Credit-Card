# Author: Youngju Chae
# Code that checks validation and type of credit card

# Code to check validation
def checkCard():
  card_num = input("Enter credit card number: ")
  # Remove the last digit
  payload = card_num[:-1]
  # Create neccessary variables
  n = len(payload)
  sum = 0
  # Starting from the rightmost digit, double the value of every second digit
  for x in payload:
    if n % 2 != 0:
      digits = int(x) * 2
      # Check if digit greater than 9
      if digits > 9:
        digits = digits - 9
      n += 1
    else:
      digits = int(x)
      n += 1
    # Add all the digits
    sum += digits
  print(sum)
  # Determine check digit
  check_digit = 10 - (sum % 10)
  print(check_digit)
  # Determine if number is valid
  return (payload + str(check_digit) == card_num)

# Code to check type (American Express, Visa, Discover Card, and Mastercard)
def checkType():
  # Get card number
  card_num = input("Enter credit card number: ")
  # Create necessary variable
  length = len(card_num)
  # Check if card is Express
  if (length == 15) and ((card_num[0:2] == str(34)) or (card_num[0:2] == str(37))):
    print("The credit card is an American Express.")
  # Check if card is Visa
  if card_num[0] == str(4) and ((length == 13) or (length == 16)):
    print("The credit card is a Visa.")
  # Check if card is Discover 
  elif (length < 20) and (length > 15):
    if ((card_num.startswith("65")) or (card_num.startswith("6011")) or (int(card_num[0:3]) < 650 and int(card_num[0:3]) > 643) or (int(card_num[0:6]) < 622926 and int(card_num[0:6]) > 622125)):
      print("The credit card is a Discover Card.")
  # Check if card is Mastercard
  elif (length == 16) and ((int(card_num[0:2]) < 56 and int(card_num[0:2]) > 50) or (int(card_num[0:4]) < 2721) and (int(card_num[0:4]) > 2220)):
    print("The credit card is a MasterCard.")

# Determine if user wants to continue
def playAgain():
  while True:
    choice = input("Would you like to check (v)alidation, (t)ype, or quit? ")
    # Validation
    if choice == "v":
      print(checkCard())
    # Type
    elif choice == "t":
      checkType()
    # Quit
    elif choice == "q":
      break
  
playAgain()

# Author: Youngju Chae
# Code that checks validation and type of credit card

# Code to check validation
def checkCard():
  # Ask for credit card number
  card_num = input("Enter credit card number: ")
  # Remove the last digit
  payload = card_num[:-1]
  # Create neccessary variables
  n = 1
  sum = 0
  # Double the value of every second digit
  for x in payload:
    if n % 2 == 0:
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
  # Determine check digit
  check_digit = 10 - (sum % 10)
  # Determine if number is valid
  return (payload + str(check_digit) == card_num)
  
  

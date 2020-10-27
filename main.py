# Guess the number!

import random

# Setting the variables
guess = input('Give me a number between 1 and 20 :)')
number = random.randint(1,20)

# If the guess isn't the generated number
while int(guess) != int(number): 
  if (int(guess) > int(number)):
   print ('Too high, try again!')
  elif (int(guess) < int(number)):
   print ('Too low, guess something higher!')
  guess = input('Give me a number between 1 and 20 :)')

# If the guess is equal to the number (outside the loop)  
print ('Yay, you got it! Well done! :D')
import string
import random

def generate_key(needed_length):
  if isinstance(needed_length, int):
    chars = string.ascii_letters
    key = ''.join(random.choice(chars) for i in range(needed_length))

    return key

needed_length = None

try:
  needed_length = int(input("Please enter a valid length: "))

  if isinstance(needed_length, int):
    key = generate_key(needed_length)
    print(key)
except ValueError:
  print("Invalid input, Please enter a valid number.")

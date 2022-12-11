import string
import random

def generate_key(length):
  chars = string.ascii_letters + string.digits + string.punctuation
  key = ''.join(random.choice(chars) for i in range(length))

  return key

key = generate_key(100)

print(key)

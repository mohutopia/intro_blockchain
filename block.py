# Every Block in the blockchain has a timestamp associated with it. In order to dynamically generate a timestamp, we must import a Python module that returns the current date and time
from datetime import datetime # Import the datetime module from the datetime library
from hashlib import sha256 # Import sha256 from the hashlib Python library.

print(datetime.now()) # .now() method returns the current date and time

class Block(object):
 # Now let's work on creating our Block. We will be passing transactions and previous_hash to the default constructor each time a Block is created.
 def __init__(self, transactions, previous_hash, nonce = 0):
  self.transactions = transactions
  self.previous_hash = previous_hash
  self.nonce = nonce
  # Inside the __init__() method, create a timestamp instance variable that stores the current date and time.
  self.timestamp = datetime.now()
  self.hash = self.generate_hash()
 

 def print_block(self):
  # prints block contents
  print("timestamp:", self.timestamp)
  print("transactions:", self.transactions)
  print("current hash:", self.generate_hash())
  print("previous hash:", self.previous_hash) 
 
 
 def generate_hash(self):
  # Create the variable block_contents, which combines the Block timestamp, transactions, nonce, and previous hash.
  block_contents = str(self.timestamp) + str(self.transactions) + str(self.nonce) + str(self.previous_hash)
  # Create a variable block_hash. Create a new hash with sha256() and block_contents and save the value to block_hash. Remember to use the .encode() method to encode the string.
  block_hash = sha256(block_contents.encode())
  # Return the text hash value by calling the hexdigest() method on block_hash.
  return block_hash.hexdigest()
'''
The blockchain is a new way of storing and moving data securely. The data mostly consists of transactions which include messages exchanged between two parties.

These transactions are all stored inside the mempool, a pool of transactions that miners reference when selecting the set of transactions they want to verify.
'''

from blockchain import Blockchain

# transaction1 = {
#   'amount': '30',
#   'sender': 'Alice',
#   'receiver': 'Bob'}
# transaction2 = { 
#   'amount': '200',
#   'sender': 'Bob',
#   'receiver': 'Alice'}
# transaction3 = { 
#   'amount': '300',
#   'sender': 'Alice',
#   'receiver': 'Timothy' }
# transaction4 = { 
#   'amount': '300',
#   'sender': 'Rodrigo',
#   'receiver': 'Thomas' }
# transaction5 = { 
#   'amount': '200',
#   'sender': 'Timothy',
#   'receiver': 'Thomas' }
# transaction6 = { 
#   'amount': '400',
#   'sender': 'Tiffany',
#   'receiver': 'Xavier' }

# mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]


##################  HACKING THE CHAIN  ##################


new_transactions = [
  {'amount': '30', 'sender':'alice', 'receiver':'bob'},
  {'amount': '55', 'sender':'bob', 'receiver':'alice'}
  ]

# Instantiate a new Blockchain object called my_blockchain.
my_blockchain = Blockchain()

# Add a new block to my_blockchain and pass in new_transactions as the argument.
my_blockchain.add_block(new_transactions)

# Print out the contents of my_blockchain to see the new block!
my_blockchain.print_blocks()

# Select the transactions found in my_blockchain's chain attribute. Modify the transactions of the first block setting its value to the string "fake_transactions".
my_blockchain.chain[1].transactions = "fake_transactions"

# Now let's check if the blockchain is still valid by calling the correct method over my_blockchain!
my_blockchain.validate_chain() # ==> prints: "The current hash of the block does not equal the generated hash of the block."


##################  NONCE AND PROOF-OF-WORK ##################


from hashlib import sha256 # Import sha256 from the hashlib Python library.

# new_transactions is defined in the section above

# Create a variable called difficulty and assign it a value of 2. This sets the number of leading zeros that the hash we find must have.
difficulty = 2
# Create another variable called nonce and assign it to a value of 0. This will be our default starting value.
nonce = 0

# Using the .str() method, cast nonce and new_transactions into strings. Pass the two strings into the sha256 function.
# Store the resulting hash value into a variable called proof and print it out!
# Note: Use the .hexdigest() method over the resulting sha256 function to properly store the hash value.
proof = sha256(str(nonce).encode() + str(new_transactions).encode()).hexdigest()

# ...not finished
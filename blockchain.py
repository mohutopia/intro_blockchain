# imports the Block class from block.py
from block import Block

class Blockchain(object):
 
 def __init__(self):
  # Fill in the __init__() method inside the Blockchain class by initializing instance variables chain and all_transactions as empty Python lists.
  self.chain = []
  self.all_transactions = []
  self.genesis_block() # to automatically create a Genesis Block when a new blockchain object is created

 
 def genesis_block(self):
  # Complete the method genesis_block by instantiating a new Block object with an empty transactions list and a hash of 0. Append the resulting block to the chain.
  transactions = {}
  genesis_block = Block(transactions, "0")
  self.chain.append(genesis_block)
  return self.chain

 
 # prints contents of blockchain
 def print_blocks(self):
  for i in range(len(self.chain)):
   current_block = self.chain[i]
   print("Block {} {}".format(i, current_block))
   current_block.print_contents()    
 
 
 def add_block(self, transactions):
  # Create a variable named new_block that takes in a transaction and the previous_block' hash. Append new_block to the end of the chain.
  previous_block_hash = self.chain[len(self.chain)-1].hash
  new_block = Block(transactions, previous_block_hash)
  # In the .add_block() method, calculate the proof_of_work for the new_block. Assign the calculated proof_of_work to a variable named proof before appending the new_block to the blockchain.
  proof = self.proof_of_work(new_block)
  self.chain.append(new_block)
  # Return, in order, the calculated proof and the new_block itself.
  return proof, new_block
 
 
 def validate_chain(self):
  # In the .validate_chain() method, create a for loop with the loop variable i and traverse through the entire length of self.chain. Be sure to start at index 1 instead of index 0.
  # Inside the for loop, create a variable current and assign it to the current block being indexed with i. Create another variable previous and assign it to the previous block using index i-1.
  for i in range(1, len(self.chain)):
   current = self.chain[i]
   previous = self.chain[i-1]
   # Verify that the hash of the current block is NOT equal to the value the current block generates via the generate_hash() method. If this condition is true, then the blockchain is not valid, therefore we should return False.
   if(current.hash != current.generate_hash()):
    print("The current hash of the block does not equal the generated hash of the block.")
    return False
   # Verify that the hash of the previous hash of the current block is NOT equal to the value generated over the previous block using the generate_hash() method. If this condition is true, then the blockchain is not valid, therefore we should return False.
   if(current.previous_hash != previous.generate_hash()):
    print("The previous block's hash does not equal the previous hash value stored in the current block.")
    return False
  # If the above conditions are not satisfied, then the blockchain is valid! Return True outside the for loop.
  return True
 
 
 def proof_of_work(self,block, difficulty=2):
  # Inside the .proof-of-work() method, create a local variable proof and assign it the block's hash.
  proof = block.generate_hash()
  # Finish the rest of the method by creating a loop that increments the nonce value until the hash with the required difficulty has been generated.
  while proof[:difficulty] != '0'*difficulty:
   block.nonce += 1
   proof = block.generate_hash()
  # After finding the correct hash, set the value of the block.nonce back to 0 and return the correct hash outside of the loop.
  block.nonce = 0
  return proof

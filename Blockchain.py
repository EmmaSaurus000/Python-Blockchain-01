# ------------------------------------------------------------
# Filename      : Blockchain.py
# Location      : ./Blockchain
# Project       : repos
# Author        : Emma Saurus <20078202@tafe.wa.edu.au>
# Created       : 11/08/2021
# Version       : 0.1
# Description   : A simplified model of a Blockchain -- tutorial
#                 <https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531>
#
# ------------------------------------------------------------


# Each block is a row of data
# 1 Create Blockchain class
# 2 Fumction to build new blocks
# 3 Fumction to create new transactions
#   and get last block
# 4. Write a function to hash the blocks
#

import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="I am moving the world.", proof=100)

    # block-builder
    def new_block(self, proof, previous_hash=None):
        # define the object properties
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):

        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        # Super-simplified object properties
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }

        # JSON object apparrently, like a form waiting for data
        # "Data stays in limbo until a new block is mined
        # and added to our blockchain."
        self.pending_transactions.append(transaction)
        # ID ready for the new transaction
        return self.last_block['index'] + 1

    def hash(self, block):
        # (in JSON, out text string)
        string_object = json.dumps(block, sort_keys=True)
        print(f"string_object = {string_object}")
        # "turns string into Unicode"
        block_string = string_object.encode()
        print(f"block_string = {block_string}")

        # Block text Unicode string encrypted with
        # SHA-256 hash function from hashlib
        # (in text -> out 64-char-long encrypted string)
        raw_hash = hashlib.sha256(block_string)
        print(f"raw_hash = {raw_hash}")
        # create hexidecimal string from raw_hash"
        hex_hash = raw_hash.hexdigest()
        print(f"hex_hash = {hex_hash}")

        return hex_hash

"""
Blockchains are considered 'tamper-proof' 
because blocks contain a copy of the previous block's hash.
[like DNA?]
Since your new hash is derived from the previous block, 
you can't change any part of it 
without changing every single hash in front of it.
"""
# execution
blockchain = Blockchain()
b1 = blockchain.new_transaction("Tom", "Jerry", "1 BTC")
b2 = blockchain.new_transaction("Brutus", "Jerry", "3 BTC")
b3 = blockchain.new_transaction("Jerry", "Brutus", "0.5 BTC")
b4 = blockchain.new_transaction("Tom", "Brutus", "2.5 BTC")
blockchain.new_block(12345)

b5 = blockchain.new_transaction("Brutus", "Tom", "0.5 BTC")
b6 = blockchain.new_transaction("Jerry", "Brutus", "2 BTC")
b7 = blockchain.new_transaction("Tom", "Jerry", "1.5 BTC")
blockchain.new_block(67890)







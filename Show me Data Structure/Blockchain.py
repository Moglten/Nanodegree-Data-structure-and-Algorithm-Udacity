import hashlib
from datetime import datetime
class BlockChain:
    def __init__(self):
        self.head = None


    def create_block(self, data):

        if self.head is None:

            self.head = Block( datetime.utcnow(), data, 0 )

        else:

            new_Block = Block( datetime.utcnow(), data, self.head.get_hash())
            new_Block.pointer = self.head
            self.head = new_Block

    def print_block_data(self):
        if self.head is None:
            print(None)
        else:
            curr = self.head
            while curr:
                print(curr.get_data())
                curr = curr.get_prev_block()

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.pointer = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.data).encode( 'utf-8' )
        sha.update( hash_str )
        return sha.hexdigest()

    def get_utc_time(self):
        return self.timestamp

    def get_hash(self):
        return self.hash

    def get_prev_block(self):
        return self.pointer

    def get_data(self):
        return self.data


MyBlockChain = BlockChain()
MyBlockChain.create_block("first block ")
MyBlockChain.create_block("second block ")
MyBlockChain.create_block("third block ")
MyBlockChain.print_block_data()  #return data of Blocks

MyBlockChain1= BlockChain()
MyBlockChain1.print_block_data()  #return None is empty block chain

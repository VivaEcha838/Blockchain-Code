import datetime
import hashlib
class Block():
    def __init__(self, previous_block_hash, data, timestamp):
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.timestamp = timestamp
        self.hash = self.hashFunction()

        @staticmethod
        def genesisBlock():
            return Block(0, 0, datetime.datetime.now())

        def hashFunction(self):
            block_header = (str(self.previous_block_hash)+str(self.data)+str(self.timestamp))
            inner_hash = hashlib.sha256(block_header.encode()).hexdigest().encode()
            outer_hash = hashlib.sha256(inner_hash).hexdigest()
            return outer_hash
    
    class BlockChain():
        number_of_blocks = int(input("Enter number of blocks in your blockchain: "))
        block_chain = [Block.genesisBlock()]
        print("Block 1 (genesis block) has been created" )
        print("Hash of block:- %s" % block_chain[0].hash)
        print("Hash of previous block:- 0")

        for i in range(1, number_of_blocks):
            block_chain.append(Block(block_chain[i-1].hash,
                "Block number %d" % (i+1),
                datetime.datetime.now()))
            print("Block %d created" % (i+1))
            print("Hash of block:- %s" % block_chain[-1].hash)
            print("Hash of previous block:- %s" % block_chain[i-1].hash)



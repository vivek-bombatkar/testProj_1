import datetime as date
import hashlib as hash

class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = hash.sha256(data.encode('ascii')).hexdigest()

    def __repr__(self):
        return "{0} : {1}, {2}, {3} ".format(self.index, str(self.timestamp), self.data,self.prev_hash)

def getGenesisBlock():
    return Block(0, date.datetime.now(), "the genesis block", "0")

def getNextBlock(prev_block, data):
    index = prev_block.index + 1
    timestamp = date.datetime.now()
    data = data
    hash = prev_block.hash
    return Block(index, timestamp, data, hash)

def addToBlockchain(prev_block,inputData,value_data_science_module,result_data_set):
    new_block = getNextBlock(prev_block, hash.sha256(inputData.encode('ascii')).hexdigest(), 0)
    bc.append(new_block)
    return ""
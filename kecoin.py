import hashlib
import json
import time


class Block:
    def __init__(self, index, timestamp, data, previousHash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.calculateHash()

    def calculateHash(self):
        m = hashlib.sha256()
        m.update(str(self.index).encode('utf-8'))
        m.update(self.previousHash.encode('utf-8'))
        m.update(str(self.timestamp).encode('utf-8'))
        m.update(json.dumps(self.data, separators=(',', ':')).encode('utf-8'))
        return m.hexdigest()


class BlockChain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]

    def createGenesisBlock(self):
        return Block(0, 0, "Genesis Block", "0")

    def getLatestBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock):
        newBlock.previousHash = self.getLatestBlock().hash
        newBlock.hash = newBlock.calculateHash()
        self.chain.append(newBlock)


if __name__ == "__main__":
    kecoin = BlockChain()
    kecoin.addBlock(Block(1, time.time(), {"ammount": 4}))
    kecoin.addBlock(Block(1, time.time(), {"ammount": 10}))

    print(json.dumps(kecoin))

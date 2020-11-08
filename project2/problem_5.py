from datetime import datetime
import hashlib


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp      = timestamp
        self.data           = data
        self.previous_hash  = previous_hash
        self.hash           = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        pass


if __name__ == '__main__':
    block = Block(datetime.utcnow(), '', '')
    print(block.hash)
    print(block.timestamp)
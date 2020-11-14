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
        hash_data = self.data.encode('utf-8')
        sha.update(hash_data)

        return sha.hexdigest()

    def __repr__(self):
        return f"timestamp: {self.timestamp}, data: {self.data}, hash: {self.hash}"


class BlockChain:
    def __init__(self):
        self.tail = None
        self.size = 0

    def add(self, data):
        if self.tail is None:
            self.tail = Block(datetime.utcnow().timestamp(), data, None)
        else:
            tail = self.tail
            new_block = Block(datetime.utcnow().timestamp(), data, tail)
            self.tail = new_block

        self.size += 1
        return self.tail

    def find(self, data):
        if self.tail is None:
            return 'empty chain'

        for block in self.to_list():
            if block.data == data:
                return block

        return None

    def to_list(self):
        out = []
        tail = self.tail
        while tail is not None:
            out.append(tail)
            tail = tail.previous_hash

        return out

    def __repr__(self):
        if self.tail is None:
            return 'empty chain'

        blocks = ''
        for item in self.to_list():
            blocks += str(item) + '\n'

        return blocks.strip()


def test_1():
    print("test 1: Chain with five blocks")

    blockchain = BlockChain()

    print(blockchain)
    # empty chain

    print(blockchain.add("block1"))
    # timestamp: 1605291729.380887, data: block1, hash: 9a59c5f8229aab55e9f855173ef94485aab8497eea0588f365c871d6d0561722

    print(blockchain.add("block2"))
    # timestamp: 1605291729.381191, data: block2, hash: 6d0b07ee773591f2a1b492d3ca65afdefc90e1cadfcc542a74048bb0ae7daa27

    print(blockchain.add("block3"))
    # timestamp: 1605291729.381198, data: block3, hash: 7e56ddaff5ff44d9e1732b1fd138a2057df045b163385068988554f72047e272

    print(blockchain.add("block4"))
    # timestamp: 1605291729.381203, data: block4, hash: 215008ba416eb06b8cfd53814660a43255e4ccc8703080af501ea0eaf7b7fdea

    print(blockchain.add("block5"))
    # timestamp: 1605291729.381207, data: block5, hash: 2e134675975ce520a5b2f59a4a13846a399d73c3152647a6c1757842f8864f0b

    print(blockchain)
    # timestamp: 1605291729.381207, data: block5, hash: 2e134675975ce520a5b2f59a4a13846a399d73c3152647a6c1757842f8864f0b
    # timestamp: 1605291729.381203, data: block4, hash: 215008ba416eb06b8cfd53814660a43255e4ccc8703080af501ea0eaf7b7fdea
    # timestamp: 1605291729.381198, data: block3, hash: 7e56ddaff5ff44d9e1732b1fd138a2057df045b163385068988554f72047e272
    # timestamp: 1605291729.381191, data: block2, hash: 6d0b07ee773591f2a1b492d3ca65afdefc90e1cadfcc542a74048bb0ae7daa27
    # timestamp: 1605291729.380887, data: block1, hash: 9a59c5f8229aab55e9f855173ef94485aab8497eea0588f365c871d6d0561722


def test_2():
    print("test 2: Chain size")

    blockchain = BlockChain()

    print(blockchain.add("block1"))
    # timestamp: 1605292403.698623, data: block1, hash: 9a59c5f8229aab55e9f855173ef94485aab8497eea0588f365c871d6d0561722

    print(blockchain.add("block2"))
    # timestamp: 1605292403.698976, data: block2, hash: 6d0b07ee773591f2a1b492d3ca65afdefc90e1cadfcc542a74048bb0ae7daa27

    print(blockchain.add("block3"))
    # timestamp: 1605291729.698991, data: block3, hash: 7e56ddaff5ff44d9e1732b1fd138a2057df045b163385068988554f72047e272

    print(blockchain.size)
    # 3


def test_3():
    print("test 3: Find Block")

    blockchain = BlockChain()

    print(blockchain.add("block1"))
    # timestamp: 1605292573.398235, data: block1, hash: 9a59c5f8229aab55e9f855173ef94485aab8497eea0588f365c871d6d0561722

    print(blockchain.add("block2"))
    # timestamp: 1605292573.398737, data: block2, hash: 6d0b07ee773591f2a1b492d3ca65afdefc90e1cadfcc542a74048bb0ae7daa27

    print(blockchain.find("block"))
    # None


def test_4():
    print("test 4: Edge case with zero length of blockchain")

    blockchain = BlockChain()
    print(blockchain)
    # empty chain
    print(blockchain.size)
    # 0


if __name__ == '__main__':
    # NOTE: Your timestamp value will be different
    test_1()
    test_2()
    test_3()
    test_4()

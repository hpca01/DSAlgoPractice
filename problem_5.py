import datetime
import hashlib
from time import sleep


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
    
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.tail = None
    
    def add_data(self, data):
        if not self.tail:
            self.tail = Block(datetime.datetime.now(), data, None)
        else:
            curr = Block(datetime.datetime.now(), data, self.tail)
            self.tail = curr
    
    def peek(self):
        if not self.tail:
            return None
        else:
            return (self.tail.data, self.tail.timestamp)

    def __repr__(self):
        output = ""
        curr = self.tail
        while curr:
            output+=" Data: {} Time: {} \n".format(curr.data, curr.timestamp)
            curr = curr.previous_hash
        return output
            

def test1():
    '''Test to see if blockchain can hold data and represent accurately'''
    chain = BlockChain()
    print(f'Creating blockchain')
    for x in range(1,10):
        chain.add_data(x)
        print(f'Adding block {x} to the chain')
        sleep(1)
    print(f'Printing chain')
    print(chain)

def test2():
    pass

def test3():
    pass

if __name__ == "__main__":
    test1()
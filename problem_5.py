import datetime
import inspect
import hashlib
from time import sleep


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(self.data, self.timestamp)
    
    def calc_hash(self, data, timestamp:datetime):
        sha = hashlib.sha256()
        hash_str = "{} - {}".format(data, timestamp).encode('UTF-8')
        sha.update(hash_str)
        return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.tail = None
        self.curr = None
    
    def add_data(self, data):
        if not data:
            return
        if not self.tail:
            self.tail = Block(datetime.datetime.now(), data, None)
        else:
            curr = Block(datetime.datetime.now(), data, self.tail)
            self.tail = curr
        self.curr = self.tail
    
    def peek(self):
        if not self.tail:
            return None
        else:
            return (self.tail.data, self.tail.timestamp)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curr is None:
            self.curr = self.tail
            raise StopIteration
        else:
            data = (self.curr.data, self.curr.timestamp)
            self.curr = self.curr.previous_hash
            return data


    def __repr__(self):
        output = ""
        curr = self.tail
        while curr:
            output+=" Data: {} Time: {} Calculated Hash: {} \n".format(curr.data, curr.timestamp, curr.hash)
            curr = curr.previous_hash
        return output
            

def test1():
    '''Test to see if blockchain can hold data and represent accurately'''
    print("Executing {}".format(inspect.stack()[0].function))
    chain = BlockChain()
    print(f'Creating blockchain')
    for x in range(1,10):
        chain.add_data(x)
        print(f'Adding block {x} to the chain')
        sleep(1)
    print(f'Printing chain ')
    print(chain)
    ### Print data from 1, 9 with time stamps
    # Data: 9 Time: 2020-06-14 10:18:07.058959
    # Data: 8 Time: 2020-06-14 10:18:06.057800
    # Data: 7 Time: 2020-06-14 10:18:05.057613
    # Data: 6 Time: 2020-06-14 10:18:04.057176
    # Data: 5 Time: 2020-06-14 10:18:03.055334
    # Data: 4 Time: 2020-06-14 10:18:02.054651
    # Data: 3 Time: 2020-06-14 10:18:01.053611
    # Data: 2 Time: 2020-06-14 10:18:00.052607
    # Data: 1 Time: 2020-06-14 10:17:59.051530

def test2():
    print("Executing {}".format(inspect.stack()[0].function))
    chain = BlockChain()
    for x in range(5):
        if x % 2 == 0:
            chain.add_data(x)
        else:
            chain.add_data(None)
    print(f'Printing chain ')
    print(chain)
    ### Print even numbers only, None should not be added
    # Data: 4 Time: 2020-06-14 10:19:30.075570
    # Data: 2 Time: 2020-06-14 10:19:30.075570

def test3():
    print("Executing {}".format(inspect.stack()[0].function))
    chain = BlockChain()
    print(chain)
    ### Print nothing

if __name__ == "__main__":
    test1()
    test2()
    test3()
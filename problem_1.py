from collections import OrderedDict
class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.size = capacity
        self.jar = OrderedDict()
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.jar:
            return -1
        else:
            rtn = self.jar.get(key)
            self.jar.move_to_end(key)
            return rtn

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key is None:
            return
        if len(self.jar) == self.size:
            self.jar.popitem(last=False)
            self.jar[key] = value
        else:
            self.jar[key] = value
        return
    
    def __str__(self):
        return f'{self.jar}'


def test_1():
    '''Basically testing to see if the cache can store and recall info'''
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(f'Cache get 1 returns -> {our_cache.get(1)} | expected result = 1')


def test_2():
    '''testing to see if the least used object gets removed'''
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.set(5, 5) 

    our_cache.get(1)

    our_cache.set(6, 6)



    print(f'Cache get 2 returns -> {our_cache.get(2)} | expected result = -1')

def test_3():
    '''entering null key to be set, should not work'''
    our_cache = LRU_Cache(5)

    [our_cache.set(None, 1) for _ in range(5)]

    print(f'Current Cache state: {our_cache} expected result is for it to be empty')

def test_4():
    '''0 capacity test case'''
    our_cache = LRU_Cache(0)

    [our_cache.set(None, 1) for _ in range(5)]

    print(f'Current Cache state: {our_cache} expected result is for it to be empty')

    

if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()

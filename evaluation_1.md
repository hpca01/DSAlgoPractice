## Solution

1. Why did you use that data structure? 
   
   I used a **ordered** dictionary because the operations are confined to limit of O(1) per specification. Dictionary aka HashTable is good for this reason. I used ordered dictionary(backwards compatability < python 3.6) because I wanted to be able to push the most recently used element to the back of the map and pop the first element when needed(size limit is reached).


2. You also need to explain the efficiency (time and space) of your solution.

    As far as the documentation goes on https://wiki.python.org/moin/TimeComplexity the stated time complexity is O(1) for each of the operations of dict except for iteration and copying. My code does neither, so I assert that my time complexity is O(1) and space complexity is related to the hash function in CPython. If I had to guess, I would say the space complexity would be O(n) as general hashmaps are implemented with arrays underneath.
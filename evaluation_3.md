## Solution

1. Why did you use that data structure?
    
    Data structures used: Tree, HashMap(dictionary in Python), Minheap(heapq in python)
    - Tree
      - For creating the encoding Tree as per the algorithm
    - HashMap
      - For trascribing character frequencies, and for creating a "dictionary" of character -> encoding.
    - Minheap
      - In order to keep the list of Nodes sorted so as to pick out the smallest size Node(by frequency) first.

# TODO
2. You also need to explain the efficiency (time and space) of your solution.

    Time complexity:
    - Iteration through string:
      - O(n)
    - Iteration through HashMap
      - O(n)
    - Heapq sorting:
      - O(n)
    - BST traversal:
      - O(n)
    - HashMap:
      - O(1)
    - BST Traversal:
      - O(n)
    
    Total : O(5n+1) --**simplified**--> O(n)

    Space complexity:
    - Frequency hashmap
      - O(n)
    - Heapq
      - O(n)
    - Hashtable of character encoding pairs:
      - O(n)
    - Output String:
      - O(n)
    - Tree
      - O(n)

    Total : O(5n) --**simplified**-->O(n)
import inspect
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.curr_pos = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        self.curr_pos = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curr_pos is None:
            self.curr_pos = self.head
            raise StopIteration
        else:
            data = self.curr_pos.value
            self.curr_pos = self.curr_pos.next
            return data
        

def union(llist_1, llist_2):
    hset = set()
    hset.update(llist_1)
    hset.update(llist_2)
    linked = LinkedList()
    for value in hset:
        linked.append(value)
    return linked

def intersection(llist_1, llist_2):
    hset = set()
    hset.update(llist_1)
    linked = LinkedList()
    for each in llist_2:
        if each in hset:
            linked.append(each)
    return linked

def test_1():
    # Test case 1
    print("Executing {}".format(inspect.stack()[0].function))
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

    #output should be
    # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
    # 6 -> 4 -> 6 -> 21 ->


def test_2():
    # Test case 2
    print("Executing {}".format(inspect.stack()[0].function))
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4))
    print (intersection(linked_list_3,linked_list_4))
    #output should be
    # 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
    #

def test_3():
    print("Executing {}".format(inspect.stack()[0].function))
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for x in range(1,9):
        linked_list_1.append(x)
    
    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))
    #output should be
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 ->
    #

if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
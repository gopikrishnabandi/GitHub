"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListTest:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        pointer = self.head
        if self.head:
            while pointer.next:
                pointer = pointer.next
            pointer.next = new_node
        else:
            self.head = new_node

    def get_position(self, position):
        pointer = self.head
        counter = 1
        if position < 1:
            return None
        while pointer.next and counter < position:
            if counter == position:
                return pointer
            pointer = pointer.next
            counter += 1
        return None


n1 = Node(11)
n2 = Node(21)
n3 = Node(31)

l1 = LinkedListTest()
l1.append(n1)
l1.append(n2)
l1.append(n3)

print(l1.get_position(1).data)

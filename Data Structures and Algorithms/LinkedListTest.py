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
        counter = 1
        pointer = self.head
        if position < 1:
            return None
        while pointer and counter <= position:
            if counter == position:
                return pointer
            pointer = pointer.next
            counter += 1
        return None

    def insert(self, new_node, position):
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        elif position > 1:
            pointer = self.head
            counter = 1
            while pointer.next and counter < position:
                if counter == position - 1:
                    new_node.next = pointer.next
                    pointer.next = new_node
                pointer = pointer.next
                counter += 1

    def delete(self, value):
        pointer = self.head
        previous = None
        while pointer.data != value and pointer.next:
            previous = current
            pointer = pointer.next
        if pointer.data == value:
            if previous:
                previous.next = pointer.next
            else:
                self.head = pointer.next


# Test cases
# Set up some Elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a LinkedList
ll = LinkedListTest(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.data)
# Should also print 3
print(ll.get_position(3).data)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).data)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).data)
# Should print 4 now
print(ll.get_position(2).data)
# Should print 3 now
print(ll.get_position(3).data)

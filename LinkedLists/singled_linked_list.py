class ListNode:
    def __init__(self, value=None):
        self.value = value 
        self.next = None  

    def __lt__(self, other):
        return self.value < other.value 

    def __repr__(self):
        return '<ListNode(value = %s, next = %s)>' % (self.value, self.next)

class LinkedList:
    """
    """

    def __init__(self, head=None):
        self.head = head
        self.values = []

    def get_array_of_values(self):
        temp = self.head
        while temp is not None:
            self.values.append(temp.value)
            temp = temp.next 
            # print(temp)
        return self.values 

    def traverse(self):
        """
        Go through each node in the LinkedList
        """
        temp = self.head
        while temp is not None:
            print(f'{temp}', end = " ")
            temp = temp.next 


    def append(self, value):
        """
        Add to the end
        """
        if self.head == None:
            self.head = ListNode(value)
            return 
        current = self.head 
        while current.next is not None:
            current = current.next 
        current.next = ListNode(value)


    def prepend(self, value):
        """Add to the beginning"""
        new_head = ListNode(value)
        new_head.next = self.head 
        self.head = new_head


    def __get_length(self):
        """ Find the length of the LinkedList"""
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next 
            count += 1 
        return count 


    def append_to_middle(self, value):
        """ Add ListNode to the middle of the LinkedList"""
        length_of_list = self.__get_length()
        middle = length_of_list // 2 
        if self.head is None:
            self.head = ListNode(value)
            return 
        else:
            new_node = ListNode(value)
            slow, fast = self.head, self.head.next 
            while fast is not None and fast.next is not None:
                slow = slow.next 
                fast = fast.next.next 
            new_node.next = slow.next 
            slow.next = new_node 


    def delete_with_value(self, value):
        """ """
        if self.head == None:
            return 
        if self.head.value == value:
            self.head = self.head.next 
            return self.head
        current = self.head 
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next  
                
            current = current.next 


    def delete_last(self):
        """ Remove the last node """
        temp = self.head 
        while temp.next is not None:
            prev = temp 
            temp = temp.next 
        prev.next = None 


    def delete_front(self):
        """ Remove the first node in a linked list """
        self.head = self.head.next 


def main():
    # Driver Code 
      
    # Creating the list 1.2.4.5  
    ll = LinkedList(ListNode()) 
    ll.prepend(ListNode(5)) 
    ll.prepend(ListNode(4)) 
    ll.prepend(ListNode(3)) 
    ll.prepend(ListNode(2)) 
    ll.append(ListNode(20)) 

    # print("Linked list before insertion: "), 
    # ll.traverse() 

    x = ListNode(1)
    # ll.append_to_middle(x) 
      
    print("\nLinked list after insertion: "), 
    # ll.traverse() 
    ll.delete_with_value(5)
    ll.traverse()
    ll.get_array_of_values()
    print(ll.values)
main()







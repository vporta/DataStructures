class ListNode:
    def __init__(self, value=None):
        self.value = value 
        self.next = None  

    def __lt__(self, other):
        return self.value < other.value 

    def __repr__(self):
        return '<ListNode(value = %s, next = %s)>' % (self.value, self.next)
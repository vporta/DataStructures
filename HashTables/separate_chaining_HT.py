# # Separate Chaining Hash Table 


class ListNode:
    def __init__(self, key, value):
        self.value = value 
        self.next = None 

    def __repr__(self):
        return f"<ListNode(value={self.value}, next={self.next})>"

class SeparateChainingHashST:
    INIT_CAPACITY: int = 4 
    n: int = None 
    st = []

    def __init__(self, m: int):
        self.m = m 
        for i in range(m):
            self.st.append(ListNode(i))
        print(self.st)

st = SeparateChainingHashST(5)

    



# Item class used as item in priority queues

class Item:

    def __init__(self, item, priority=0):
        self.item = item 
        self.priority = priority
        

    def __repr__(self):
        return f"<Item(item={self.item}, priority={self.priority})>"


    def __lt__(self, other):
        return self.priority < other.priority


    def __gt__(self, other):
        return self.priority > other.priority


    def __eq__(self, other):
        return self.priority == other.priority






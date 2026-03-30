class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Maps key to Node
        
        # Dummy nodes to prevent out-of-bounds edge cases
        self.left = Node(0, 0)  # Left marks the Least Recently Used (LRU)
        self.right = Node(0, 0) # Right marks the Most Recently Used (MRU)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node):
        """Removes an existing node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node: Node):
        """Inserts a node right before the right dummy node (MRU position)."""
        prev_node = self.right.prev
        next_node = self.right
        
        prev_node.next = node
        next_node.prev = node
        
        node.prev = prev_node
        node.next = next_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node) # Remove from its current position
            self.insert(node) # Re-insert at the MRU position
            return node.value
        return -1
            
    def put(self, key: int, value: int) -> None:   
        if key in self.cache:
            # If it already exists, remove the old node
            self.remove(self.cache[key])
            
        # Create a new node and place it in the cache and list
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)
        
        # If capacity is exceeded, evict the LRU node
        if len(self.cache) > self.cap:
            lru = self.left.next # The node just after the left dummy head
            self.remove(lru)
            del self.cache[lru.key] # Delete it from the dictionary
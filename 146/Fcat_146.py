class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.link_list_head = None
        self.link_list_tail = None
        self.node_map = {}

    def move_node_to_head(self, node):
        if len(self.node_map) < 2:
            return
        next = node.next
        prev = node.prev
        if next is not None and prev is not None:
            node.next.prev = node.prev
            node.prev.next = node.next
        elif next is None:
            self.link_list_tail = node.prev
            node.prev.next = None
        elif prev is None:
            return

        node.prev = None
        node.next = self.link_list_head
        self.link_list_head.prev = node
        self.link_list_head = node

    def get(self, key: int) -> int:
        if key in self.node_map:
            node = self.node_map[key]
            self.move_node_to_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self.move_node_to_head(node)
            return

        if len(self.node_map.keys()) == self.capacity:
            pop_node = self.node_map[self.link_list_tail.key]
            if pop_node.prev is not None:
                pop_node.prev.next = None
            else:
                self.link_list_head = None
            del self.node_map[pop_node.key]
            self.link_list_tail = pop_node.prev

        new_node = Node(key, value, next=self.link_list_head)
        if self.link_list_head is not None:
            self.link_list_head.prev = new_node
        self.link_list_head = new_node
        self.node_map[key] = new_node
        if self.link_list_tail is None:
            self.link_list_tail = new_node


lru = LRUCache(2)
lru.put(2,1)
lru.put(3,2)
print(lru.get(3))
print(lru.get(2))
lru.put(4,3)
print(lru.get(2))
print(lru.get(3))
print(lru.get(4))
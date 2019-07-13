class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_value(self):
        return self.value

    def get_key(self):
        return self.key

    def set_next(self, next):
        self.next = next

    def get_next(self, next):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, key, value):
        """
        Insert an item with given key value
        """
        node = Node(key, value)
        node.set_next(self.head)
        self.head = node
        self.size += 1

    def search(self, key):
        """
        Search for a item with a given key
        """
        cur, found = self.head, False
        while cur != None and not found:
            if cur.get_key() == key:
                return True
        return False

    def get(self, key):
        """
        Retrive an item with a given key
        """
        cur, found = self.head, False
        while cur != None and not found:
            if cur.get_key() == key:
                return cur
        # If not found raise KeyError
        raise KeyError

    def remove(self, key):
        """
        Removes node with key value equal to key
        """
        if self.head == None:
            raise KeyError

        cur, prev, found = self.head, None, False
        while not found:
            if cur.get_key() == key:
                found = True
            else:
                prev = cur
                cur = cur.get_next()
        if prev == None:
            self.head = self.head.get_next()
        else:
            prev.set_next(cur.get_next())

        # If not found raise KeyError
        if not found:
            raise KeyError
        else:
            self.size -= 1

    def length(self):
        return self.size


class HashTable:
    def __init__(self, size):
        """
        Initialize the hash table structure
        """
        self.size = size
        self.length = 0
        self.hash_table = []
        for _ in range(self.size):
            self.hash_table.append(LinkedList())

    def get_index(self, key):
        """
        Get index in hash table 
        """
        return hash(key) % self.size

    def get_item(self, key):
        """
        Get value with an key, returns value if present 
        otherwise raises an IndexError
        """
        index = self.get_index(key)
        return self.hash_table[index].get(key).get_value()

    def set_item(self, key, value):
        """
        Set an key and value in hash table
        """
        index = self.get_index(key)
        self.hash_table[index].insert(key, value)
        self.length += 1

    def delete_item(self, key):
        """
        Delete an item with a given key
        """
        index = self.get_index(key)
        self.hash_table[index].remove(key)
        self.length -= 1

    def search(self, key):
        """
        Search for an item with given key
        """
        index = self.get_index(key)
        return self.hash_table[index].search(key)

    def __setitem__(self, key, value):
        """
        Set an key and value in hash table
        """
        self.set_item(key, value)

    def __getitem__(self, key):
        """
        Get value with an key if present
        """
        return self.get_item(key)

    def __delitem__(self, key):
        """
        Delete an item with a given key
        """
        self.delete_item(key)

    def __contains__(self, key):
        """
        Search for an item with given key
        """
        return self.search(key)

    def __len__(self):
        return self.length


if __name__ == "__main__":
    hash_table = HashTable(100)
    print(len(hash_table))
    print("hello" in hash_table)
    hash_table["hello"] = "world"
    print(len(hash_table))
    hash_table["foo"] = "bar"
    print(hash_table["foo"])
    del hash_table["bar"]

class HashTable:
    def __init__(self):
        self.table = {}

    def __contains__(self, key):
        return key in self.table

    def __len__(self):
        return len(self.table)
    def insert(self, key, value):
        self.table[key] = value

hash_table = HashTable()
hash_table.insert("key", "value")
hash_table.insert("key1", "value1")
print(len(hash_table))
print("key" in hash_table)
print("key2" in hash_table)
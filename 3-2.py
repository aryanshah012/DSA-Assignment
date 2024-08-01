class HashMapLinearProbing:
    def __init__(self, capacity=101):
        self.capacity = capacity
        self.size = 0
        self.table = [(-1, -1)] * capacity
        self.occupied = [False] * capacity

    def _hash(self, key):
        return key % self.capacity

    def find(self, key):
        index = self._hash(key)
        original_index = index
        while self.occupied[index]:
            if self.table[index][0] == key:
                return True
            index = (index + 1) % self.capacity
            if index == original_index:
                break
        return False

    def insert(self, key, value):
        if self.size >= self.capacity:
            print("HashMap is full")
            return

        index = self._hash(key)
        while self.occupied[index]:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.capacity

        self.table[index] = (key, value)
        self.occupied[index] = True
        self.size += 1

    def remove(self, key):
        index = self._hash(key)
        original_index = index
        while self.occupied[index]:
            if self.table[index][0] == key:
                self.table[index] = (-1, -1)
                self.occupied[index] = False
                self.size -= 1
                return
            index = (index + 1) % self.capacity
            if index == original_index:
                break

    def print(self):
        for i in range(self.capacity):
            if self.occupied[i]:
                print(f"{{{self.table[i][0]}, {self.table[i][1]}}}", end=" ")
        print()


class HashMapSeparateChaining:
    def __init__(self, capacity=101):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        return key % self.capacity

    def find(self, key):
        index = self._hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                return True
        return False

    def insert(self, key, value):
        index = self._hash(key)
        for i, entry in enumerate(self.table[index]):
            if entry[0] == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.size += 1

    def remove(self, key):
        index = self._hash(key)
        for i, entry in enumerate(self.table[index]):
            if entry[0] == key:
                del self.table[index][i]
                self.size -= 1
                return

    def print(self):
        for i in range(self.capacity):
            for entry in self.table[i]:
                print(f"{{{entry[0]}, {entry[1]}}}", end=" ")
        print()


if __name__ == "__main__":
    print("HashMap with Linear Probing:")
    hashMapLP = HashMapLinearProbing()
    hashMapLP.insert(1, 100)
    hashMapLP.insert(2, 200)
    hashMapLP.insert(3, 300)
    hashMapLP.print()
    print(hashMapLP.find(2))
    hashMapLP.remove(2)
    hashMapLP.print()
    print(hashMapLP.find(2))

    print("\nHashMap with Separate Chaining:")
    hashMapSC = HashMapSeparateChaining()
    hashMapSC.insert(1, 100)
    hashMapSC.insert(2, 200)
    hashMapSC.insert(3, 300)
    hashMapSC.print()
    print(hashMapSC.find(2))
    hashMapSC.remove(2)
    hashMapSC.print()
    print(hashMapSC.find(2))

import unittest
from hash_table import HashTable


def has_pair(table, target):
    for row in range(len(table)):
        for col in range(len(table[row])):
            if table[row][col][0] == target[0] and table[row][col][1] == target[1]:
                return True
    return False


class Test(unittest.TestCase):
    size = 5
    first_pair = ["apple", 10]
    second_pair = ["orange", 20]
    third_pair = ["banana", 30]

    def test_hash_function(self):
        hash_table = HashTable(self.size)
        index = hash_table.hash_function(self.first_pair[0])

        # hash result shoul remain same
        for _ in range(100):
            self.assertEqual(hash_table.hash_function(self.first_pair[0]), index)

    def test_insert(self):
        hash_table = HashTable(self.size)

        hash_table.insert(self.first_pair[0], self.first_pair[1])
        hash_table.insert(self.second_pair[0], self.second_pair[1])
        hash_table.insert(self.third_pair[0], self.third_pair[1])

        self.assertEqual(hash_table.size, self.size)
        self.assertEqual(len(hash_table.table), self.size)
        self.assertEqual(has_pair(hash_table.table, self.first_pair), True)
        self.assertEqual(has_pair(hash_table.table, self.second_pair), True)
        self.assertEqual(has_pair(hash_table.table, self.third_pair), True)

    def test_collision_resolution(self):
        hash_table = HashTable(self.size)
        # Test for handling collisions by inserting multiple keys with the same hash
        hash_table.insert("key4", "value4")
        hash_table.insert("key14", "value14")  # Same hash

        self.assertEqual(hash_table.get("key4"), "value4")
        self.assertEqual(hash_table.get("key14"), "value14")

    def test_get(self):
        hash_table = HashTable(self.size)

        hash_table.insert(self.first_pair[0], self.first_pair[1])
        hash_table.insert(self.second_pair[0], self.second_pair[1])
        hash_table.insert(self.third_pair[0], self.third_pair[1])

        self.assertEqual(hash_table.get(self.first_pair[0]), self.first_pair[1])
        self.assertEqual(hash_table.get(self.second_pair[0]), self.second_pair[1])
        self.assertEqual(hash_table.get(self.third_pair[0]), self.third_pair[1])
        self.assertIsNone(hash_table.get("non_existing_key"))

    def test_delete(self):
        hash_table = HashTable(self.size)

        hash_table.insert(self.first_pair[0], self.first_pair[1])
        hash_table.insert(self.second_pair[0], self.second_pair[1])
        hash_table.insert(self.third_pair[0], self.third_pair[1])

        hash_table.delete(self.first_pair[0])
        hash_table.delete(self.second_pair[0])
        hash_table.delete("non_existing_key")

        self.assertEqual(hash_table.get(self.third_pair[0]), self.third_pair[1])
        self.assertIsNone(hash_table.get(self.first_pair[0]))
        self.assertIsNone(hash_table.get(self.second_pair[0]))
        self.assertIsNone(hash_table.delete("non_existing_key"))

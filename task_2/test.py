import unittest
from binary_search import binary_search


class Test(unittest.TestCase):
    sorted_array = [0.1, 0.3, 0.5, 1.2, 1.5, 1.7, 2.0, 2.5, 3.1, 4.0, 4.5, 5.2, 7]

    def test_find_existing_value(self):
        iterations, upper_bound = binary_search(self.sorted_array, 1.5)

        self.assertEqual(iterations, 3)
        self.assertEqual(upper_bound, 1.5)

    def test_find_existing_mid_value(self):
        iterations, upper_bound = binary_search(self.sorted_array, 2.0)

        self.assertEqual(iterations, 1)
        self.assertEqual(upper_bound, 2.0)

    def test_get_upper_bound_for_missing_value(self):
        iterations, upper_bound = binary_search(self.sorted_array, 0.2)

        self.assertEqual(iterations, 4)
        self.assertEqual(upper_bound, 0.3)

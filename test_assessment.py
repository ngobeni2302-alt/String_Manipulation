import unittest
import assessment


class TestAssessment(unittest.TestCase):

    # 1. STRING MANIPULATION
    def test_shout_text(self):
        self.assertEqual(assessment.shout_text("hello"), "HELLO!")
        self.assertEqual(assessment.shout_text("Hi"), "HI!")

    def test_count_letter_a(self):
        self.assertEqual(assessment.count_letter_a("Apple"), 1)
        self.assertEqual(assessment.count_letter_a("Banana"), 3)

    # 2. LIST & ARRAY LOGIC
    def test_find_first_element(self):
        self.assertEqual(assessment.find_first_element([10, 20, 30]), 10)
        self.assertIsNone(assessment.find_first_element([]))
    def test_double_list(self):
        self.assertEqual(assessment.double_list([1, 2, 3]), [2, 4, 6])
        self.assertEqual(assessment.double_list([0, -5]), [0, -10])

    # 3. MATHEMATICAL OPERATIONS
    def test_is_even(self):
        self.assertTrue(assessment.is_even(4))
        self.assertFalse(assessment.is_even(7))

    def test_sum_two_numbers(self):
        self.assertEqual(assessment.sum_two_numbers(10, 5), 15)
        self.assertEqual(assessment.sum_two_numbers(-1, 1), 0)

    # 4. DICTIONARY & FREQUENCY
    def test_get_value(self):
        test_dict = {"name": "Alice", "age": 25}
        self.assertEqual(assessment.get_value(test_dict, "name"), "Alice")
        self.assertEqual(assessment.get_value(test_dict, "job"), "Not Found")

    def test_create_simple_dict(self):
        self.assertEqual(
            assessment.create_simple_dict("color", "red"),
            {"color": "red"}
        )

    # 5. SEARCHING & FILTERING
    def test_contains_negative(self):
        self.assertTrue(assessment.contains_negative([1, 2, -3, 4]))
        self.assertFalse(assessment.contains_negative([1, 2, 3]))

    def test_filter_over_ten(self):
        self.assertEqual(assessment.filter_over_ten([5, 12, 8, 20]), [12, 20])
        self.assertEqual(assessment.filter_over_ten([1, 2, 3]), [])

    # 6. MATRIX & 2D GRIDS
    def test_get_top_left(self):
        matrix = [[5, 2], [3, 4]]
        self.assertEqual(assessment.get_top_left(matrix), 5)

    def test_count_rows(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(assessment.count_rows(matrix), 2)
        self.assertEqual(assessment.count_rows([[1], [2], [3]]), 3)

    # 7. LOGIC & CONDITIONALS
    def test_can_vote(self):
        self.assertTrue(assessment.can_vote(18))
        self.assertFalse(assessment.can_vote(17))

    def test_simple_calculator(self):
        self.assertEqual(assessment.simple_calculator(10, 5, "add"), 15)
        self.assertEqual(assessment.simple_calculator(10, 5, "sub"), 5)


if __name__ == "__main__":
    unittest.main()
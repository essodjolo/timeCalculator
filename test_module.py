import unittest
import time_calculator as tc


class MyTestCase(unittest.TestCase):
    def test_convert_time_to_24h_format(self):
        given_data = "11:05 PM"
        expected_result = "23:05"
        self.assertEqual(tc.convert_time_to_24h_format(given_data), expected_result)

        given_data = "1:05 PM"
        expected_result = "13:05"
        self.assertEqual(tc.convert_time_to_24h_format(given_data), expected_result)

        given_data = "9:45 AM"
        expected_result = "09:45"
        self.assertEqual(tc.convert_time_to_24h_format(given_data), expected_result)

        given_data = "12:22 PM"
        expected_result = "12:22"
        self.assertEqual(tc.convert_time_to_24h_format(given_data), expected_result)

        given_data = "12:05 AM"
        expected_result = "00:05"
        self.assertEqual(tc.convert_time_to_24h_format(given_data), expected_result)

    def test_convert_time_to_12h_format(self):
        given_data = "23:05"
        expected_result = "11:05 PM"
        self.assertEqual(tc.convert_time_to_12h_format(given_data), expected_result)

        given_data = "12:05"
        expected_result = "12:05 PM"
        self.assertEqual(tc.convert_time_to_12h_format(given_data), expected_result)

        given_data = "00:07"
        expected_result = "00:07 AM"
        self.assertEqual(tc.convert_time_to_12h_format(given_data), expected_result)

        given_data = "7:16"
        expected_result = "07:16 AM"
        self.assertEqual(tc.convert_time_to_12h_format(given_data), expected_result)

    def test_add_time(self):
        expected_result = "6:10 PM"
        self.assertEqual(tc.add_time("3:00 PM", "3:10"), expected_result)


if __name__ == '__main__':
    unittest.main()

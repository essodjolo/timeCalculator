import unittest
import time_calculator as tc


class MyTestCase(unittest.TestCase):
    def test_convert_time_to_24h_format(self):
        given_data = "11:05 PM"
        expected_result = "23:05"
        self.assertEqual(expected_result, tc.convert_time_to_24h_format(given_data))

        given_data = "1:05 PM"
        expected_result = "13:05"
        self.assertEqual(expected_result, tc.convert_time_to_24h_format(given_data))

        given_data = "9:45 AM"
        expected_result = "09:45"
        self.assertEqual(expected_result, tc.convert_time_to_24h_format(given_data))

        given_data = "12:22 PM"
        expected_result = "12:22"
        self.assertEqual(expected_result, tc.convert_time_to_24h_format(given_data))

        given_data = "12:05 AM"
        expected_result = "00:05"
        self.assertEqual(expected_result, tc.convert_time_to_24h_format(given_data))

    def test_convert_time_to_12h_format(self):
        given_data = "23:05"
        expected_result = "11:05 PM"
        self.assertEqual(expected_result, tc.convert_time_to_12h_format(given_data))

        given_data = "12:05"
        expected_result = "12:05 PM"
        self.assertEqual(expected_result, tc.convert_time_to_12h_format(given_data))

        given_data = "00:07"
        expected_result = "12:07 AM"
        self.assertEqual(expected_result, tc.convert_time_to_12h_format(given_data))

        given_data = "7:16"
        expected_result = "7:16 AM"
        self.assertEqual(expected_result, tc.convert_time_to_12h_format(given_data))

    def test_add_time(self):
        expected_result = "6:10 PM"
        self.assertEqual(expected_result, tc.add_time("3:00 PM", "3:10"))

        expected_result = "2:02 PM, Monday"
        self.assertEqual(expected_result, tc.add_time("11:30 AM", "2:32", "Monday"))

        expected_result = "12:03 PM"
        self.assertEqual(expected_result, tc.add_time("11:43 AM", "00:20"))

        expected_result = "1:40 AM (next day)"
        self.assertEqual(expected_result, tc.add_time("10:10 PM", "3:30"))

        expected_result = "12:03 AM, Thursday (2 days later)"
        self.assertEqual(expected_result, tc.add_time("11:43 PM", "24:20", "tueSday"))

    def test_wrong_duration(self):
        expected_result = "Duration time is incorrect."
        self.assertEqual(expected_result, tc.add_time("11:43 AM", "00:90"))
        self.assertEqual(expected_result, tc.add_time("11:43 AM", "0q:20"))
        self.assertEqual(expected_result, tc.add_time("11:43 AM", "020"))

    def test_wrong_starting_day_of_the_week(self):
        expected_result = "Starting day of the week is incorrect."
        self.assertEqual(expected_result, tc.add_time("11:43 AM", "00:20", "Tuday"))
        self.assertEqual(expected_result, tc.add_time("11:43 AM", "00:20", "Manday"))


if __name__ == '__main__':
    unittest.main()
